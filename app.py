import streamlit as st
import json
import os
from groq import Groq

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Message Analyzer",
    page_icon="🎯",
    layout="centered"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { max-width: 750px; }
    .stTextArea textarea { font-size: 15px; }
    .result-box {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e0e0e0;
    }
    .badge {
        display: inline-block;
        padding: 5px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        margin: 4px;
    }
    .badge-blue  { background: #dbeafe; color: #1e40af; }
    .badge-green { background: #dcfce7; color: #166534; }
    .badge-red   { background: #fee2e2; color: #991b1b; }
    .badge-gray  { background: #f3f4f6; color: #374151; }
    .reply-card {
        background: #ffffff;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 16px;
        margin-top: 12px;
        font-size: 15px;
        line-height: 1.7;
    }
    .section-label {
        font-size: 12px;
        font-weight: 600;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🎯 Customer Message Analyzer")
st.markdown("**AI-powered** classification · sentiment detection · auto-reply generation")
st.divider()

# ── API Key input ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("**Groq API Key** (Free at [console.groq.com](https://console.groq.com))")
    api_key = st.text_input("Enter your Groq API Key", type="password", placeholder="gsk_...")
    st.markdown("---")
    st.markdown("**Model:** `llama3-8b-8192`")
    st.markdown("**Categories:**")
    cats = ["Complaint","Refund/Return","Sales Inquiry",
            "Delivery Question","Account/Technical Issue","General Query","Spam"]
    for c in cats:
        st.markdown(f"• {c}")

# ── Sample messages ───────────────────────────────────────────────────────────
st.markdown("**💬 Try a sample message:**")
samples = {
    "😠 Angry Complaint": "I have been waiting 3 weeks for my order and no one is responding to my emails. This is completely unacceptable!",
    "💰 Sales Inquiry": "Hi, I wanted to ask about the pricing plans for your Pro subscription. Do you offer annual discounts?",
    "📦 Delivery Issue": "My package shows delivered but I never received it. Can you help me track it down?",
    "😊 Positive Feedback": "I just wanted to say your customer service team was amazing! Really happy with my purchase.",
    "🔧 Tech Issue": "I cannot log into my account. It keeps saying 'invalid credentials' even though I just reset my password.",
    "💸 Refund Request": "I would like to request a refund for order #45231. The product arrived damaged.",
    "🚫 Spam": "Buy cheap meds online!! Click here now!!! Limited time offer!!!",
}

cols = st.columns(3)
for i, (label, msg) in enumerate(samples.items()):
    if cols[i % 3].button(label, use_container_width=True):
        st.session_state["sample_msg"] = msg

# ── Text input ────────────────────────────────────────────────────────────────
default_val = st.session_state.get("sample_msg", "")
user_message = st.text_area(
    "✍️ Customer Message",
    value=default_val,
    height=130,
    placeholder="Paste or type a customer message here...",
)

analyze_clicked = st.button("🔍 Analyze Message", type="primary", use_container_width=True)

# ── Analysis ──────────────────────────────────────────────────────────────────
def analyze_message(message: str, key: str):
    client = Groq(api_key=key)

    prompt = f"""You are a customer support AI. Analyze the following customer message and respond with ONLY a valid JSON object (no markdown, no extra text) with these exact keys:
- "category": one of ["Complaint", "Refund/Return", "Sales Inquiry", "Delivery Question", "Account/Technical Issue", "General Query", "Spam"]
- "sentiment": one of ["Positive", "Neutral", "Negative"]
- "reply": a short professional auto-reply (2-4 sentences, friendly and helpful tone)

Customer message: "{message}"
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)


def sentiment_badge(sentiment):
    colors = {"Positive": "green", "Negative": "red", "Neutral": "gray"}
    icons  = {"Positive": "😊", "Negative": "😞", "Neutral": "😐"}
    c = colors.get(sentiment, "gray")
    i = icons.get(sentiment, "")
    return f'<span class="badge badge-{c}">{i} {sentiment}</span>'


if analyze_clicked:
    if not api_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar.")
    elif not user_message.strip():
        st.warning("⚠️ Please enter a customer message.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                result = analyze_message(user_message.strip(), api_key)

                st.success("✅ Analysis complete!")
                st.markdown("---")

                # Badges row
                st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)
                cat_badge  = f'<span class="badge badge-blue">🏷️ {result["category"]}</span>'
                sent_badge = sentiment_badge(result["sentiment"])
                st.markdown(f'{cat_badge} {sent_badge}', unsafe_allow_html=True)

                # Metrics
                col1, col2 = st.columns(2)
                col1.metric("Category", result["category"])
                col2.metric("Sentiment", result["sentiment"])

                # Auto-reply
                st.markdown("---")
                st.markdown('<div class="section-label">Suggested Auto-Reply</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="reply-card">{result["reply"]}</div>',
                    unsafe_allow_html=True
                )

                # Copy button
                st.code(result["reply"], language=None)

                # History
                if "history" not in st.session_state:
                    st.session_state["history"] = []
                st.session_state["history"].insert(0, {
                    "message": user_message[:80] + ("..." if len(user_message) > 80 else ""),
                    "category": result["category"],
                    "sentiment": result["sentiment"],
                })

            except json.JSONDecodeError:
                st.error("❌ Could not parse AI response. Please try again.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ── History ───────────────────────────────────────────────────────────────────
if st.session_state.get("history"):
    st.markdown("---")
    st.markdown("### 📋 Recent Analyses")
    for item in st.session_state["history"][:5]:
        sent_icon = {"Positive":"😊","Negative":"😞","Neutral":"😐"}.get(item["sentiment"],"")
        st.markdown(
            f"**{item['category']}** · {sent_icon} {item['sentiment']}"
            f"  \n_{item['message']}_"
        )
        st.markdown("")
