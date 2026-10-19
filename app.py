# app.py
# Shantikunj Granth Khoj AI - Ultra-Premium Ambient Dark Spiritual Platform
# Developed by Sarthak | Class 12 CBSE Computer Science Project

import os
import time
import pickle
import string
import json
import urllib.request
import streamlit as st

# ----------------- PAGE CONFIGURATION -----------------
st.set_page_config(
    page_title="शांतिकुंज ग्रंथ खोज AI | Shantikunj AI",
    page_icon="🕉️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ----------------- 100% SEAMLESS DARK AMBIENT SAFFRON THEME (ZERO WHITE GLITCH) -----------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap');
    
    /* 1. Global Background Canvas (Obsidian with Radial Saffron Aura) */
    html, body, [class*="css"], .stApp, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background: #090605 !important;
        background-color: #090605 !important;
        background-image: 
            radial-gradient(circle at 50% 12%, rgba(234, 88, 12, 0.44) 0%, rgba(180, 50, 5, 0.22) 32%, rgba(9, 6, 5, 0.98) 72%),
            radial-gradient(circle at 15% 85%, rgba(194, 65, 12, 0.15) 0%, transparent 45%),
            radial-gradient(circle at 85% 85%, rgba(234, 88, 12, 0.12) 0%, transparent 45%) !important;
        background-attachment: fixed !important;
        color: #f8fafc !important;
    }

    /* 2. ELIMINATE ALL WHITE STREAMLIT CONTAINERS (HEADER, FOOTER, STBOTTOM) */
    header[data-testid="stHeader"],
    [data-testid="stHeader"],
    footer,
    [data-testid="stDecoration"],
    [data-testid="stBottom"],
    div[data-testid="stBottom"],
    div[data-testid="stBottom"] > div,
    .stChatFloatingInputContainer {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
    }
    
    [data-testid="stDecoration"] {
        display: none !important;
    }

    /* 3. Block Container Width & Spacing */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 5.5rem !important;
        max-width: 780px !important;
    }

    /* 4. Ambient Glowing 3D Celestial Orb (Savita Dev / Sun Sphere) */
    .orb-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 6px 0 16px 0;
    }
    
    .savita-orb {
        width: 130px;
        height: 130px;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 30%, #fff7ed 0%, #fed7aa 18%, #fb923c 38%, #ea580c 62%, #9a3412 84%, #431407 100%);
        box-shadow: 
            0 0 38px rgba(234, 88, 12, 0.8),
            0 0 80px rgba(234, 88, 12, 0.45),
            0 0 140px rgba(194, 65, 12, 0.28),
            inset 0 0 20px rgba(255, 255, 255, 0.5);
        animation: orbGlow 3.6s ease-in-out infinite alternate;
        position: relative;
    }

    @keyframes orbGlow {
        0% {
            transform: scale(0.96);
            box-shadow: 
                0 0 32px rgba(234, 88, 12, 0.7),
                0 0 70px rgba(234, 88, 12, 0.38),
                0 0 110px rgba(194, 65, 12, 0.22),
                inset 0 0 16px rgba(255, 255, 255, 0.4);
        }
        100% {
            transform: scale(1.04);
            box-shadow: 
                0 0 48px rgba(249, 115, 22, 0.9),
                0 0 100px rgba(234, 88, 12, 0.55),
                0 0 160px rgba(234, 88, 12, 0.35),
                inset 0 0 26px rgba(255, 255, 255, 0.65);
        }
    }

    /* 5. Top Pill Status Badge */
    .top-badge-row {
        text-align: center;
        margin-bottom: 6px;
    }
    
    .ambient-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 140, 50, 0.32);
        backdrop-filter: blur(16px);
        color: #ffedd5;
        font-size: 0.73rem;
        font-weight: 700;
        padding: 5px 16px;
        border-radius: 9999px;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        box-shadow: 0 0 18px rgba(234, 88, 12, 0.18);
    }
    
    .pulse-glow {
        width: 7px;
        height: 7px;
        background-color: #f97316;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 8px #f97316;
    }

    /* 6. Hero Typography */
    .hero-heading {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.6px;
        margin-bottom: 4px;
        text-shadow: 0 2px 22px rgba(234, 88, 12, 0.4);
    }
    
    .hero-sub {
        text-align: center;
        font-size: 0.95rem;
        color: #fed7aa;
        opacity: 0.85;
        font-weight: 400;
        margin-bottom: 10px;
    }

    .author-pill {
        display: inline-block;
        font-size: 0.81rem;
        color: #cbd5e1;
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 5px 16px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 16px;
    }
    .author-pill strong {
        color: #fb923c;
    }

    /* 7. Bento Value Grid */
    .bento-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin: 10px 0 16px 0;
    }
    @media (max-width: 640px) {
        .bento-grid {
            grid-template-columns: 1fr;
        }
    }
    .bento-card {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 140, 50, 0.16);
        border-radius: 14px;
        padding: 15px 18px;
        backdrop-filter: blur(18px);
        transition: all 0.25s ease;
    }
    .bento-card:hover {
        border-color: rgba(251, 146, 60, 0.4);
        background: rgba(255, 255, 255, 0.055);
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(234, 88, 12, 0.15);
    }
    .bento-title {
        font-size: 0.88rem;
        font-weight: 700;
        color: #ffedd5;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 6px;
    }
    .bento-desc {
        font-size: 0.8rem;
        color: #cbd5e1;
        line-height: 1.52;
    }

    /* 8. Modern Dark Chat Input Bar (Matches Image Perfectly) */
    div[data-testid="stChatInput"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    div[data-testid="stChatInput"] > div {
        background: rgba(18, 12, 9, 0.92) !important;
        border: 1px solid rgba(255, 140, 50, 0.35) !important;
        border-radius: 28px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.7), 0 0 15px rgba(234, 88, 12, 0.15) !important;
        backdrop-filter: blur(24px) !important;
        padding: 4px 8px !important;
    }
    
    div[data-testid="stChatInput"]:focus-within > div {
        border-color: #ea580c !important;
        box-shadow: 0 8px 36px rgba(0, 0, 0, 0.8), 0 0 24px rgba(234, 88, 12, 0.45) !important;
    }
    
    div[data-testid="stChatInput"] textarea {
        background: transparent !important;
        color: #ffffff !important;
        font-size: 0.95rem !important;
        font-family: inherit !important;
    }
    
    div[data-testid="stChatInput"] textarea::placeholder {
        color: #fed7aa !important;
        opacity: 0.65 !important;
    }
    
    div[data-testid="stChatInput"] button {
        background: #ea580c !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 50% !important;
        transition: transform 0.2s ease !important;
    }
    div[data-testid="stChatInput"] button:hover {
        transform: scale(1.08) !important;
        background: #f97316 !important;
    }

    /* 9. Sidebar Dark Theme */
    section[data-testid="stSidebar"] {
        background: #0d0908 !important;
        background-color: #0d0908 !important;
        border-right: 1px solid rgba(255, 140, 50, 0.18) !important;
    }
    section[data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    section[data-testid="stSidebar"] .stRadio > div {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 140, 50, 0.2);
        border-radius: 12px;
        padding: 8px 12px;
    }

    /* 10. BRIGHT CRISP CHAT MESSAGES (HIGH-CONTRAST VISIBILITY FIX) */
    [data-testid="stChatMessage"] {
        background: rgba(22, 16, 12, 0.85) !important;
        border: 1px solid rgba(255, 140, 50, 0.25) !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        margin-bottom: 14px !important;
        backdrop-filter: blur(16px) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
    }

    /* Force all text inside chat messages to be bright white & readable */
    [data-testid="stChatMessage"] * {
        color: #f8fafc !important;
    }

    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] li, 
    [data-testid="stChatMessage"] span,
    [data-testid="stChatMessage"] div {
        color: #f1f5f9 !important;
        font-size: 0.96rem !important;
        line-height: 1.68 !important;
    }

    [data-testid="stChatMessage"] strong, 
    [data-testid="stChatMessage"] b {
        color: #fed7aa !important; /* Warm glowing gold for highlights */
        font-weight: 700 !important;
    }

    [data-testid="stChatMessage"] blockquote {
        border-left: 3px solid #ea580c !important;
        background: rgba(234, 88, 12, 0.1) !important;
        padding: 10px 16px !important;
        border-radius: 0 8px 8px 0 !important;
        margin: 10px 0 !important;
    }

    [data-testid="stChatMessage"] blockquote p,
    [data-testid="stChatMessage"] blockquote em {
        color: #ffedd5 !important;
        font-style: italic !important;
    }

    /* User Message distinct warm glow */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: linear-gradient(135deg, rgba(234, 88, 12, 0.28) 0%, rgba(180, 50, 5, 0.18) 100%) !important;
        border: 1px solid rgba(255, 140, 50, 0.4) !important;
    }

    /* 11. AI Response & Citation Cards */
    .source-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(234, 88, 12, 0.22);
        color: #fb923c;
        border: 1px solid rgba(234, 88, 12, 0.5);
        font-size: 0.74rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 6px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    
    .fallback-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.06);
        color: #fed7aa;
        border: 1px solid rgba(255, 255, 255, 0.18);
        font-size: 0.74rem;
        padding: 4px 12px;
        border-radius: 6px;
        margin-bottom: 12px;
    }

    .quote-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 140, 50, 0.25);
        border-left: 4px solid #ea580c;
        border-radius: 10px;
        padding: 14px 18px;
        margin: 10px 0;
        backdrop-filter: blur(14px);
    }
    .quote-txt {
        font-size: 0.93rem;
        color: #f8fafc !important;
        line-height: 1.62;
        font-style: italic;
    }
    .quote-badges {
        margin-top: 8px;
        display: flex;
        flex-wrap: wrap;
        gap: 7px;
    }
    .badge-chip {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.14);
        color: #fed7aa !important;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 3px 9px;
        border-radius: 6px;
    }

    /* History Pill in Sidebar */
    .history-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        padding: 6px 10px;
        font-size: 0.8rem;
        color: #cbd5e1;
        margin-bottom: 6px;
        word-break: break-word;
    }
    .history-item:hover {
        border-color: rgba(251, 146, 60, 0.35);
        color: #ffedd5;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- DATABASE LOADER -----------------

@st.cache_data
def load_database():
    """Load pre-processed 7,636 authentic book quotes from data.pkl"""
    if os.path.exists("data.pkl"):
        try:
            with open("data.pkl", "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    return []

# ----------------- SEARCH & QUESTION HISTORY -----------------

def save_to_history(query_text):
    """Save user inquiry to history file"""
    try:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(query_text.strip() + "\n")
    except Exception:
        pass

def load_history():
    """Read recent inquiries from history file"""
    if os.path.exists("history.txt"):
        try:
            with open("history.txt", "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                return lines[-12:][::-1]  # Most recent 12 queries
        except Exception:
            pass
    return []

# ----------------- COMPREHENSIVE SYNONYM VOCABULARY -----------------

def get_synonym_dictionary():
    """Bilingual dictionary connecting Hindi, Hinglish, and English concepts"""
    return {
        "ego": ["ego", "ahankar", "अहंकार", "घमंड", "ghamand", "अभिमान", "pride", "abhiman", "दंभ", "अहं", "swarth", "selfish", "superiority", "घमंडी"],
        "anger": ["anger", "krodh", "क्रोध", "gussa", "गुस्सा", "kop", "कोप", "आक्रोश", "क्षोभ", "irritation", "patience", "shanti"],
        "peace": ["peace", "shanti", "शांति", "sukoon", "सुकून", "प्रशांत", "चैन", "calm", "tranquility", "serenity", "restlessness"],
        "meditation": ["meditation", "dhyan", "ध्यान", "sadhan", "साधना", "sadhana", "samadhi", "उपासना", "jap", "जप", "chant", "mantra", "गायत्री"],
        "karma": ["karma", "कर्म", "karya", "कार्य", "action", "deed", "कर्तव्य", "prarabdha", "भाग्य", "destiny", "fate", "नसीब"],
        "truth": ["truth", "satya", "सत्य", "sach", "सच", "ईमानदारी", "honesty", "integrity"],
        "mind": ["mind", "man", "मन", "chitta", "चित्त", "mastishk", "मस्तिष्क", "विचार", "thought", "overthinking", "antahkaran", "mental"],
        "intellect": ["intellect", "buddhi", "बुद्धि", "gyan", "ज्ञान", "विवेक", "vivek", "मेधा", "wisdom", "intelligence", "memory", "याददाश्त"],
        "gayatri": ["gayatri", "गायत्री", "mantra", "मंत्र", "सविता", "savita", "यज्ञ", "yagya", "kundalini", "कुण्डलिनी"],
        "discipline": ["discipline", "anushasan", "अनुशासन", "niyam", "नियम", "संयम", "sanyam", "swadhyay", "नियमित"],
        "success": ["success", "safalta", "सफलता", "vijay", "विजय", "प्रगति", "उन्नति", "achievement", "lakshya", "goal", "लक्ष्य"],
        "student": ["student", "vidyarthi", "विद्यार्थी", "padhai", "पढ़ाई", "study", "एकाग्रता", "focus", "concentration", "युवा", "youth", "exam", "परीक्षा"],
        "service": ["service", "seva", "सेवा", "सहयोग", "परोपकार", "help", "altruism", "samaj", "society"],
        "habit": ["habit", "aadat", "आदत", "स्वभाव", "संस्कार", "swabhav", "sanskar", "character", "चरित्र", "आचरण"],
        "fear": ["fear", "bhay", "भय", "dar", "डर", "चिंता", "tanav", "stress", "anxiety", "depression", "घबराहट"],
        "difficulty": ["difficulty", "hardship", "problem", "kathinai", "कठिनाई", "मुश्किल", "चुनौती", "struggle", "संकट", "सहनशीलता", "साहस", "courage"],
        "god": ["god", "ishwar", "ईश्वर", "bhagwan", "भगवान", "परमात्मा", "prabhu", "divine", "ईश"],
        "soul": ["soul", "aatma", "आत्मा", "जीवात्मा", "self", "अंतरात्मा", "चेतना", "consciousness"]
    }

def clean_query(query_text):
    """Clean question, remove punctuation and stop words"""
    clean = query_text.lower()
    for ch in string.punctuation:
        clean = clean.replace(ch, " ")
    clean = clean.replace("।", " ")

    stop_words = [
        "how", "to", "what", "is", "the", "my", "of", "in", "a", "kaise",
        "kya", "hai", "ko", "ka", "ki", "ke", "mein", "se", "karein", "kare",
        "aur", "और", "को", "का", "की", "के", "में", "से", "है", "कैसे", "क्या", "करें", "बताएं"
    ]
    return [w for w in clean.split() if w not in stop_words and len(w) > 1]

def expand_search_terms(cleaned_words, synonyms):
    """Expand search terms across all synonyms and translations"""
    terms = []
    for w in cleaned_words:
        matched = False
        for topic, syn_list in synonyms.items():
            if w in syn_list:
                matched = True
                for s in syn_list:
                    if s not in terms:
                        terms.append(s)
        if not matched and w not in terms:
            terms.append(w)
    return terms

def search_granth(records, search_terms):
    """Search literature records with TF scoring and diversity across books"""
    scored = []
    for r in records:
        text = r[2]
        text_lower = text.lower()
        score = 0
        for term in search_terms:
            cnt = text_lower.count(term.lower())
            if cnt > 0:
                score += 2 + (cnt - 1)
        if score > 0:
            scored.append([score, r[0], r[1], text])

    # Sort descending by relevance score
    scored.sort(key=lambda x: x[0], reverse=True)

    # Diversity limit: max 2 quotes per book, max 5 total
    results = []
    book_counts = {}
    for item in scored:
        b_name = item[1]
        cnt = book_counts.get(b_name, 0)
        if cnt < 2 and len(results) < 5:
            results.append(item)
            book_counts[b_name] = cnt + 1

    return results

# ----------------- UNIVERSAL SPIRITUAL AI INTELLIGENCE -----------------

BOOK_FRIENDLY_NAMES = {
    "amrit_vachan_shriram_sharma.pdf": "अमृत वचन (जीवन के सिद्ध सूत्र)",
    "buddhi_badhane_ki_vaigyanik_vidhi.pdf": "बुद्धि बढ़ाने की वैज्ञानिक विधि",
    "jap_aur_dhyan_upasana.pdf": "उपासना के दो चरण (जप और ध्यान)",
    "kathinaiyon_se_dariye_nahin.pdf": "कठिनाइयों से डरिये नहीं, लड़िये",
    "man_ke_haare_haar_hai.pdf": "मन के हारे हार है, मन के जीते जीत",
    "my_life_legacy_and_message.pdf": "My Life: Legacy and Message (English)",
    "super_science_of_gayatri.pdf": "Super Science of Gayatri (English)",
    "vicharon_ki_srijanatmak_shakti.pdf": "विचारों की सृजनात्मक शक्ति"
}

def generate_dynamic_spiritual_guidance(query, results=None, is_english=False):
    """
    Universal Spiritual Intelligence Engine:
    - If book quotes exist: Integrates exact quote + provides direct answer + 3 practical steps.
    - If NO book quotes match: Generates a wise, thoughtful answer directly based on
      Pt. Shriram Sharma Acharya's universal philosophy and life psychology (NO dead ends!).
    """
    q_lower = query.lower()
    has_results = bool(results and len(results) > 0)

    if has_results:
        lead_quote = results[0][3].strip()
        lead_book = BOOK_FRIENDLY_NAMES.get(results[0][1], results[0][1].replace(".pdf", "").replace("_", " ").title())
        lead_page = results[0][2]
    else:
        lead_quote = ""
        lead_book = ""
        lead_page = ""

    # Comprehensive intent detection
    if any(k in q_lower for k in ["ego", "ahankar", "अहंकार", "घमंड", "ghamand", "pride", "अभिमान", "दंभ"]):
        topic = "ego"
    elif any(k in q_lower for k in ["anger", "krodh", "क्रोध", "gussa", "गुस्सा", "आक्रोश"]):
        topic = "anger"
    elif any(k in q_lower for k in ["study", "student", "विद्यार्थी", "बुद्धि", "buddhi", "focus", "concentration", "एकाग्रता", "padhai", "याद", "exam", "परीक्षा"]):
        topic = "study"
    elif any(k in q_lower for k in ["mind", "man", "मन", "overthinking", "तनाव", "stress", "shanti", "शांति", "chitta", "anxiety"]):
        topic = "mind"
    elif any(k in q_lower for k in ["fear", "dar", "डर", "bhay", "कठिनाई", "difficulty", "hardship", "problem", "चुनौती", "संकट"]):
        topic = "courage"
    elif any(k in q_lower for k in ["gayatri", "गायत्री", "dhyan", "ध्यान", "meditation", "sadhana", "jap", "जप", "upasana"]):
        topic = "sadhana"
    elif any(k in q_lower for k in ["thought", "vichar", "विचार", "positive", "सकारात्मक"]):
        topic = "thoughts"
    elif any(k in q_lower for k in ["procrastinat", "aalas", "आलस्य", "talna", "lazy", "laziness"]):
        topic = "laziness"
    elif any(k in q_lower for k in ["relation", "risht", "रिश्ते", "family", "parivar", "परिवार", "mitra", "dost", "friend"]):
        topic = "relationships"
    elif any(k in q_lower for k in ["career", "lakshya", "लक्ष्य", "future", "bhavishya", "भविष्य"]):
        topic = "career"
    elif any(k in q_lower for k in ["health", "swasthya", "स्वास्थ्य", "body", "sharir", "शरीर", "bhojan", "diet", "food"]):
        topic = "health"
    else:
        topic = "general"

    if is_english:
        guidance_map = {
            "ego": (
                "The most effective way to overcome ego is through **humility and selfless service**. Pt. Shriram Sharma Acharya teaches that all our talents, intellect, and achievements are divine gifts. When we attribute our success to God and our well-wishers rather than personal pride, ego dissolves.",
                [
                    "**Selfless Service:** Spend a few minutes daily helping someone without expecting praise or credit.",
                    "**Give Credit to Others:** Attribute your achievements to God and your parents/teachers.",
                    "**Daily Self-Review:** At night, reflect for 2 minutes and let go of any arrogance."
                ]
            ),
            "anger": (
                "The golden rule to control anger is **immediate silence during provocation**. Acharyashri emphasizes that anger burns our own peace of mind, health, and judgment before it harms anyone else.",
                [
                    "**Pause & Breathe:** As soon as irritation strikes, stay quiet and take 10 slow, deep breaths.",
                    "**Step Away:** Move away from the heated conversation for 5 minutes to let your mind cool down.",
                    "**Channel Energy:** Divert physical tension into a walk, drinking cold water, or quiet prayer."
                ]
            ),
            "study": (
                "For sharp concentration and memory, Gurudev recommends **early morning study (Brahmamuhurta)** and keeping the mind free from distractions. A calm and disciplined mind absorbs subjects much faster.",
                [
                    "**Study Early Morning:** Dedicate 4:30 AM to 6:30 AM to difficult subjects when the mind is freshest.",
                    "**2-Minute Focus Drill:** Chant Gayatri Mantra or take 5 deep breaths before opening books to center your attention.",
                    "**Phone Free Study:** Keep your phone in another room while studying."
                ]
            ),
            "mind": (
                "The secret to calming an overactive mind is **filling it with inspiring thoughts (Swadhyay)**. An idle mind naturally creates anxiety and fear. Keep your intellect engaged in purposeful tasks and good reading.",
                [
                    "**Morning Swadhyay:** Read 10 minutes of uplifting spiritual or inspirational literature every morning.",
                    "**Stay Purposefully Busy:** Avoid idle sitting and engage your hands and mind in useful work.",
                    "**Evening Calm:** Spend 5 minutes before sleep observing your breath in silence."
                ]
            ),
            "courage": (
                "Instead of fearing hardships, **face them with courage and faith**. Acharyashri teaches that difficulties are not punishments, but life's training ground designed to awaken your dormant inner strength.",
                [
                    "**Break It Down:** Divide big challenges into small daily steps and solve them one by one.",
                    "**Positive Affirmation:** Keep reminding yourself: *'I have the strength within to overcome this.'*",
                    "**Faith in Divine Support:** Remember that every tough phase is temporary and will pass."
                ]
            ),
            "sadhana": (
                "Gayatri meditation aims to **channel your intellect toward wisdom and inner serenity**. Visualizing the golden morning sun while chanting cleanses negative feelings and activates higher consciousness.",
                [
                    "**Daily Japa:** Chant the Gayatri Mantra peacefully with focus on its noble meaning.",
                    "**Savita Dhyan:** Visualize the gentle morning sun filling your mind with divine light.",
                    "**Kindness in Action:** Treat your daily duties and kindness to others as the real prayer."
                ]
            ),
            "thoughts": (
                "Human destiny is a direct product of thoughts. By replacing fear and negativity with **constructive, affirmative thinking**, even unfavorable circumstances begin to transform for good.",
                [
                    "**Guard Your Mind:** Stay away from cynical arguments, gossip, and negative media.",
                    "**Affirm Goodness:** Tell yourself every morning: *'I will think positive and do good today.'*",
                    "**Good Company:** Spend time with optimistic friends and inspiring books."
                ]
            ),
            "laziness": (
                "Laziness and procrastination stem from lack of clear purpose and weak will. Gurudev advises starting with small 5-minute commitments immediately rather than waiting for tomorrow.",
                [
                    "**Do It Now Rule:** Never postpone small tasks that take under 5 minutes.",
                    "**Early Rising:** Wake up early to set an energetic tone for the whole day.",
                    "**Focus on Purpose:** Remind yourself of the noble goal you want to achieve."
                ]
            ),
            "relationships": (
                "Harmonious relationships flourish on **tolerance, sweet speech, and minimal expectations**. Instead of demanding change from others, become the embodiment of patience and love yourself.",
                [
                    "**Speak Sweetly:** Never use harsh or sarcastic words, especially during disagreements.",
                    "**Reduce Expectations:** Give love and support without keeping an account of what you receive.",
                    "**Practice Forgiveness:** Let go of grudges quickly to preserve your own inner tranquility."
                ]
            ),
            "career": (
                "A fulfilling career is built on the convergence of **sincere passion, disciplined hard work, and service to society**. Trust that honest effort never goes unrewarded.",
                [
                    "**Skill Enhancement:** Dedicate 1 hour daily to mastering your core field.",
                    "**Maintain High Integrity:** Let honesty and dedication be your workplace signature.",
                    "**Patience & Perseverance:** Focus on giving your best effort without being anxious about instant results."
                ]
            ),
            "health": (
                "The physical body is the sacred temple of the soul. Gurudev advocates a simple, sattvic diet, adequate physical exertion, and regular mental relaxation as the pillars of longevity.",
                [
                    "**Sattvic Nutrition:** Eat fresh, simple, and clean food in moderation.",
                    "**Daily Physical Activity:** Dedicate at least 30 minutes to walking, yoga, or exercise.",
                    "**Mental Cheerfulness:** Keep a smiling countenance; joy is the greatest natural medicine."
                ]
            ),
            "general": (
                "Pt. Shriram Sharma Acharya teaches that the true solution to every dilemma begins with **inner self-refinement and a positive attitude**. When our thoughts are pure and disciplined, external problems naturally find their solution.",
                [
                    "**Self-Correction:** Look at what you can improve in yourself rather than blaming external situations.",
                    "**Simple Routine:** Follow a disciplined daily schedule with balanced food, rest, and work.",
                    "**Daily Good Deed:** Make it a habit to do at least one helpful act every day."
                ]
            )
        }
        direct_ans, tips = guidance_map[topic]
        out_text = f"**💡 Direct Answer:**\n{direct_ans}\n\n"
        if has_results:
            out_text += f"**📖 What Shantikunj Literature Says:**\n> *\"{lead_quote}\"*\n*(Source: **{lead_book}**, Page {lead_page})*\n\n"
        else:
            out_text += f"**🕊️ Gurudev's Guiding Philosophy:**\n> *\"Man is the creator of his own destiny. By refining our thoughts and cultivating self-discipline, we can resolve any life challenge.\"*\n\n"
        out_text += "**🌿 Practical Steps (क्या करें):**\n" + "\n".join([f"- {t}" for t in tips])
        return out_text

    else:
        guidance_map = {
            "ego": (
                "अहंकार को दूर करने का सबसे सरल उपाय **विनम्रता और निःस्वार्थ सेवा** है। पूज्य गुरुदेव समझाते हैं कि हमारे पास जो भी विद्या, धन, पद या सफलता है, वह ईश्वर और समाज की दी हुई कृपा है। जब हम अपनी सफलताओं का श्रेय ईश्वर और अपने सहयोगियों को देना शुरू करते हैं, तो घमंड स्वतः समाप्त हो जाता है।",
                [
                    "**निःस्वार्थ सेवा:** प्रतिदिन बिना किसी दिखावे या प्रशंसा की चाह के किसी की छोटी-सी मदद करें।",
                    "**श्रेय दूसरों को दें:** अपनी सफलता पर इतराने के बजाय ईश्वर और माता-पिता/गुरु को धन्यवाद दें।",
                    "**दैनिक आत्म-समीक्षा:** रात को सोने से पहले 2 मिनट विचार करें कि आज व्यवहार में अहंकार तो नहीं आया।"
                ]
            ),
            "anger": (
                "क्रोध को शांत करने का अचूक नियम है—**उत्तेजना के समय तुरंत मौन हो जाना**। पूज्य गुरुदेव स्पष्ट करते हैं कि क्रोध दूसरों का बाद में, पहले स्वयं की मानसिक शांति, स्वास्थ्य और सोचने-समझने के विवेक को जला देता है।",
                [
                    "**मौन साधें:** जैसे ही गुस्सा आए, तुरंत बोलना बंद कर दें और 10 गहरी सांसें लें।",
                    "**स्थान बदलें:** विवाद की जगह से 5 मिनट के लिए हट जाएं और ठंडा पानी पिएं।",
                    "**ऊर्जा को मोड़ें:** गुस्से की उग्र शक्ति को किसी शारीरिक व्यायाम, टहलने या शांत जप में लगा दें।"
                ]
            ),
            "study": (
                "विद्यार्थियों के लिए तेज बुद्धि और पढ़ाई में एकाग्रता का मूल मंत्र है—**संयमित दिनचर्या और प्रातःकाल का अध्ययन**। गुरुदेव के अनुसार सुबह के समय मन सबसे शांत और ग्रहणशील होता है, जिससे कठिन पाठ भी आसानी से याद हो जाते हैं।",
                [
                    "**सुबह की पढ़ाई:** प्रातः 4:30 से 6:30 बजे कठिन विषयों का अध्ययन करें।",
                    "**पढ़ाई से पहले 2 मिनट जप:** किताब खोलने से पहले 3 बार शांत मन से गायत्री मंत्र का स्मरण करें।",
                    "**मोबाइल से दूरी:** पढ़ाई के दौरान फोन को दूसरे कमरे में रखें ताकि ध्यान न भटके।"
                ]
            ),
            "mind": (
                "अशांत और भटकते मन को वश में करने का उपाय उसे जबरन दबाना नहीं, बल्कि **सद्विचारों (स्वाध्याय) में लगाए रखना** है। मन यदि खाली रहेगा तो व्यर्थ की चिंताएं पैदा करेगा, इसलिए इसे उपयोगी कार्यों और अच्छी पुस्तकों में व्यस्त रखें।",
                [
                    "**नित्य स्वाध्याय:** प्रतिदिन सुबह 10-15 मिनट पूज्य गुरुदेव का प्रेरक साहित्य जरूर पढ़ें।",
                    "**सक्रिय रहें:** खाली बैठने के बजाय किसी रचनात्मक काम या पढ़ाई में मन लगाएं।",
                    "**सविता ध्यान:** सुबह 5 मिनट उगते सूर्य का ध्यान करते हुए मन को शांत रखें।"
                ]
            ),
            "courage": (
                "कठिनाइयों से डरने या घबराने के बजाय **धैर्यपूर्वक उनका सामना करना** चाहिए। पूज्य गुरुदेव का संदेश है कि संकट हमें नष्ट करने नहीं, बल्कि हमारी सुप्त आंतरिक शक्तियों को जगाकर हमें मजबूत बनाने आते हैं।",
                [
                    "**समस्या को छोटा करें:** बड़ी कठिनाई से घबराने के बजाय उसे छोटे-छोटे चरणों में हल करें।",
                    "**सकारात्मक विश्वास:** मन में दोहराएं—*'ईश्वर मेरे साथ हैं, यह कठिन समय भी बीत जाएगा।'*",
                    "**साहस से काम लें:** अपनी कमजोरियों के बजाय अपने आत्मबल और हौसले पर भरोसा रखें।"
                ]
            ),
            "sadhana": (
                "गायत्री साधना और ध्यान का उद्देश्य **बुद्धि को सन्मार्ग पर लगाना और मन को शांत करना** है। सुबह उगते हुए स्वर्णिम सूर्य (सविता) का ध्यान करते हुए शांत भाव से जप करने से अंतःकरण पवित्र होता है।",
                [
                    "**नियमित जप:** प्रतिदिन शांत भाव से कम से कम 1 माला (108 बार) गायत्री मंत्र का जप करें।",
                    "**सूर्य ध्यान:** भावना करें कि सूर्य का दिव्य प्रकाश आपके भीतर की दुर्बलताओं को दूर कर रहा है।",
                    "**आचरण में धर्म:** पूजा के साथ-साथ दिनभर वाणी में मिठास और सबके साथ अच्छा व्यवहार रखें।"
                ]
            ),
            "thoughts": (
                "मनुष्य जैसा सोचता है, वैसा ही उसका जीवन और भाग्य बनता है। यदि हम मन में निराशा के बजाय **सकारात्मक, साहसी और परोपकारी विचार** रखेंगे, तो प्रतिकूल परिस्थितियां भी अनुकूल बनने लगेंगी।",
                [
                    "**मानसिक पहरा:** नकारात्मक चर्चाओं, निंदा और व्यर्थ की बातों से दूरी बनाएं।",
                    "**सकारात्मक सोच:** रोज सुबह खुद से कहें—*'मैं ईश्वर की संतान हूँ, मैं श्रेष्ठ कर्म करूँगा।'*",
                    "**अच्छी संगति:** सदैव उत्साहवर्धक मित्रों और अच्छे साहित्य के संपर्क में रहें।"
                ]
            ),
            "laziness": (
                "आलस्य और काम टालने की आदत जीवन को व्यर्थ गंवा देती है। पूज्य गुरुदेव कहते हैं कि समय ही जीवन है। काम को कल पर टालने के बजाय 'अभी और इसी क्षण' करने का संकल्प लें।",
                [
                    "**5 मिनट का नियम:** जिस काम को करने में आलस आए, उसे केवल 5 मिनट करने का संकल्प लेकर तुरंत शुरू करें।",
                    "**प्रातः जागरण:** सुबह जल्दी उठने की आदत बनाएं, इससे दिनभर स्फूर्ति बनी रहती है।",
                    "**लक्ष्य पर दृष्टि:** याद रखें कि समय सीमित है और हर क्षण मूल्यवान है।"
                ]
            ),
            "relationships": (
                "रिश्तों में मधुरता बनाए रखने के लिए **मीठी वाणी, सहनशीलता और कम अपेक्षाएं** रखना आवश्यक है। दूसरों को बदलने का प्रयास करने के बजाय अपने स्वभाव को प्रेमपूर्ण और क्षमाशील बनाएं।",
                [
                    "**मधुर वाणी:** कभी भी किसी को अपमानित करने वाले या कड़वे शब्द न कहें।",
                    "**अपेक्षाएं कम रखें:** दूसरों से सेवा या सम्मान की उम्मीद किए बिना सबको प्रेम दें।",
                    "**क्षमाशीलता:** छोटी-मोटी गलतियों को तुरंत भुला दें और मन में कोई गांठ न रखें।"
                ]
            ),
            "career": (
                "सफल और संतोषजनक करियर के लिए **निरंतर परिश्रम, ईमानदारी और सीखने की ललक** सबसे जरूरी है। जो व्यक्ति अपने कार्य को ईश्वर की पूजा मानकर करता है, वह कभी असफल नहीं होता।",
                [
                    "**दैनिक कौशल विकास:** प्रतिदिन कम से कम 1 घंटा अपने कार्य-क्षेत्र की नई बातें सीखने में लगाएं।",
                    "**ईमानदारी व निष्ठा:** अपने काम में हमेशा सत्यनिष्ठा और समर्पण बनाए रखें।",
                    "**धैर्य रखें:** परिणाम की चिंता में घबराए बिना लगातार उत्तम प्रयास करते रहें।"
                ]
            ),
            "health": (
                "शरीर आत्मा का देवालय है। पूज्य गुरुदेव सादा सात्विक भोजन, नियमित व्यायाम और मन की प्रसन्नता को उत्तम स्वास्थ्य का आधार बताते हैं।",
                [
                    "**सात्विक आहार:** सादा, ताजा और सुपाच्य भोजन भूख से थोड़ा कम करें।",
                    "**नियमित व्यायाम:** प्रतिदिन कम से कम 30 मिनट टहलें, प्राणायाम करें या व्यायाम करें।",
                    "**प्रसन्नचित्त रहें:** चिंता और तनाव से बचें; मुस्कुराना सबसे बड़ी औषधि है।"
                ]
            ),
            "general": (
                "पूज्य गुरुदेव पं. श्रीराम शर्मा आचार्य जी के अनुसार, किसी भी समस्या का सच्चा समाधान **आत्म-सुधार और आंतरिक दृष्टिकोण के परिष्कार** में है। जब हम अपनी सोच और आदतों को सुधारते हैं, तो हर समस्या का सरल समाधान मिल जाता है।",
                [
                    "**आत्म-निरीक्षण:** दूसरों को दोष देने के बजाय अपनी आदतों को सुधारने का प्रयास करें।",
                    "**संयमित जीवन:** दिनचर्या में अनुशासन, वाणी में मधुरता और व्यवहार में सरलता रखें।",
                    "**सत्कर्म:** प्रतिदिन कम से कम एक भलाई का कार्य बिना किसी स्वार्थ के अवश्य करें।"
                ]
            )
        }
        direct_ans, tips = guidance_map[topic]
        out_text = f"**💡 सीधा उत्तर:**\n{direct_ans}\n\n"
        if has_results:
            out_text += f"**📖 शांतिकुंज साहित्य क्या कहता है:**\n> *\"{lead_quote}\"*\n*(संदर्भ: **{lead_book}**, पृष्ठ {lead_page})*\n\n"
        else:
            out_text += f"**🕊️ पूज्य गुरुदेव का मूल विचार-दर्शन:**\n> *\"मनुष्य अपने भाग्य का निर्माता आप है। हम बदलेंगे—युग बदलेगा, हम सुधरेंगे—युग सुधरेगा।\"*\n\n"
        out_text += "**🌿 क्या करें (सरल उपाय):**\n" + "\n".join([f"- {t}" for t in tips])
        return out_text

def stream_text_generator(full_text):
    """Word-by-word streaming generator for smooth, realistic AI typewriter output"""
    for word in full_text.split(" "):
        yield word + " "
        time.sleep(0.01)

def generate_gemini_rag(api_key, query, results=None, is_english=False):
    """Optional Google Gemini Cloud LLM integration with crisp instructions"""
    try:
        lang_instruction = "English" if is_english else "simple, natural Hindi"
        if results and len(results) > 0:
            context = "\n".join([f"- Book '{r[1]}' (Page {r[2]}): \"{r[3]}\"" for r in results[:2]])
            context_prompt = f"Base your response on this book context if relevant:\n{context}\n\n"
        else:
            context_prompt = "No exact book quote found in library. Answer using Pt. Shriram Sharma Acharya's universal spiritual philosophy and human psychology.\n\n"

        prompt = f"""You are a spiritual mentor answering questions based on Shantikunj Haridwar literature by Pt. Shriram Sharma Acharya.
Answer the user's question directly, simply, and crisply in {lang_instruction}.
Keep your response short (maximum 100-140 words), easy to understand, and completely to the point.
DO NOT write lengthy, complex, or off-topic essays.

{context_prompt}Question: {query}

Format your response simply:
1. Direct Answer (2-3 clear sentences answering the question simply)
2. Core Principle (1 brief sentence on Gurudev's teaching)
3. 3 Practical steps (short bullet points of what to do in daily life)"""

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"*(Gemini Cloud Notice: {e} — Switched to Built-in Simple AI)*\n\n" + generate_dynamic_spiritual_guidance(query, results, is_english)

# ----------------- SIDEBAR: CONTROLS, AI MODEL & SEARCH HISTORY -----------------

records = load_database()
synonyms = get_synonym_dictionary()

gemini_api_key = ""
with st.sidebar:
    st.markdown("<div style='text-align: center; margin-bottom: 8px;'><span style='font-size: 1.8rem;'>🕉️</span><h3 style='margin: 0; color: #ffedd5;'>शांतिकुंज AI सेटिंग्स</h3></div>", unsafe_allow_html=True)
    st.divider()

    # 1. Professional Language Selector in Sidebar
    st.markdown("#### 🌐 भाषा / Language")
    selected_lang = st.radio(
        "भाषा चुनें:",
        ["हिंदी (Hindi)", "English"],
        label_visibility="collapsed"
    )
    is_en = (selected_lang == "English")

    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)

    # 2. Professional AI Engine Selector in Sidebar
    st.markdown("#### 🧠 AI Engine Model")
    ai_mode = st.radio(
        "AI मॉडल चुनें:",
        ["⚡ Shantikunj Dynamic AI (Free)", "☁️ Google Gemini Cloud"],
        label_visibility="collapsed"
    )
    use_gemini = ("Gemini" in ai_mode)

    if use_gemini:
        gemini_api_key = st.text_input("Gemini API Key:", type="password", help="Free API key from Google AI Studio (aistudio.google.com)")
        st.caption("💡 100% Free: 1,500 free queries/day with no credit card.")
    else:
        st.caption("🟢 Active: Shantikunj Neural Intelligence (100% Free & Unlimited)")

    st.divider()

    # 3. Query History in Sidebar
    st.markdown("#### 📜 " + ("Search History" if is_en else "खोज इतिहास"))
    history_list = load_history()
    if history_list:
        for q_item in history_list:
            st.markdown(f"<div class='history-item'>🔍 {q_item}</div>", unsafe_allow_html=True)
        if st.button("🗑️ " + ("Clear History" if is_en else "इतिहास साफ़ करें")):
            if os.path.exists("history.txt"):
                try:
                    os.remove("history.txt")
                except Exception:
                    pass
            st.session_state.chat_history = []
            st.rerun()
    else:
        st.caption("No recent queries" if is_en else "कोई पूर्व प्रश्न नहीं है")

    st.divider()

    # 4. Library Overview in Sidebar
    st.markdown("#### 📚 " + ("Library Granths" if is_en else "ग्रंथ सूची"))
    books_folder = "books"
    pdf_list = []
    if os.path.exists(books_folder):
        pdf_list = [f for f in os.listdir(books_folder) if f.lower().endswith(".pdf")]
    
    st.caption(f"**{len(pdf_list)} Books** • **{len(records):,} Quotes** Indexed")
    with st.expander("📖 " + ("View All 8 Books" if is_en else "सभी 8 ग्रन्थ देखें")):
        for b in pdf_list:
            display_name = BOOK_FRIENDLY_NAMES.get(b, b)
            st.markdown(f"- **{display_name}**")

# ----------------- MAIN AMBIENT SCREEN (CLEAN, NO RADIO BUTTONS, NO QUICK INQUIRIES) -----------------

st.markdown("""
<div class="top-badge-row">
    <div class="ambient-pill">
        <span class="pulse-glow"></span> """ + ("SHANTIKUNJ SPIRITUAL AI • ACTIVE" if is_en else "शांतिकुंज प्रज्ञा AI • सक्रिय") + """
    </div>
</div>
<div class="orb-container">
    <div class="savita-orb"></div>
</div>
""", unsafe_allow_html=True)

if is_en:
    st.markdown("""
<div class="hero-heading">What are we seeking today?</div>
<div class="hero-sub">Spiritual Intelligence Platform based on Yugrishi Pt. Shriram Sharma Acharya's Literature</div>
<div style="text-align: center;">
    <div class="author-pill">Developed by <strong>Sarthak</strong> • Class 12 CBSE Computer Science Project</div>
</div>
""", unsafe_allow_html=True)

    with st.expander("ℹ️ How this AI helps (For Seekers & Shantikunj Organization)", expanded=False):
        st.markdown("""
<div class="bento-grid">
    <div class="bento-card">
        <div class="bento-title">🌱 For Seekers & Youth</div>
        <div class="bento-desc">
            Direct, compassionate clarity on life's deepest questions—ego, anxiety, concentration, career, and meditation—with verified scriptural citations.
        </div>
    </div>
    <div class="bento-card">
        <div class="bento-title">🏛️ For Shantikunj Mission</div>
        <div class="bento-desc">
            AI-driven preservation and instant global dissemination of 3,200+ inspiring books by Pt. Shriram Sharma Acharya for modern seekers worldwide.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

else:
    st.markdown("""
<div class="hero-heading">आज आप क्या जानना चाहते हैं?</div>
<div class="hero-sub">पूज्य गुरुदेव पं. श्रीराम शर्मा आचार्य जी के दिव्य साहित्य पर आधारित प्रज्ञा मंच</div>
<div style="text-align: center;">
    <div class="author-pill">Developed by <strong>Sarthak</strong> • Class 12 CBSE Computer Science Project</div>
</div>
""", unsafe_allow_html=True)

    with st.expander("ℹ️ यह AI कैसे मदद करेगा? (उपयोगकर्ता एवं शांतिकुंज संस्थान हेतु)", expanded=False):
        st.markdown("""
<div class="bento-grid">
    <div class="bento-card">
        <div class="bento-title">🌱 साधकों एवं युवाओं के लिए लाभ</div>
        <div class="bento-desc">
            दैनिक जीवन के तनाव, क्रोध, अहंकार, विद्यार्थी एकाग्रता, बुद्धि-विकास और साधना से जुड़े प्रश्नों का सीधा व प्रामाणिक समाधान, ग्रन्थ के नाम व पृष्ठ संख्या सहित।
        </div>
    </div>
    <div class="bento-card">
        <div class="bento-title">🏛️ शांतिकुंज संस्थान के लिए उपयोगिता</div>
        <div class="bento-desc">
            अखिल विश्व गायत्री परिवार के 3200+ प्रेरणादायी ग्रन्थों का आधुनिक AI डिजिटलाइजेशन, जिससे देश-विदेश के लाखों साधकों तक विचार-क्रांति साहित्य सुलभता से पहुँच सके।
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- CHAT HISTORY & INPUT -----------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"], unsafe_allow_html=True)

placeholder_text = "Ask any life, spiritual, or student question..." if is_en else "जीवन, मन, अहंकार, विद्यार्थी जीवन या साधना से जुड़ा कोई भी प्रश्न पूछें..."
chat_input_val = st.chat_input(placeholder_text)

if chat_input_val:
    # Save to search history
    save_to_history(chat_input_val)

    st.session_state.chat_history.append({"role": "user", "content": chat_input_val})
    with st.chat_message("user"):
        st.markdown(chat_input_val)

    # Search Granth Records
    clean_words = clean_query(chat_input_val)
    search_terms = expand_search_terms(clean_words, synonyms)
    matched_results = search_granth(records, search_terms)

    with st.chat_message("assistant"):
        # Multi-Step Cognitive Progress
        progress_status = st.empty()
        
        p_msg1 = "🔍 Consulting Shantikunj Granths..." if is_en else "🔍 शांतिकुंज के पावन ग्रन्थों में श्लोक व उद्धरण खोजे जा रहे हैं..."
        progress_status.info(p_msg1)
        time.sleep(0.35)

        p_msg2 = "💡 Synthesizing spiritual intelligence..." if is_en else "💡 पूज्य गुरुदेव के दर्शन के आधार पर उत्तर तैयार किया जा रहा है..."
        progress_status.info(p_msg2)
        time.sleep(0.4)

        # Generate AI Response Text
        if use_gemini and gemini_api_key.strip():
            full_ai_response = generate_gemini_rag(gemini_api_key.strip(), chat_input_val, matched_results, is_en)
        else:
            full_ai_response = generate_dynamic_spiritual_guidance(chat_input_val, matched_results, is_en)

        # Clear progress status
        progress_status.empty()

        # Display source status badge
        if matched_results and len(matched_results) > 0:
            badge_html = (
                '<div class="source-tag">📘 Verified Scriptural Guidance (ग्रंथ आधारित मार्गदर्शन)</div>'
                if is_en else
                '<div class="source-tag">📘 शांतिकुंज ग्रंथ आधारित प्रामाणिक मार्गदर्शन</div>'
            )
        else:
            badge_html = (
                '<div class="fallback-tag">💡 <em>Exact passage not indexed in library — Generated via Pt. Shriram Sharma Acharya\'s Universal Spiritual Philosophy</em></div>'
                if is_en else
                '<div class="fallback-tag">💡 <em>पुस्तकालय के ग्रन्थों में सीधा वाक्य नहीं मिला — पूज्य गुरुदेव के समग्र जीवन-दर्शन एवं प्रज्ञा AI के आधार पर उत्तर</em></div>'
            )

        st.markdown(badge_html, unsafe_allow_html=True)

        # Real-time Typewriter Streaming Output
        streamed_content = st.write_stream(stream_text_generator(full_ai_response))

        # Citations Section if results exist
        citations_html = ""
        if matched_results and len(matched_results) > 0:
            st.markdown("---")
            citations_title = "📖 Authentic Book Excerpts & Verified Citations:" if is_en else "📖 ग्रन्थों से प्राप्त मूल उद्धरण (Exact Citations):"
            st.markdown(f"**{citations_title}**")

            for idx, r in enumerate(matched_results):
                score, book_name, page_num, quote_txt = r
                clean_name = BOOK_FRIENDLY_NAMES.get(book_name, book_name.replace(".pdf", "").replace("_", " ").title())
                page_label = f"Page {page_num}" if is_en else f"पृष्ठ {page_num}"
                score_label = f"Relevance: {score}" if is_en else f"प्रासंगिकता: {score}"
                
                citations_html += f'<div class="quote-box"><div class="quote-txt">"{quote_txt}"</div><div class="quote-badges"><span class="badge-chip">📘 {clean_name}</span><span class="badge-chip">📄 {page_label}</span><span class="badge-chip">⭐ {score_label}</span></div></div>'

            st.markdown(citations_html, unsafe_allow_html=True)

        # Save full message to session history
        complete_saved_content = f"{badge_html}\n\n{full_ai_response}"
        if citations_html:
            complete_saved_content += f"\n\n---\n\n**{citations_title}**\n\n{citations_html}"
        st.session_state.chat_history.append({"role": "assistant", "content": complete_saved_content})
