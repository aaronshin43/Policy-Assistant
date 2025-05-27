import streamlit as st
from rag_chain import get_conversational_rag_chain, get_context
from htmlTemplates import css
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama.llms import OllamaLLM

def format_chat_history(messages, turns=3):
    limited_history = messages[-(turns * 2):]

    history = ""
    for msg in limited_history:
        if isinstance(msg, HumanMessage):
            history += f"User: {msg.content}\n"
        # elif isinstance(msg, AIMessage):
        #     history += f"Assistant: {msg.content}\n"
    return history.strip()

def stream_llm_rag_response(model, question, chat_history):
    rag_chain = get_conversational_rag_chain(model)
    context = get_context(question)

    inputs = {
        "context": context,
        "question": question,
        "chat_history": chat_history
    }

    response_message = ""
    for chunk in rag_chain.stream(inputs):
        response_message += chunk
        yield chunk

    st.session_state.messages.append(AIMessage(response_message))

def main():
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.header("Chat with multiple PDFs :books:")

    model = OllamaLLM(model="llama3.2", stream=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat history
    for message in st.session_state.messages:
        with st.chat_message("user" if isinstance(message, HumanMessage) else "ai"):
            st.markdown(message.content)

    user_question = st.chat_input("Ask a question about Dickinson policies")
    if user_question:

        with st.chat_message("user"):
            st.markdown(user_question)
        st.session_state.messages.append(HumanMessage(user_question))

        with st.chat_message("ai"):
            chat_history = format_chat_history(st.session_state.messages[:-1], turns=3)
            st.write_stream(stream_llm_rag_response(model, user_question, chat_history))


if __name__ == '__main__':
    main()