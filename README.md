Hudabot

Hudabot is a simple voice assistant built with Python. It listens to your voice through the microphone, converts it into text, sends it to a language model (e.g., Cohere), and responds with a spoken reply.

Features

Converts voice to text using SpeechRecognition.
Sends the text to an AI model for a smart reply.
Converts the AI-generated response back to voice using pyttsx3.
Operates via the terminal in real time.
Project Structure

hudabot/
│
├── app.py (Main Python script)
├── requirements.txt (Required Python packages)
└── README.md (Project documentation)

AI Integration

This project uses a function such as get_response_from_cohere() to call a language model API. You can modify it to use Cohere, OpenAI, or any other NLP service.

Requirements

Python 3.8 or higher
SpeechRecognition
PyAudio
pyttsx3
(Optional) AI API key (e.g., Cohere)
