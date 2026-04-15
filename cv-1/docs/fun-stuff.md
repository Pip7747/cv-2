# Fun Stuff

<style>
/* ===== Guitar chord sidebar (LEFT) ===== */
#piano-zone {
    position: fixed;
    left: 0;
    top: 0;
    width: 60px;
    height: 100%;
    z-index: 9999;
}

#piano-sidebar {
    position: fixed;
    left: -90px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 4px;
    transition: left 0.3s ease;
    z-index: 10000;
    padding: 10px 6px;
    background: rgba(30, 30, 30, 0.85);
    border-radius: 0 12px 12px 0;
    backdrop-filter: blur(6px);
}

#piano-zone:hover ~ #piano-sidebar,
#piano-sidebar:hover {
    left: 0;
}

.piano-key {
    width: 72px;
    height: 72px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 15px;
    color: #1a1a2e;
    transition: transform 0.1s, box-shadow 0.1s, filter 0.1s;
    box-shadow: 0 3px 8px rgba(0,0,0,0.25);
    user-select: none;
    text-shadow: 0 1px 1px rgba(255,255,255,0.3);
}

.piano-key:active,
.piano-key.playing {
    transform: scale(0.92);
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    filter: brightness(1.15);
}

.piano-key:nth-child(1) { background: linear-gradient(135deg, #ff6b6b, #ee5a24); }
.piano-key:nth-child(2) { background: linear-gradient(135deg, #ffa502, #e67e22); }
.piano-key:nth-child(3) { background: linear-gradient(135deg, #ffd32a, #f0c419); }
.piano-key:nth-child(4) { background: linear-gradient(135deg, #7bed9f, #2ed573); }
.piano-key:nth-child(5) { background: linear-gradient(135deg, #70a1ff, #1e90ff); }
.piano-key:nth-child(6) { background: linear-gradient(135deg, #a29bfe, #6c5ce7); }

/* ===== Drum sidebar (RIGHT) ===== */
#drum-zone {
    position: fixed;
    right: 0;
    top: 0;
    width: 60px;
    height: 100%;
    z-index: 9999;
}

#drum-sidebar {
    position: fixed;
    right: -90px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 4px;
    transition: right 0.3s ease;
    z-index: 10000;
    padding: 10px 6px;
    background: rgba(30, 30, 30, 0.85);
    border-radius: 12px 0 0 12px;
    backdrop-filter: blur(6px);
}

#drum-zone:hover ~ #drum-sidebar,
#drum-sidebar:hover {
    right: 0;
}

.drum-key {
    width: 72px;
    height: 72px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 12px;
    color: #fff;
    transition: transform 0.1s, box-shadow 0.1s, filter 0.1s;
    box-shadow: 0 3px 8px rgba(0,0,0,0.35);
    user-select: none;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.drum-key:active,
.drum-key.playing {
    transform: scale(0.88);
    box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    filter: brightness(1.2);
}

.drum-key:nth-child(1) { background: radial-gradient(circle at 35% 35%, #e74c3c, #922b21); }
.drum-key:nth-child(2) { background: radial-gradient(circle at 35% 35%, #f39c12, #b7950b); }
.drum-key:nth-child(3) { background: radial-gradient(circle at 35% 35%, #2ecc71, #1a9850); }
.drum-key:nth-child(4) { background: radial-gradient(circle at 35% 35%, #3498db, #21618c); }
.drum-key:nth-child(5) { background: radial-gradient(circle at 35% 35%, #9b59b6, #6c3483); }
.drum-key:nth-child(6) { background: radial-gradient(circle at 35% 35%, #e67e22, #a04000); }

/* ===== Chord display overlay ===== */
#chord-display {
    position: fixed;
    left: 50%;
    top: 30%;
    transform: translate(-50%, -50%);
    font-size: 64px;
    font-weight: 800;
    opacity: 0;
    transition: opacity 0.2s, transform 0.3s;
    pointer-events: none;
    z-index: 10001;
    text-shadow: 0 2px 20px rgba(0,0,0,0.2);
}

#chord-display.show {
    opacity: 1;
    transform: translate(-50%, -55%);
}

/* ===== Drum display overlay ===== */
#drum-display {
    position: fixed;
    left: 50%;
    top: 45%;
    transform: translate(-50%, -50%);
    font-size: 42px;
    font-weight: 700;
    opacity: 0;
    transition: opacity 0.15s, transform 0.2s;
    pointer-events: none;
    z-index: 10001;
    text-shadow: 0 2px 15px rgba(0,0,0,0.3);
    color: #e74c3c;
}

#drum-display.show {
    opacity: 1;
    transform: translate(-50%, -55%);
}

/* ===== Song cards ===== */
.song-card {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border-radius: 12px;
    padding: 18px 22px;
    margin: 12px 0;
    color: #eee;
    border-left: 4px solid;
    transition: transform 0.2s, box-shadow 0.2s;
}
.song-card:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.song-card h4 { margin: 0 0 4px 0; color: #ffd32a; font-size: 17px; }
.song-card .artist { color: #a0a0a0; font-size: 13px; margin-bottom: 10px; }
.song-card .progression {
    font-family: 'Courier New', monospace;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #70a1ff;
}
.song-card .progression span {
    display: inline-block;
    background: rgba(112, 161, 255, 0.12);
    padding: 2px 10px;
    border-radius: 6px;
    margin: 2px 4px;
    cursor: pointer;
    transition: background 0.15s;
}
.song-card .progression span:hover {
    background: rgba(112, 161, 255, 0.3);
}

/* ===== Launchpad ===== */
#launchpad {
    margin: 28px 0 32px;
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #101820, #1b2735);
    color: #f5f7fa;
    box-shadow: 0 18px 40px rgba(0,0,0,0.28);
}

.launchpad-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 10px;
}

.launchpad-title {
    margin: 0;
    font-size: 24px;
    color: #ffd32a;
}

.launchpad-subtitle {
    margin: 6px 0 0;
    color: #d7dce2;
    font-size: 14px;
}

.transport {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
}

.transport label {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 14px;
}

.transport button,
.transport input {
    border: none;
    border-radius: 10px;
    padding: 10px 12px;
    font-size: 14px;
}

.transport button {
    background: #ffd32a;
    color: #111;
    font-weight: 700;
    cursor: pointer;
}

.transport button.secondary {
    background: #dfe6e9;
}

.transport button.recording {
    background: #ff6b6b;
    color: #fff;
}

.transport input {
    width: 72px;
    background: #f4f4f4;
    color: #111;
}

#launchpad-status {
    margin: 10px 0 16px;
    color: #9fd3ff;
    min-height: 20px;
    font-size: 14px;
}

.launchpad-grid {
    display: grid;
    grid-template-columns: 110px repeat(8, minmax(40px, 1fr));
    gap: 8px;
}

.lp-label,
.lp-step-label {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    border-radius: 10px;
    background: rgba(255,255,255,0.06);
    font-weight: 700;
}

.lp-step-label {
    color: #9fd3ff;
    font-size: 13px;
}

.lp-label {
    justify-content: flex-start;
    padding-left: 12px;
    color: #f5f7fa;
}

.lp-cell {
    min-height: 42px;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    background: rgba(255,255,255,0.08);
    cursor: pointer;
    transition: transform 0.12s ease, background 0.12s ease, box-shadow 0.12s ease;
}

.lp-cell:hover {
    transform: translateY(-1px);
    background: rgba(255,255,255,0.14);
}

.lp-cell.active {
    background: linear-gradient(135deg, #1e90ff, #6c5ce7);
    box-shadow: 0 0 0 2px rgba(255,255,255,0.12) inset;
}

.lp-cell.playhead {
    outline: 2px solid #ffd32a;
    outline-offset: -2px;
}

@media (max-width: 900px) {
    .launchpad-grid {
        grid-template-columns: 88px repeat(8, minmax(28px, 1fr));
        gap: 6px;
    }

    .lp-label,
    .lp-step-label,
    .lp-cell {
        min-height: 36px;
        font-size: 12px;
    }
}
</style>

<!-- LEFT: Guitar chords -->
<div id="piano-zone"></div>

<div id="piano-sidebar">
    <button class="piano-key" data-chord="C" onclick="playChord('C')">C</button>
    <button class="piano-key" data-chord="Dm" onclick="playChord('Dm')">Dm</button>
    <button class="piano-key" data-chord="Em" onclick="playChord('Em')">Em</button>
    <button class="piano-key" data-chord="F" onclick="playChord('F')">F</button>
    <button class="piano-key" data-chord="G" onclick="playChord('G')">G</button>
    <button class="piano-key" data-chord="Am" onclick="playChord('Am')">Am</button>
</div>

<!-- RIGHT: Drum pads -->
<div id="drum-zone"></div>

<div id="drum-sidebar">
    <button class="drum-key" data-drum="kick" onclick="playDrum('kick')">Kick</button>
    <button class="drum-key" data-drum="snare" onclick="playDrum('snare')">Snare</button>
    <button class="drum-key" data-drum="hihat" onclick="playDrum('hihat')">Hi-Hat</button>
    <button class="drum-key" data-drum="tom" onclick="playDrum('tom')">Tom</button>
    <button class="drum-key" data-drum="crash" onclick="playDrum('crash')">Crash</button>
    <button class="drum-key" data-drum="roll" onclick="playDrumRoll()">Roll</button>
</div>

<div id="chord-display"></div>
<div id="drum-display"></div>

Left edge -> Guitar chords | Right edge -> Drum kit

---

## Beat Lab

Build a quick groove, jam chords on top, or record a live take from the side pads.

<div id="launchpad">
    <div class="launchpad-header">
        <div>
            <h3 class="launchpad-title">Launchpad</h3>
            <p class="launchpad-subtitle">8-step sequencer for drums and chords. Live taps are recorded too.</p>
        </div>
        <div class="transport">
            <label for="bpm-input">BPM <input id="bpm-input" type="number" min="60" max="180" value="96"></label>
            <button id="sequencer-toggle" onclick="toggleSequencer()">Play</button>
            <button class="secondary" onclick="stopSequencer()">Stop</button>
            <button class="secondary" onclick="clearPattern()">Clear</button>
            <button id="record-toggle" onclick="togglePerformanceRecording()">Record</button>
            <button class="secondary" onclick="playLiveTake()">Play Take</button>
        </div>
    </div>
    <div id="launchpad-status">Click cells to program a groove. Use the side pads to overdub a live take.</div>
    <div class="launchpad-grid" id="launchpad-grid"></div>
</div>

---

## Famous Chord Progressions

Try playing these on the guitar keys! Click any chord in a song to hear it.

<div class="song-card" style="border-color: #ff6b6b;">
<h4>You're My Best Friend - Queen</h4>
<div class="artist">Queen · A Night at the Opera (1975)</div>
<div class="progression">
<span onclick="playChord('C')">C</span> <span onclick="playChord('F')">F</span> <span onclick="playChord('C')">C</span> <span onclick="playChord('F')">F</span>
</div>
</div>

<div class="song-card" style="border-color: #a29bfe;">
<h4>Red Wine Supernova - Chappell Roan</h4>
<div class="artist">Chappell Roan · The Rise and Fall of a Midwest Princess (2023)</div>
<div class="progression">
<span onclick="playChord('C')">C</span> <span onclick="playChord('F')">F</span> <span onclick="playChord('Am')">Am</span> <span onclick="playChord('G')">G</span>
</div>
</div>

<div class="song-card" style="border-color: #ee5a24;">
<h4>Songbird - Oasis</h4>
<div class="artist">Liam Gallagher · Standing on the Shoulder of Giants (2000)</div>
<div class="progression">
<span onclick="playChord('G')">G</span> <span onclick="playChord('G')">G</span> <span onclick="playChord('C')">C</span> <span onclick="playChord('C')">C</span>
</div>
</div>

<div class="song-card" style="border-color: #e67e22;">
<h4>Wonderwall - Oasis</h4>
<div class="artist">Noel Gallagher · (What's the Story) Morning Glory? (1995)</div>
<div class="progression">
<span onclick="playChord('Em')">Em</span> <span onclick="playChord('G')">G</span> <span onclick="playChord('D')">D</span> <span onclick="playChord('Am')">Am</span>
</div>
</div>

<div class="song-card" style="border-color: #2ed573;">
<h4>Let It Be - The Beatles</h4>
<div class="artist">Paul McCartney · Let It Be (1970)</div>
<div class="progression">
<span onclick="playChord('C')">C</span> <span onclick="playChord('G')">G</span> <span onclick="playChord('Am')">Am</span> <span onclick="playChord('F')">F</span>
</div>
</div>

<div class="song-card" style="border-color: #6c5ce7;">
<h4>Someone Like You - Adele</h4>
<div class="artist">Adele · 21 (2011)</div>
<div class="progression">
<span onclick="playChord('Am')">Am</span> <span onclick="playChord('C')">C</span> <span onclick="playChord('G')">G</span> <span onclick="playChord('F')">F</span>
</div>
</div>

<div class="song-card" style="border-color: #f0c419;">
<h4>Hotel California - Eagles</h4>
<div class="artist">Eagles · Hotel California (1977)</div>
<div class="progression">
<span onclick="playChord('Am')">Am</span> <span onclick="playChord('Em')">Em</span> <span onclick="playChord('G')">G</span> <span onclick="playChord('D')">D</span> <span onclick="playChord('F')">F</span> <span onclick="playChord('C')">C</span> <span onclick="playChord('Dm')">Dm</span> <span onclick="playChord('Em')">Em</span>
</div>
</div>

<div class="song-card" style="border-color: #1e90ff;">
<h4>Stand By Me - Ben E. King</h4>
<div class="artist">Ben E. King (1961)</div>
<div class="progression">
<span onclick="playChord('C')">C</span> <span onclick="playChord('Am')">Am</span> <span onclick="playChord('F')">F</span> <span onclick="playChord('G')">G</span>
</div>
</div>

---

| Guitar (Left) | Chord | Drum (Right) | Sound |
|:-:|:-:|:-:|:-:|
| C | C Major | Kick | Bass drum hit |
| Dm | D Minor | Snare | Snare crack |
| Em | E Minor | Hi-Hat | Closed hi-hat |
| F | F Major | Tom | Floor tom |
| G | G Major | Crash | Crash cymbal |
| Am | A Minor | Roll | Snare roll |

<script>
let audioCtx = null;
function getAudioCtx() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

const launchpadTracks = [
    { id: 'kick', label: 'Kick', type: 'drum' },
    { id: 'snare', label: 'Snare', type: 'drum' },
    { id: 'hihat', label: 'Hi-Hat', type: 'drum' },
    { id: 'crash', label: 'Crash', type: 'drum' },
    { id: 'C', label: 'C', type: 'chord' },
    { id: 'G', label: 'G', type: 'chord' },
    { id: 'Am', label: 'Am', type: 'chord' },
    { id: 'F', label: 'F', type: 'chord' }
];

const stepCount = 8;
const pattern = {};
let sequencerTimer = null;
let currentStep = 0;
let liveRecording = false;
let liveTake = [];
let recordStartTime = 0;

launchpadTracks.forEach(function(track) {
    pattern[track.id] = new Array(stepCount).fill(false);
});

const noteFreqs = {
    'C3': 130.81, 'D3': 146.83, 'E3': 164.81, 'F3': 174.61, 'G3': 196.00, 'A3': 220.00, 'B3': 246.94,
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88,
    'C5': 523.25, 'D5': 587.33, 'E5': 659.25
};

const chords = {
    'C':  ['C4', 'E4', 'G4'],
    'D':  ['D4', 'F4', 'A4'],
    'Dm': ['D4', 'F4', 'A4'],
    'Em': ['E4', 'G4', 'B4'],
    'F':  ['F3', 'A3', 'C4'],
    'G':  ['G3', 'B3', 'D4'],
    'Am': ['A3', 'C4', 'E4']
};

const chordColors = {
    'C': '#ee5a24', 'D': '#e67e22', 'Dm': '#e67e22', 'Em': '#f0c419',
    'F': '#2ed573', 'G': '#1e90ff', 'Am': '#6c5ce7'
};

function playGuitarNote(ctx, freq, startTime) {
    var osc1 = ctx.createOscillator();
    var g1 = ctx.createGain();
    osc1.type = 'sawtooth';
    osc1.frequency.value = freq;
    g1.gain.setValueAtTime(0.15, startTime);
    g1.gain.exponentialRampToValueAtTime(0.001, startTime + 0.08);
    osc1.connect(g1);
    g1.connect(ctx.destination);
    osc1.start(startTime);
    osc1.stop(startTime + 0.08);

    var osc2 = ctx.createOscillator();
    var g2 = ctx.createGain();
    osc2.type = 'triangle';
    osc2.frequency.value = freq;
    g2.gain.setValueAtTime(0.12, startTime);
    g2.gain.setValueAtTime(0.12, startTime + 0.01);
    g2.gain.exponentialRampToValueAtTime(0.001, startTime + 1.2);
    osc2.connect(g2);
    g2.connect(ctx.destination);
    osc2.start(startTime);
    osc2.stop(startTime + 1.2);

    var osc3 = ctx.createOscillator();
    var g3 = ctx.createGain();
    osc3.type = 'sine';
    osc3.frequency.value = freq * 2;
    g3.gain.setValueAtTime(0.04, startTime);
    g3.gain.exponentialRampToValueAtTime(0.001, startTime + 0.5);
    osc3.connect(g3);
    g3.connect(ctx.destination);
    osc3.start(startTime);
    osc3.stop(startTime + 0.5);

    var osc4 = ctx.createOscillator();
    var g4 = ctx.createGain();
    osc4.type = 'sine';
    osc4.frequency.value = freq * 3;
    g4.gain.setValueAtTime(0.015, startTime);
    g4.gain.exponentialRampToValueAtTime(0.001, startTime + 0.25);
    osc4.connect(g4);
    g4.connect(ctx.destination);
    osc4.start(startTime);
    osc4.stop(startTime + 0.25);
}

function playChord(chordName) {
    var ctx = getAudioCtx();
    var notes = chords[chordName];
    if (!notes) return;
    var now = ctx.currentTime;

    recordHit('chord', chordName);

    notes.forEach(function(note, i) {
        playGuitarNote(ctx, noteFreqs[note], now + i * 0.025);
    });

    var btn = document.querySelector('.piano-key[data-chord="' + chordName + '"]');
    if (btn) {
        btn.classList.add('playing');
        setTimeout(function() { btn.classList.remove('playing'); }, 200);
    }

    var display = document.getElementById('chord-display');
    display.textContent = chordName;
    display.style.color = chordColors[chordName] || '#70a1ff';
    display.classList.add('show');
    setTimeout(function() { display.classList.remove('show'); }, 800);
}

function playDrum(type) {
    var ctx = getAudioCtx();
    var now = ctx.currentTime;

    recordHit('drum', type);

    if (type === 'kick') {
        var osc = ctx.createOscillator();
        var g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(150, now);
        osc.frequency.exponentialRampToValueAtTime(40, now + 0.12);
        g.gain.setValueAtTime(0.8, now);
        g.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
        osc.connect(g); g.connect(ctx.destination);
        osc.start(now); osc.stop(now + 0.4);
    }
    else if (type === 'snare') {
        var bufSize = ctx.sampleRate * 0.15;
        var buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
        var data = buf.getChannelData(0);
        for (var i = 0; i < bufSize; i++) data[i] = Math.random() * 2 - 1;
        var noise = ctx.createBufferSource();
        noise.buffer = buf;
        var nGain = ctx.createGain();
        nGain.gain.setValueAtTime(0.5, now);
        nGain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        var filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.value = 3000;
        noise.connect(filter); filter.connect(nGain); nGain.connect(ctx.destination);
        noise.start(now);
        var osc = ctx.createOscillator();
        var g = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.value = 180;
        g.gain.setValueAtTime(0.35, now);
        g.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.connect(g); g.connect(ctx.destination);
        osc.start(now); osc.stop(now + 0.08);
    }
    else if (type === 'hihat') {
        var bufSize = ctx.sampleRate * 0.06;
        var buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
        var data = buf.getChannelData(0);
        for (var i = 0; i < bufSize; i++) data[i] = Math.random() * 2 - 1;
        var noise = ctx.createBufferSource();
        noise.buffer = buf;
        var filter = ctx.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 7000;
        var g = ctx.createGain();
        g.gain.setValueAtTime(0.3, now);
        g.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
        noise.connect(filter); filter.connect(g); g.connect(ctx.destination);
        noise.start(now);
    }
    else if (type === 'tom') {
        var osc = ctx.createOscillator();
        var g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(120, now);
        osc.frequency.exponentialRampToValueAtTime(70, now + 0.2);
        g.gain.setValueAtTime(0.6, now);
        g.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.connect(g); g.connect(ctx.destination);
        osc.start(now); osc.stop(now + 0.35);
    }
    else if (type === 'crash') {
        var bufSize = ctx.sampleRate * 0.8;
        var buf = ctx.createBuffer(1, bufSize, ctx.sampleRate);
        var data = buf.getChannelData(0);
        for (var i = 0; i < bufSize; i++) data[i] = Math.random() * 2 - 1;
        var noise = ctx.createBufferSource();
        noise.buffer = buf;
        var filter = ctx.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.value = 4000;
        var g = ctx.createGain();
        g.gain.setValueAtTime(0.35, now);
        g.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
        noise.connect(filter); filter.connect(g); g.connect(ctx.destination);
        noise.start(now);
    }

    var btn = document.querySelector('.drum-key[data-drum="' + type + '"]');
    if (btn) {
        btn.classList.add('playing');
        setTimeout(function() { btn.classList.remove('playing'); }, 150);
    }

    var dd = document.getElementById('drum-display');
    var labels = { kick: '💥 Kick', snare: '🪘 Snare', hihat: '🎩 Hi-Hat', tom: '🔊 Tom', crash: '💫 Crash' };
    dd.textContent = labels[type] || type;
    dd.classList.add('show');
    setTimeout(function() { dd.classList.remove('show'); }, 500);
}

function playDrumRoll() {
    var count = 12;
    for (var i = 0; i < count; i++) {
        (function(idx) {
            setTimeout(function() { playDrum('snare'); }, idx * 60);
        })(i);
    }
    var dd = document.getElementById('drum-display');
    dd.textContent = '🥁 DRUM ROLL!';
    dd.classList.add('show');
    setTimeout(function() { dd.classList.remove('show'); }, 1000);
}

function setLaunchpadStatus(message) {
    var status = document.getElementById('launchpad-status');
    if (status) {
        status.textContent = message;
    }
}

function buildLaunchpad() {
    var grid = document.getElementById('launchpad-grid');
    if (!grid) return;

    grid.innerHTML = '';

    var spacer = document.createElement('div');
    spacer.className = 'lp-step-label';
    spacer.textContent = 'Track';
    grid.appendChild(spacer);

    for (var step = 0; step < stepCount; step++) {
        var stepLabel = document.createElement('div');
        stepLabel.className = 'lp-step-label';
        stepLabel.textContent = String(step + 1);
        grid.appendChild(stepLabel);
    }

    launchpadTracks.forEach(function(track) {
        var label = document.createElement('div');
        label.className = 'lp-label';
        label.textContent = track.label;
        grid.appendChild(label);

        for (var stepIndex = 0; stepIndex < stepCount; stepIndex++) {
            (function(trackId, currentIndex) {
                var cell = document.createElement('button');
                cell.type = 'button';
                cell.className = 'lp-cell';
                cell.dataset.track = trackId;
                cell.dataset.step = String(currentIndex);
                cell.onclick = function() {
                    pattern[trackId][currentIndex] = !pattern[trackId][currentIndex];
                    cell.classList.toggle('active', pattern[trackId][currentIndex]);
                    if (pattern[trackId][currentIndex]) {
                        getAudioCtx();
                        triggerTrack(trackId);
                    }
                };
                grid.appendChild(cell);
            })(track.id, stepIndex);
        }
    });
}

function updatePlayhead(step) {
    var cells = document.querySelectorAll('.lp-cell');
    cells.forEach(function(cell) {
        cell.classList.toggle('playhead', Number(cell.dataset.step) === step);
    });
}

function clearPlayhead() {
    var cells = document.querySelectorAll('.lp-cell');
    cells.forEach(function(cell) {
        cell.classList.remove('playhead');
    });
}

function triggerTrack(trackId) {
    var drumIds = ['kick', 'snare', 'hihat', 'crash'];
    if (drumIds.indexOf(trackId) >= 0) {
        playDrum(trackId);
    } else {
        playChord(trackId);
    }
}

function getStepDurationMs() {
    var bpmInput = document.getElementById('bpm-input');
    var bpm = bpmInput ? Number(bpmInput.value) : 96;
    if (!bpm || bpm < 60) bpm = 60;
    if (bpm > 180) bpm = 180;
    if (bpmInput) bpmInput.value = bpm;
    return (60 / bpm) * 1000 / 2;
}

function runSequencerStep() {
    launchpadTracks.forEach(function(track) {
        if (pattern[track.id][currentStep]) {
            triggerTrack(track.id);
        }
    });

    updatePlayhead(currentStep);
    currentStep = (currentStep + 1) % stepCount;
}

function toggleSequencer() {
    getAudioCtx();

    if (sequencerTimer) {
        stopSequencer();
        return;
    }

    currentStep = 0;
    runSequencerStep();
    sequencerTimer = setInterval(runSequencerStep, getStepDurationMs());

    var toggleButton = document.getElementById('sequencer-toggle');
    if (toggleButton) toggleButton.textContent = 'Pause';
    setLaunchpadStatus('Sequencer running. Change BPM anytime or tap the side pads to layer a live take.');
}

function stopSequencer() {
    if (sequencerTimer) {
        clearInterval(sequencerTimer);
        sequencerTimer = null;
    }

    clearPlayhead();
    currentStep = 0;

    var toggleButton = document.getElementById('sequencer-toggle');
    if (toggleButton) toggleButton.textContent = 'Play';
    setLaunchpadStatus('Sequencer stopped.');
}

function clearPattern() {
    launchpadTracks.forEach(function(track) {
        pattern[track.id] = new Array(stepCount).fill(false);
    });

    var cells = document.querySelectorAll('.lp-cell');
    cells.forEach(function(cell) {
        cell.classList.remove('active', 'playhead');
    });

    currentStep = 0;
    setLaunchpadStatus('Pattern cleared.');
}

function recordHit(kind, value) {
    if (!liveRecording) return;
    liveTake.push({
        kind: kind,
        value: value,
        at: performance.now() - recordStartTime
    });
}

function togglePerformanceRecording() {
    var recordButton = document.getElementById('record-toggle');
    getAudioCtx();

    if (!liveRecording) {
        liveTake = [];
        liveRecording = true;
        recordStartTime = performance.now();
        if (recordButton) {
            recordButton.textContent = 'Stop Rec';
            recordButton.classList.add('recording');
        }
        setLaunchpadStatus('Recording live taps from the side pads and launchpad playback.');
        return;
    }

    liveRecording = false;
    if (recordButton) {
        recordButton.textContent = 'Record';
        recordButton.classList.remove('recording');
    }
    setLaunchpadStatus('Recorded ' + liveTake.length + ' events. Use Play Take to hear it back.');
}

function playLiveTake() {
    if (!liveTake.length) {
        setLaunchpadStatus('No live take recorded yet. Press Record and tap the side pads first.');
        return;
    }

    getAudioCtx();
    setLaunchpadStatus('Playing back your recorded take.');

    liveTake.forEach(function(event) {
        setTimeout(function() {
            if (event.kind === 'drum') playDrum(event.value);
            if (event.kind === 'chord') playChord(event.value);
        }, event.at);
    });
}

buildLaunchpad();
</script>
