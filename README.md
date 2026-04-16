#  Customer Message Analyzer

An AI-powered customer support tool that automatically **classifies** customer messages, detects their **sentiment**, and generates a professional **auto-reply** — all in seconds.

Built with **Streamlit** + **Groq API (LLaMA 3)** — completely free to use.

---

##  Features

-  **Message Classification** — Automatically categorizes messages into:
  - Complaint
  - Refund / Return
  - Sales Inquiry
  - Delivery Question
  - Account / Technical Issue
  - General Query
  - Spam

-  **Sentiment Detection** — Identifies if the message is Positive, Neutral, or Negative

-  **Auto-Reply Generation** — Generates a short, professional reply suited to the message

-  **Recent History** — Keeps track of the last 5 analyzed messages in your session

- ⚡ **Fast & Free** — Powered by Groq's free API (no credit card needed)

---

## 🖥️ Live Demo

👉 [Click here to open the app](https://customer-message-analyzer.streamlit.app/)

> Enter your free Groq API key in the sidebar and start analyzing messages instantly.

---

## 🚀 Run Locally (On Your Own Laptop)

### Prerequisites
- Python 3.8 or higher installed
- A free Groq API key (see below)

### Step 1 — Clone or Download this Repository

```bash
git clone https://github.com/your-username/customer-analyzer.git
cd customer-analyzer
```

Or simply download the ZIP and extract it.

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Get Your Free Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account (no credit card required)
3. Navigate to **API Keys** → click **Create API Key**
4. Copy the key — it starts with `gsk_...`

### Step 4 — Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Step 5 — Use the App

1. Paste your **Groq API key** in the left sidebar
2. Type or paste a customer message in the text box
   - Or click any of the **sample message buttons** to try it out
3. Click **🔍 Analyze Message**
4. View the results:
   - **Category** — what type of message it is
   - **Sentiment** — Positive / Neutral / Negative
   - **Auto-Reply** — a ready-to-send professional response

---

## 📁 Project Structure

```
customer-analyzer/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Groq API](https://console.groq.com) | Free AI inference |
| [LLaMA 3 (8B)](https://groq.com) | Language model |
| Python 3 | Backend logic |

---

## ⚠️ Important Note on API Key

Your Groq API key is entered **directly in the app sidebar** at runtime.  
It is **never stored** in the code or uploaded to GitHub.  
Each user uses their own free key — completely safe. 🔒

---

## 📄 License

This project is open source and free to use.
