# AI Chatbot using LangChain, Google Gemini & Streamlit

An interactive AI-powered chatbot built using **LangChain**, **Google Gemini**, and **Streamlit**. This application allows users to communicate with Google's Gemini language model through a clean and user-friendly chat interface.

## Overview

This project demonstrates how to integrate a Large Language Model (LLM) with LangChain and build an interactive chatbot application using Streamlit.

Users can enter questions and receive AI-generated responses in real time. The application also maintains conversation history during the session.

## Key Features

- **AI-Powered Conversations:** Generate intelligent responses using Google Gemini.
- **LangChain Integration:** Connect and interact with the Gemini language model using LangChain.
- **Interactive Chat Interface:** Simple and user-friendly interface developed with Streamlit.
- **Conversation History:** Maintain previous messages during the active session.
- **Real-Time Responses:** Get responses dynamically from the AI model.
- **Clear Chat Option:** Reset the conversation and start a new session.
- **Secure API Configuration:** Manage API credentials using Streamlit Secrets.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration and message management |
| Google Gemini | Large Language Model |
| Streamlit | Web application interface |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
LangChain_Chatbot/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Application Workflow

1. User enters a question through the Streamlit chat interface.
2. The application receives the user's input.
3. LangChain manages the conversation messages.
4. The Google Gemini model processes the conversation.
5. The model generates an AI response.
6. Streamlit displays the response to the user.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/APavan123/LangChain_Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd LangChain_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Google Gemini API Key

Create a `.streamlit` folder and add a file named `secrets.toml`.

Add your API key:

```toml
GOOGLE_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"
```

**Security Note:** Never expose your API key in source code or commit your `secrets.toml` file to GitHub.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

The application can be deployed using **Streamlit Community Cloud**.

For deployment:
1. Push the project to GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select `app.py` as the main application file.
4. Configure `GOOGLE_API_KEY` in the application's Secrets settings.
5. Deploy the application.

## Future Enhancements

- Add persistent conversation history.
- Implement PDF-based question answering using RAG.
- Add support for multiple LLM models.
- Improve chatbot memory and context management.
- Add document upload functionality.

## Learning Outcomes

Through this project, I gained practical experience in:

- Working with Large Language Models.
- Integrating Google Gemini with LangChain.
- Building interactive applications using Streamlit.
- Managing API keys securely.
- Deploying AI applications.

## Author

**Pavan**

MCA Graduate | Aspiring AI/ML Engineer

Interested in Generative AI, Large Language Models, LangChain, and AI-powered applications.

---

⭐ If you find this project useful, feel free to explore the repository!
