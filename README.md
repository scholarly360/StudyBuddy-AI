# StudyBuddy-AI
Generate 10 comprehensive questions and answers on any topic using gpt-4-o mini (Gradio)


# Features:

Topic Input: Enter any topic you want to generate Q&A pairs for

Difficulty Levels: Choose between Easy, Medium, or Hard difficulty

Clean Interface: User-friendly design with instructions and examples

Error Handling: Proper handling of API errors and authentication issues

Copy Function: Easy copying of generated content

# Setup Requirements:

Install dependencies:
```
pip install gradio openai
```
Set your OpenAI API key:
```
export OPENAI_API_KEY='your-api-key-here'
```
Run the program:
```
python app.py
```

# How it works:

The program creates a structured prompt asking GPT-4 Mini to generate exactly 10 Q&A pairs
It includes system instructions to ensure high-quality, educational content
The response is formatted with numbered questions and comprehensive answers
Error handling covers authentication, rate limits, and other API issues

The interface will be available at http://localhost:7860 once you run the script. You can test it with topics like "Machine Learning", AWS S3" to see how it generates relevant questions and detailed answers


<img width="2203" height="1065" alt="image" src="https://github.com/user-attachments/assets/b8180b15-6a57-4129-8f28-02d9784e775f" />


<img width="2122" height="1190" alt="image" src="https://github.com/user-attachments/assets/f5f9d871-4197-4107-82d1-85cc79ff3189" />





