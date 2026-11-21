Project Chronos

AI-Powered Digital Text Reconstruction

Project Chronos is a Python-based AI application designed to reconstruct fragmented, abbreviated, or outdated digital text into coherent modern language while providing relevant historical and cultural context.

The project combines Google Gemini’s generative AI capabilities with Google Custom Search to interpret incomplete text and retrieve supporting information.

Overview

Digital communication has evolved significantly over time, leaving behind abbreviations, slang, and fragmented expressions that can be difficult to interpret without context.

Project Chronos addresses this challenge by using generative AI to reconstruct digital text and web search to provide additional contextual information.

Key Features

AI-Powered Text Reconstruction

* Uses Google Gemini to interpret fragmented or abbreviated text.
* Reconstructs incomplete expressions into readable modern language.
* Preserves the intended meaning of the original input where possible.

Contextual Information Retrieval

* Integrates Google Custom Search API.
* Retrieves relevant online resources associated with the input text.
* Provides contextual references alongside AI-generated reconstructions.

Structured Reconstruction Reports

* Displays the original text fragment.
* Presents the AI-generated reconstruction.
* Lists relevant contextual source links.

Technologies Used

Technology	Purpose
Python 3.13	Core application development
Google Gemini API	AI-powered text reconstruction
Google Custom Search API	Contextual information retrieval
python-dotenv	Environment variable management

How It Works

1. The user enters a fragmented or outdated piece of digital text.
2. The application sends the input to Google Gemini for interpretation.
3. Gemini generates a reconstructed version in modern language.
4. Google Custom Search retrieves relevant contextual resources.
5. The application displays a structured reconstruction report.

Example

Input

smh at the top 8 drama. ppl need to chill. g2g ttyl

AI-Reconstructed Text

I am shaking my head in disappointment over the drama
in the top eight. People need to calm down.
I must go now, talk later.

Contextual Sources

Relevant resources explaining historical digital platforms, internet slang, and abbreviations are retrieved using Google Custom Search.

Installation

1. Clone the Repository

git clone https://github.com/Tanvi-0809/-project-chronos.git
cd -project-chronos/gemini_project

2. Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure API Keys

Create a .env file inside the gemini_project directory.

GEMINI_API_KEY=your_gemini_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX_ID=your_google_cx_id

5. Run the Application

python gemini.py

Project Structure

-project-chronos/
│
├── gemini_project/
│   ├── gemini.py
│   ├── list_models.py
│   ├── requirements.txt
│   └── README.md
│
├── README.md
├── env_example.txt
└── gitignore.txt

Applications

* Interpretation of historical internet slang
* Reconstruction of abbreviated digital communication
* Digital text analysis
* AI-assisted contextual research
* Exploration of evolving online communication patterns

Future Improvements

* Develop a web-based user interface.
* Support reconstruction across multiple languages.
* Improve contextual search relevance.
* Introduce confidence indicators for AI-generated interpretations.
* Expand support for historical digital communication formats.

Author

Tanvi Gajula

GitHub: Tanvi-0809

License

No license has been specified for this repository.
