import os
import re
from pathlib import Path
from typing import List, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

app = FastAPI(title="Resume Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RESUME_PATH = Path(__file__).resolve().parents[1] / "resume.md"
CHAT_MODE = os.getenv("CHAT_MODE", "groq").strip().lower()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant").strip()

LAST_GROQ_MODEL_USED = None
LAST_GROQ_ERROR = None

# ✅ Load Groq client
try:
    from groq import Groq
    groq_client = Groq(api_key=GROQ_API_KEY) if (CHAT_MODE == "groq" and GROQ_API_KEY) else None
    print("✅ Groq client ready!" if groq_client else "⚠️ Groq disabled or missing key.")
except Exception as e:
    print(f"⚠️ Groq not available: {e}")
    groq_client = None

print(f"ENV loaded from: {ENV_PATH}")
print(f"CHAT_MODE: {CHAT_MODE}")
print(f"GROQ key present: {bool(GROQ_API_KEY)}")
print(f"GROQ model configured: {GROQ_MODEL}")

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

GREETINGS = {"hi", "hello", "hey", "howdy", "sup", "good morning", "good afternoon", "good evening"}

GREETING_RESPONSE = (
    "Hi there! 👋 I'm Liz's resume assistant. "
    "Feel free to ask me about her skills, work experience, certifications, education, or projects!"
)

SMALL_TALK_RESPONSES = {
    "how are you": "I'm doing well, thanks. I'm here to help with Liz's resume, experience, projects, and skills.",
    "who are you": "I'm Liz's resume assistant. You can ask me about her skills, experience, education, certifications, or projects.",
    "what can you do": "I can answer questions about Liz's background, technical skills, work experience, certifications, education, and projects.",
    "thanks": "You're welcome. Feel free to ask anything about Liz's background or projects.",
    "thank you": "You're welcome. Feel free to ask anything about Liz's background or projects.",
    "bye": "See you later. If you want, you can come back and ask more about Liz's experience or projects.",
}

REFUSAL_RESPONSE = (
    "I can help with Liz's resume, experience, skills, education, certifications, and projects, "
    "but I can't help with that request."
)

EXPLICIT_PROJECTS = [
    "Local AI Trivia Chatbot",
    "Blockchain-Based Voting System",
]

EXPERIENCE_ROLES = [
    "QUTCSSA Backend Developer",
    "35 Middle DevOps Engineer",
]

REFUSAL_PATTERNS = [
    "password",
    "secret",
    "private",
    "hack",
    "exploit",
    "bypass",
    "illegal",
    "nude",
    "sex",
    "violence",
    "kill",
    "weapon",
]

def split_markdown_into_chunks(text: str) -> List[str]:
    sections = re.split(r"(?=^#{1,6}\s)", text, flags=re.MULTILINE)
    chunks = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        parts = [p.strip() for p in section.split("\n\n") if p.strip()]
        current = ""
        for part in parts:
            candidate = f"{current}\n\n{part}".strip() if current else part
            if len(candidate) < 900:
                current = candidate
            else:
                if current:
                    chunks.append(current)
                current = part
        if current:
            chunks.append(current)
    return [c for c in chunks if len(c) > 30]

if not RESUME_PATH.exists():
    raise FileNotFoundError(f"Resume not found at: {RESUME_PATH}")

resume_text = RESUME_PATH.read_text(encoding="utf-8")
chunks = split_markdown_into_chunks(resume_text)

print(f"✅ Loaded resume: {len(chunks)} chunks")
for i, c in enumerate(chunks):
    print(f"  Chunk {i+1}: {c[:80]}...")

vectorizer = TfidfVectorizer(stop_words="english")
chunk_vectors = vectorizer.fit_transform(chunks)

def is_greeting(text: str) -> bool:
    return text.lower().strip().rstrip("!?.") in GREETINGS

def get_small_talk_reply(text: str) -> Optional[str]:
    normalized = text.lower().strip().rstrip("!?.")
    if normalized in GREETINGS:
        return GREETING_RESPONSE
    return SMALL_TALK_RESPONSES.get(normalized)

def should_refuse(text: str) -> bool:
    normalized = text.lower().strip()
    return any(pattern in normalized for pattern in REFUSAL_PATTERNS)

def get_resume_fact_answer(question: str) -> Optional[str]:
    normalized = question.lower().strip()

    if "how many" in normalized and "project" in normalized:
        return (
            f"Liz's resume explicitly lists {len(EXPLICIT_PROJECTS)} named projects: "
            + ", ".join(EXPLICIT_PROJECTS)
            + ". It also includes "
            + f"{len(EXPERIENCE_ROLES)} professional roles: "
            + ", ".join(EXPERIENCE_ROLES)
            + "."
        )

    if "how many" in normalized and any(word in normalized for word in ["role", "job", "experience", "position"]):
        return (
            f"Liz's resume lists {len(EXPERIENCE_ROLES)} professional roles: "
            + ", ".join(EXPERIENCE_ROLES)
            + "."
        )

    if "what projects" in normalized or "which projects" in normalized or "list projects" in normalized:
        return "Liz's resume explicitly lists these projects: " + ", ".join(EXPLICIT_PROJECTS) + "."

    return None

def retrieve_context(question: str, k: int = 3) -> List[str]:
    q_vec = vectorizer.transform([question])
    scores = (chunk_vectors @ q_vec.T).toarray().ravel()
    best_idx = scores.argsort()[::-1][:k]
    return [chunks[i] for i in best_idx if scores[i] > 0]

def ask_groq(question: str, context: str) -> str:
    global LAST_GROQ_MODEL_USED, LAST_GROQ_ERROR

    prompt = f"""You are a helpful assistant answering questions about Xuejiao (Liz) Qian's resume.
Answer only from the resume context below. Be concise and friendly.
If the answer is not in the context say: "I don't have that information in Liz's resume."

Resume context:
{context}

Question: {question}"""

    candidate_models = list(dict.fromkeys([
        GROQ_MODEL,
        "llama-3.1-8b-instant",
        "qwen/qwen3-32b",
        "llama-3.3-70b-versatile",
    ]))

    last_err = None
    for m in candidate_models:
        try:
            response = groq_client.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.3,
            )
            text = (response.choices[0].message.content or "").strip()
            if not text:
                raise RuntimeError(f"Empty content from model {m}")
            LAST_GROQ_MODEL_USED = m
            LAST_GROQ_ERROR = None
            print(f"✅ Groq success with model: {m}")
            return text
        except Exception as e:
            last_err = e
            LAST_GROQ_ERROR = str(e)
            print(f"Groq model failed ({m}): {e}")

    raise RuntimeError(f"All Groq models failed: {last_err}")

