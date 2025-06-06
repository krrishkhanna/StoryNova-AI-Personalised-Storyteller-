﻿# AI Storyteller 📚✨

An interactive web application that generates creative stories using AI. Built with Streamlit and OpenAI's GPT models.

## Features 🌟

- Generate creative stories based on user prompts
- Multiple story genres (Adventure, Horror, Sci-Fi, Romance, Fairy Tale)
- Adjustable story lengths (Short, Medium, Long)
- Text-to-Speech narration
- Download stories as PDF or text files
- Beautiful, user-friendly interface
- Example prompts for inspiration

## Installation 🚀

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-storyteller
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage 🎮

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your story prompt or select from example prompts

4. Choose your preferred story type and length

5. Click "Generate Story" and watch the magic happen!

## Example Prompts 💡

- "A magical forest where trees whisper secrets"
- "A time-traveling detective solving cold cases"
- "A robot learning to paint like Van Gogh"
- "A love story between a mermaid and a lighthouse keeper"
- "A mystery in a small town where everyone has superpowers"

## Technologies Used 🛠

- Python
- Streamlit
- OpenAI GPT API
- pyttsx3 (Text-to-Speech)
- FPDF2 (PDF generation)
- Ollama (Model Generation(LLama 2))
  

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.
