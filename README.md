# 🎯 Customer Message Analyzer

AI-powered customer support tool — classifies messages, detects sentiment, and generates auto-replies.

## Features
- **Category Detection**: Complaint, Refund/Return, Sales Inquiry, Delivery Question, Account/Technical Issue, General Query, Spam
- **Sentiment Analysis**: Positive, Neutral, Negative
- **Auto-Reply Generation**: Professional, context-aware responses
- **Powered by**: Groq API (FREE) + LLaMA 3

---

## 🚀 Deploy on Streamlit Cloud (FREE — Get a shareable link!)

### Step 1: Get Free Groq API Key
1. Go to https://console.groq.com
2. Sign up (free)
3. Go to **API Keys** → Create new key
4. Copy the key (starts with `gsk_...`)

### Step 2: Upload to GitHub
1. Create a new GitHub repository (e.g. `customer-analyzer`)
2. Upload both files: `app.py` and `requirements.txt`

### Step 3: Deploy on Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click **New app**
4. Select your repo → branch: `main` → file: `app.py`
5. Click **Deploy**

✅ You'll get a live link like: `https://yourname-customer-analyzer.streamlit.app`

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

---

## Usage
1. Enter your Groq API key in the sidebar
2. Type or paste a customer message (or click a sample)
3. Click **Analyze Message**
4. See: Category + Sentiment badges + Auto-Reply
