# Policy Assistant

A conversational assistant that answers questions about college policies using local LLMs and retrieved documents.

## Features

- Ask questions about official college policy documents
- Uses LangChain's Retrieval-Augmented Generation (RAG)
- Stores embedded PDFs using Chroma vector database
- Built with Streamlit for chat interface
- Powered by locally running Ollama LLM

## Installation

### 1. **Install Ollama**

Visit the [Ollama website](https://ollama.com/) and follow instructions for your platform.
Then start the Ollama service:

```bash
ollama serve
```

### 2. **Download LLM and Embeddnig models**

For this project, llama3.2 and nomic-embed-text was used.

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 3. **Clone the repository**

```bash
git clone https://github.com/yourusername/policy-assistant.git
cd policy-assistant
```

### 4. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 5. **Install dependencies**

```bash
pip install -r requirements.txt
```

### 6. **Run the vector builder (for PDF ingestion)**

Put your college policy PDFs into the ```data/``` folder, then run:
```bash
python vector.py
# to reset the vector store add '--reset' flag
```

### 7. **Start Streamlit app**

```bash
streamlit run app.py
```

### Notes
The app uses conversational memory (last 3 turns) for better context.
The response will state clearly if the answer is not found in the provided documents.

### License
This project is open-source and licensed under the MIT License.