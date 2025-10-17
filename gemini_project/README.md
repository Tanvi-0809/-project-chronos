# Project Chronos: The AI Archeologist

**Team Members:**
- TANVI — SE24UCSE025
- NESHNA — SE24UCSE076
- OMKAR — SE24UCSE009  
- VARDHAN — SE23UECM042
- AMAAN — SE23UCSE002

This Python project reconstructs fragmented digital text using Google Gemini and provides cultural context via a Google Custom Search API.

---

## 🧠 What It Does
1. Accepts an old or cryptic piece of text (like early internet slang).
2. Uses **Google Gemini** to reconstruct it into a full modern version.
3. Searches the web using **Google Custom Search API** to find related pages or context.
4. Prints a **Reconstruction Report** with:
   - Original fragment  
   - AI-reconstructed version  
   - Contextual source links  

---

## ⚙️ Setup Instructions

1. **Create your `.env` file** inside this same folder (`gemini_project`) and add:
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CX_ID=your_google_cx_id_here

2. **Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4.Run the program:

python gemini.py

5.Example Output:

Enter an old/fragmented digital text: smh at the top 8 drama. ppl need to chill. g2g ttyl

[AI-Reconstructed Text]
I am shaking my head in disappointment over the drama in the top eight.
People need to calm down. I must go now, talk later.

[Contextual Sources]
1. https://www.dictionary.com/e/slang/smh/
2. https://en.wikipedia.org/wiki/Myspace

Folder Structure:
gemini_project/
├── gemini.py
├── list_models.py
├── requirements.txt
├── .env
├── .env.example
├── .venv/
└── README.md

 Technologies Used:
- Python 3.13  
- Google Gemini API (via `google-generativeai`)  
- Google Custom Search API  
- dotenv for environment management  