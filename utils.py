import os
import pyttsx3
from openai import OpenAI
from fpdf import FPDF
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Initialize text-to-speech engine
engine = pyttsx3.init()

def generate_story(prompt, story_type, length):
    """
    Generate a story using OpenAI's GPT model.
    
    Args:
        prompt (str): User's story prompt
        story_type (str): Type of story (Adventure, Horror, etc.)
        length (str): Desired length (Short, Medium, Long)
    
    Returns:
        str: Generated story
    """
    # Map length to approximate word count
    length_map = {
        "Short": "100",
        "Medium": "300",
        "Long": "600"
    }
    
    # Construct the system message
    system_message = f"""You are a creative storyteller. Write a {story_type.lower()} story 
    that is approximately {length_map[length]} words long. The story should be engaging, 
    well-structured, and include vivid descriptions. Make it suitable for all ages unless 
    specifically requested otherwise."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating story: {str(e)}"

def speak_text(text):
    """
    Convert text to speech using pyttsx3.
    
    Args:
        text (str): Text to be spoken
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {str(e)}")

def save_as_pdf(story, filename="story.pdf"):
    """
    Save the story as a PDF file.
    
    Args:
        story (str): Story text
        filename (str): Output filename
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Split story into lines and add to PDF
        lines = story.split('\n')
        for line in lines:
            pdf.multi_cell(0, 10, txt=line)
        
        pdf.output(filename)
        return True
    except Exception as e:
        print(f"Error saving PDF: {str(e)}")
        return False

def save_as_text(story, filename="story.txt"):
    """
    Save the story as a text file.
    
    Args:
        story (str): Story text
        filename (str): Output filename
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(story)
        return True
    except Exception as e:
        print(f"Error saving text file: {str(e)}")
        return False 