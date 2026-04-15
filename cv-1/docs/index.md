# Welcome to My Space

## About Me

Hi, I'm **Xuejiao (Liz) Qian** — a graduated computer science student based in **Brisbane, QLD** with a strong foundation in full-stack web development, cloud operations, and blockchain technology. I completed my degree in July 2025.

I'm experienced in **Java Spring** development, **Agile methodologies**, and project management using Confluence and Jira. Skilled in Git for version control and team collaboration, I contributed to a greenfield web project for the QUT Student Guild. I'm proficient in building **CI/CD pipelines** with Jenkins and deploying scalable infrastructure on **AWS**.

Previously, I developed a **blockchain-based decentralized voting system**. Currently, I'm expanding my expertise in **artificial intelligence**, focusing on **Retrieval-Augmented Generation (RAG)** and **LangChain**.

Seeking a role where I can apply both my development and problem-solving skills to contribute to innovative, forward-thinking teams.

📧 elishy.qian@gmail.com · 📱 +61 452181226 · [LinkedIn](https://linkedin.com/in/lizq)

---

### Technical Skills

- Strong **object-oriented programming** in Java development
- Building **RESTful APIs** with Java Spring Boot and Gradle
- **JPA**, **Redis** for data storage and retrieval
- **Jenkins** CI/CD, **Docker** & **Kubernetes** for containerization
- **AWS** infrastructure (ECS, S3, DynamoDB) and **Terraform** for IaC
- Blockchain technologies: **Ganache**, **MetaMask**, **Sepolia** test network

### Certifications

- **AWS Cloud Practitioner** (CLF-C01)
- **AWS Solutions Architect Associate** (SAA-C03)
- **Agile Practitioner**
- **Microsoft Build: DevOps Challenge**

### Education

- **Queensland University of Technology** — Bachelor of IT ,Computer Science Major (Feb 2023 – Jun 2025)
- **TAFE Queensland** — Diploma of Music Performance, Dynamic Drumming Major (Jan 2022 – Jan 2023)



<style>
  #resume-bot-toggle {
    position: fixed;
    right: 24px;
    bottom: 24px;
    width: 60px;
    height: 60px;
    border: none;
    border-radius: 50%;
    background: linear-gradient(135deg, #6c5ce7, #1e90ff);
    color: #fff;
    font-size: 26px;
    cursor: pointer;
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
    z-index: 9999;
  }

  #resume-bot-panel {
    position: fixed;
    right: 24px;
    bottom: 96px;
    width: 340px;
    height: 460px;
    display: none;
    flex-direction: column;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 14px 40px rgba(0,0,0,0.22);
    z-index: 9999;
  }

  #resume-bot-panel.open {
    display: flex;
  }

  #resume-bot-header {
    padding: 14px 16px;
    background: linear-gradient(135deg, #6c5ce7, #1e90ff);
    color: #fff;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  #resume-bot-close {
    background: transparent;
    border: none;
    color: #fff;
    font-size: 18px;
    cursor: pointer;
  }

  #resume-bot-messages {
    flex: 1;
    padding: 14px;
    overflow-y: auto;
    background: #f7f9fc;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .resume-bot-msg {
    max-width: 85%;
    padding: 10px 12px;
    border-radius: 12px;
    line-height: 1.4;
    font-size: 14px;
    white-space: pre-wrap;
  }

  .resume-bot-msg.bot {
    background: #e9eefb;
    color: #1f2d3d;
    align-self: flex-start;
  }

  .resume-bot-msg.user {
    background: #6c5ce7;
    color: #fff;
    align-self: flex-end;
  }

  #resume-bot-inputbar {
    display: flex;
    gap: 8px;
    padding: 12px;
    border-top: 1px solid #e5e7eb;
    background: #fff;
  }

  #resume-bot-input {
    flex: 1;
    border: 1px solid #d1d5db;
    border-radius: 10px;
    padding: 10px 12px;
    font-size: 14px;
    outline: none;
  }

  #resume-bot-send {
    border: none;
    border-radius: 10px;
    padding: 10px 14px;
    background: #1e90ff;
    color: white;
    cursor: pointer;
    font-weight: 600;
  }

  #resume-bot-send:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  @media (max-width: 520px) {
    #resume-bot-panel {
      right: 12px;
      bottom: 84px;
      width: calc(100vw - 24px);
      height: 70vh;
    }

    #resume-bot-toggle {
      right: 12px;
      bottom: 12px;
    }
  }
</style>

<button id="resume-bot-toggle" aria-label="Open resume chatbot">💬</button>

<div id="resume-bot-panel" aria-live="polite">
  <div id="resume-bot-header">
    <span>Ask about my resume</span>
    <button id="resume-bot-close" aria-label="Close chatbot">✕</button>
  </div>

  <div id="resume-bot-messages">
    <div class="resume-bot-msg bot">
      Hi — ask about my skills, education, certifications, or project experience.
    </div>
  </div>

  <div id="resume-bot-inputbar">
    <input
      id="resume-bot-input"
      type="text"
      placeholder="Type your question..."
    />
    <button id="resume-bot-send">Send</button>
  </div>
</div>

<script>
  const botToggle = document.getElementById("resume-bot-toggle");
  const botPanel = document.getElementById("resume-bot-panel");
  const botClose = document.getElementById("resume-bot-close");
  const botMessages = document.getElementById("resume-bot-messages");
  const botInput = document.getElementById("resume-bot-input");
  const botSend = document.getElementById("resume-bot-send");

  const CHAT_API = "http://127.0.0.1:8000/api/chat";

  function appendMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = `resume-bot-msg ${sender}`;
    msg.textContent = text;
    botMessages.appendChild(msg);
    botMessages.scrollTop = botMessages.scrollHeight;
    return msg;
  }

  async function sendQuestion() {
    const question = botInput.value.trim();
    if (!question) return;

    appendMessage(question, "user");
    botInput.value = "";
    botSend.disabled = true;

    const thinkingMsg = appendMessage("Thinking...", "bot");

    try {
      const res = await fetch(CHAT_API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });

      const data = await res.json();

      thinkingMsg.textContent = data.answer || "No response returned.";
    } catch (err) {
      thinkingMsg.textContent = "Chatbot is unavailable. Make sure the backend is running.";
    } finally {
      botSend.disabled = false;
      botInput.focus();
    }
  }

  botToggle.addEventListener("click", () => {
    botPanel.classList.toggle("open");
    if (botPanel.classList.contains("open")) {
      botInput.focus();
    }
  });

  botClose.addEventListener("click", () => {
    botPanel.classList.remove("open");
  });

  botSend.addEventListener("click", sendQuestion);

  botInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      sendQuestion();
    }
  });
</script>



