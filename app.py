## StudyBuddy AI - Friendly learning companion

import gradio as gr
import openai
import os
from typing import List, Tuple

# Initialize OpenAI client
def initialize_openai():
    """Initialize OpenAI client with API key"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Please set your OPENAI_API_KEY environment variable")
    return openai.OpenAI(api_key=api_key)

def generate_qa_pairs(topic: str, difficulty: str = "Medium") -> str:
    """
    Generate 10 questions and answers for a given topic using GPT-4 Mini
    
    Args:
        topic (str): The topic to generate Q&A pairs for
        difficulty (str): Difficulty level (Easy, Medium, Hard)
    
    Returns:
        str: Formatted Q&A pairs
    """
    try:
        client = initialize_openai()
        
        # Create the prompt
        prompt = f"""Generate exactly 10 questions and answers about the topic: "{topic}"
Requirements:
- Difficulty level: {difficulty}
- Questions should be diverse and cover different aspects of the topic
- Answers should be comprehensive but concise (2-4 sentences each)
- Format each Q&A pair clearly with "Q:" and "A:" labels
- Number each pair (1-10)
Topic: {topic}
Difficulty: {difficulty}
Please generate the questions and answers now:"""

        # Make API call to GPT-4 Mini
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Updated model name
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert educator who creates high-quality questions and answers on various topics. Your responses are well-structured, accurate, and educational."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except openai.AuthenticationError:
        return "❌ Authentication Error: Please check your OpenAI API key."
    except openai.RateLimitError:
        return "❌ Rate Limit Error: You've exceeded your API quota. Please try again later."
    except openai.APIError as e:
        return f"❌ OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def create_interface():
    """Create and configure the Gradio interface"""
    
    with gr.Blocks(
        title="StudyBuddy-AI - Q&A Generator with LLM",
        theme=gr.themes.Soft(),
        css="""
        .main-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .qa-output {
            font-family: 'Georgia', serif;
            line-height: 1.6;
        }
        """
    ) as interface:
        
        gr.HTML("""
        <div class="main-header">
            <h1>🤖 StudyBuddy-AI </h1>
            <p>Generate 10 comprehensive questions and answers on any topic using gpt-4-o mini</p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                topic_input = gr.Textbox(
                    label="Topic",
                    placeholder="Enter any topic (e.g., 'AWS', 'Machine Learning', 'Azure Web Apps')",
                    lines=2
                )
                
                difficulty_dropdown = gr.Dropdown(
                    label="Difficulty Level",
                    choices=["Easy", "Medium", "Hard"],
                    value="Medium"
                )
                
                generate_btn = gr.Button(
                    "Generate Q&A Pairs",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                gr.HTML("""
                <div style="padding: 1rem; background-color: #f0f8ff; border-radius: 8px; margin-top: 1rem;">
                    <h3>📝 Instructions:</h3>
                    <ol>
                        <li>Enter a topic you want to learn about</li>
                        <li>Choose difficulty level</li>
                        <li>Click "Generate Q&A Pairs"</li>
                    </ol>
                    <p><strong>Note:</strong> Make sure to set your <code>OPENAI_API_KEY</code> environment variable before running.</p>
                </div>
                """)
        
        qa_output = gr.Textbox(
            label="Generated Questions & Answers",
            lines=25,
            max_lines=50,
            elem_classes=["qa-output"],
            show_copy_button=True
        )
        
        # Example topics for quick testing
        gr.Examples(
            examples=[
                ["Artificial Intelligence", "Medium"],
                ["AWS", "Easy"],
                ["Azure", "Hard"],
                ["Renaissance Art", "Medium"],
                ["Cryptocurrency", "Medium"]
            ],
            inputs=[topic_input, difficulty_dropdown]
        )
        
        # Event handlers
        generate_btn.click(
            fn=generate_qa_pairs,
            inputs=[topic_input, difficulty_dropdown],
            outputs=qa_output
        )
        
        # Allow Enter key to trigger generation
        topic_input.submit(
            fn=generate_qa_pairs,
            inputs=[topic_input, difficulty_dropdown],
            outputs=qa_output
        )
    
    return interface

def main():
    """Main function to launch the application"""
    
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY environment variable not found!")
        print("Please set it using: export OPENAI_API_KEY='your-api-key-here'")
        print("You can get your API key from: https://platform.openai.com/api-keys")
    
    # Create and launch interface
    interface = create_interface()
    interface.launch(
        share=False,
        show_error=True
    )

if __name__ == "__main__":
    main()
