"""
Project Chronos: The AI Archeologist
------------------------------------
This script accepts a fragmented piece of text, uses Google Gemini to reconstruct
its full meaning, performs an automated (mock) web search for context, and
generates a formatted Reconstruction Report.

Requirements:
    pip install google-generativeai python-dotenv requests
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv
import requests
import warnings; warnings.filterwarnings("ignore")


# Load environment variables (for Gemini API key)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Please create a .env file with GEMINI_API_KEY=your_key_here")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


# -----------------------------
# Step 1: Reconstruct Text
# -----------------------------
def reconstruct_text(fragment: str) -> str:
    """
    Sends the input fragment to the Gemini model and returns a reconstructed version.
    """
    model = genai.GenerativeModel("models/gemini-2.5-flash")



    prompt = f"""
    You are an AI historian reconstructing incomplete or slang-filled digital text.
    Given the fragment below, rewrite it as a complete, meaningful statement
    that reflects the cultural or digital context of its time.

    Fragment:
    "{fragment}"

    Output only the reconstructed text.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Error reconstructing text: {e}]"


# -----------------------------
# Step 2: Search for Context (Live Google Search)
# -----------------------------
def search_context(query: str):
    """
    Searches the web for contextual sources using Google Custom Search API.
    Requires GOOGLE_API_KEY and GOOGLE_CX_ID in .env file.
    """
    from dotenv import load_dotenv
    import os
    import requests

    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    cx_id = os.getenv("GOOGLE_CX_ID")
    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "key": api_key,
        "cx": cx_id,
        "q": query,
        "num": 5
    }

    print("\n🔍 Searching for context related to:", query)

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])

        if not items:
            return ["(No relevant sources found.)"]

        # Format results as "Title — Link"
        results = [f"{i+1}. {item['title']} — {item['link']}" for i, item in enumerate(items[:5])]
        return results

    except Exception as e:
        return [f"(Search error: {e})"]

# -----------------------------
# Step 3: Generate the Reconstruction Report
# -----------------------------
def generate_report(original: str, reconstructed: str, sources: list):
    """
    Prints a formatted Reconstruction Report.
    """
    print("\n" + "="*60)
    print("🧠  PROJECT CHRONOS: RECONSTRUCTION REPORT")
    print("="*60)
    print(f"\n[Original Fragment]\n> {original}")
    print(f"\n[AI-Reconstructed Text]\n> {reconstructed}\n")
    print("[Contextual Sources]")
    for link in sources:
        print(f"* {link}")
    print("\n" + "="*60 + "\n")


# -----------------------------
# Step 4: Main Execution
# -----------------------------
if __name__ == "__main__":
    print("=== Project Chronos: The AI Archeologist ===")
    fragment = input("Enter an old/fragmented digital text: ")

    reconstructed_text = reconstruct_text(fragment)
    context_links = search_context(reconstructed_text)
    generate_report(fragment, reconstructed_text, context_links)
