from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from vector import get_embedding_function

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
You are an assistant to answer questions based on college policies.
Use the following policy context to answer the user's question.
Only include information found in the context. 
If the answer isn't in the context, say "I couldn't find relevant information".
Use chat history only to clarify the user's intent.

Chat History:
{chat_history}

Context:
{context}

Question:
{question}

Answer in a clear, concise, and helpful manner.
"""

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

def get_conversational_rag_chain(model):
    return prompt | model

def get_context(question: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(question, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    return context_text