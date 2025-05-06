import streamlit as st
import time
from utils import generate_story, speak_text, save_as_pdf, save_as_text

# Page configuration
st.set_page_config(
    page_title="AI Storyteller",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        font-size: 16px;
    }
    .story-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="title">📚 AI Storyteller</h1>', unsafe_allow_html=True)
st.markdown("""
    Welcome to AI Storyteller! Create unique, engaging stories with the power of AI.
    Choose your story type, length, and let your imagination run wild!
""")

# Sidebar for story settings
with st.sidebar:
    st.header("Story Settings")
    
    # Story type selection
    story_type = st.selectbox(
        "Choose Story Type",
        ["Adventure", "Horror", "Sci-Fi", "Romance", "Fairy Tale", "Mystery"]
    )
    
    # Story length selection
    story_length = st.selectbox(
        "Choose Story Length",
        ["Short", "Medium", "Long"]
    )
    
    # Example prompts
    st.header("Example Prompts")
    example_prompts = [
        "A magical forest where trees whisper secrets",
        "A time-traveling detective solving cold cases",
        "A robot learning to paint like Van Gogh",
        "A love story between a mermaid and a lighthouse keeper",
        "A mystery in a small town where everyone has superpowers"
    ]
    
    selected_prompt = st.selectbox("Try these examples:", example_prompts)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Story prompt input
    story_prompt = st.text_area(
        "Enter your story prompt",
        value=selected_prompt,
        height=100,
        placeholder="Once upon a time..."
    )

# Generate story button
if st.button("✨ Generate Story"):
    if not story_prompt.strip():
        st.error("Please enter a story prompt!")
    else:
        with st.spinner("Creating your story... This might take a moment..."):
            # Generate the story
            story = generate_story(story_prompt, story_type, story_length)
            
            # Display the story with animation
            st.markdown('<div class="story-container">', unsafe_allow_html=True)
            st.markdown("### Your Generated Story")
            st.write(story)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Story actions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🔊 Listen to Story"):
                    speak_text(story)
            
            with col2:
                if st.button("📥 Download as PDF"):
                    if save_as_pdf(story):
                        st.success("PDF saved successfully!")
                    else:
                        st.error("Error saving PDF")
            
            with col3:
                if st.button("📝 Download as Text"):
                    if save_as_text(story):
                        st.success("Text file saved successfully!")
                    else:
                        st.error("Error saving text file")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ using Streamlit and OpenAI</p>
    </div>
""", unsafe_allow_html=True) 