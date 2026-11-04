import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# --------------------------------
# 1. Page Configuration
# --------------------------------

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------
# 2. Chatbot Title
# --------------------------------

st.title("🤖 My AI Chatbot")

st.write("Welcome! Ask me anything.")


# --------------------------------
# 3. Get Gemini API Key
# --------------------------------

api_key = st.secrets["GOOGLE_API_KEY"]


# --------------------------------
# 4. Initialize Gemini Model
# --------------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key,
    temperature=0.7
)


# --------------------------------
# 5. Initialize Chat History
# --------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [

        SystemMessage(
            content="You are a helpful AI assistant. "
                    "Answer questions in simple English."
        )

    ]


# --------------------------------
# 6. Display Previous Messages
# --------------------------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# --------------------------------
# 7. Get User Input
# --------------------------------

user_input = st.chat_input("Type your message here...")


# --------------------------------
# 8. Generate AI Response
# --------------------------------

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.invoke(
                    st.session_state.messages
                )

                answer = response.content

                # Handle text response
                if isinstance(answer, list):

                    answer = "\n".join(
                        block["text"]
                        for block in answer
                        if isinstance(block, dict)
                        and block.get("type") == "text"
                    )

                st.write(answer)

                # Save AI response
                st.session_state.messages.append(
                    AIMessage(content=answer)
                )

            except Exception as e:

                st.error(f"Error: {e}")


# --------------------------------
# 9. Clear Chat
# --------------------------------

if st.button("Clear Chat"):

    st.session_state.messages = [

        SystemMessage(
            content="You are a helpful AI assistant. "
                    "Answer questions in simple English."
        )

    ]

    st.rerun()