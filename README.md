# 💵 Currency Note Speaker App

A voice-enabled web application that detects Indian currency notes using a deep learning model and reads the result aloud. This app is especially helpful for visually impaired users.

---

## 🚀 Features

- 🔍 Detects Indian currency denominations from images
- 🧠 Uses a PyTorch-based custom CNN model
- 🔊 Speaks the result using browser speech synthesis or `pyttsx3`
- 🌐 Clean, accessible Gradio interface

---

## ⚙️ Setup Instructions (Windows)

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/amithhhh/fakeCurrency.git
cd fakeCurrency
2. 🛠️ Create a Virtual Environment
bash
Copy
Edit
python -m venv env
3. ▶️ Activate the Virtual Environment
Command Prompt:

bash
Copy
Edit
env\Scripts\activate
PowerShell:

bash
Copy
Edit
.\env\Scripts\Activate.ps1
4. 📥 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Make sure you're connected to the internet. All necessary packages including gradio, torch, pyttsx3, etc., will be installed.

🧠 Model Info
The app uses a lightweight custom CNN built in PyTorch. It's trained to identify the following Indian currency notes:

₹10

₹20

₹50

₹100

₹200

₹500

₹2000

The model is saved as models/currency(6).pth and automatically loaded when the app runs.

🔉 Text-to-Speech Feature
On local system: Uses pyttsx3 to speak the result out loud.

On web UI: Uses browser’s built-in SpeechSynthesisUtterance API.

Ensure sound is allowed in your browser for localhost.

💻 How to Run the App
Once setup is complete, run:

bash
Copy
Edit
python app.py
The app will start at:

text
Copy
Edit
http://127.0.0.1:7860