def generate_answer(question: str, context_chunks: List[str]) -> str:
    fact_answer = get_resume_fact_answer(question)
    if fact_answer:
        return fact_answer

    if not context_chunks:
        return (
            "I couldn't find that in Liz's resume. I can help with her skills, experience, "
            "education, certifications, and projects."
        )

    context = "\n\n".join(context_chunks)

    if groq_client:
        ans = ask_groq(question, context)  # let error surface to logs
        return ans

    return f"Based on Liz's resume:\n\n{context_chunks[0]}"

@app.get("/api/health")
def health():
    return {
        "ok": True,
        "groq_client_ready": groq_client is not None,
        "groq_model_configured": GROQ_MODEL,
        "groq_model_last_used": LAST_GROQ_MODEL_USED,
        "groq_last_error": LAST_GROQ_ERROR,
        "resume_path": str(RESUME_PATH),
        "resume_exists": RESUME_PATH.exists(),
    }
@app.get("/")
def root():
    return {"status": "ok", "message": "Resume chatbot API is running."}

@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    q = req.question.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Question is required.")

    small_talk_reply = get_small_talk_reply(q)
    if small_talk_reply:
        return ChatResponse(answer=small_talk_reply, sources=[])

    if should_refuse(q):
        return ChatResponse(answer=REFUSAL_RESPONSE, sources=[])

    context_chunks = retrieve_context(q)
    answer = generate_answer(q, context_chunks)
    return ChatResponse(answer=answer, sources=context_chunks)