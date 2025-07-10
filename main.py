import os
import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from prompt_modes import prompt_templates
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
CHROMA_PATH = "chroma"

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)
    return db

def set_custom_prompt(custom_prompt_template):
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    return prompt

def load_chat_llm(huggingface_repo_id, HF_TOKEN):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        temperature=0.5,
        huggingfacehub_api_token=HF_TOKEN,
        max_new_tokens=512
    )
    chat_llm = ChatHuggingFace(llm=llm)
    return chat_llm

def main():
    st.title("🌟 AutiMate")
    st.markdown("_Kind, clear, and here for you._")

    with st.sidebar:
        st.markdown("## 🌈 Support Style")
        st.markdown("Pick the kind of help you’d like right now:")
    
        mode = st.radio(
            label="",
            options=list(prompt_templates.keys()),
            index=0
        )
    
        st.markdown("---")
        st.markdown("✨ You can switch styles any time.")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    prompt = st.chat_input("Pass your prompt here")

    if prompt:
        st.chat_message('user',avatar="🙂").markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})


        HUGGINGFACE_REPO_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        HF_TOKEN = os.environ.get("HF_TOKEN")

        try:
            vectorstore = get_vectorstore()
            if vectorstore is None:
                st.error("Failed to load the vector store")

            chat_llm = load_chat_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, HF_TOKEN=HF_TOKEN)

            qa_chain = ConversationalRetrievalChain.from_llm(
                llm=chat_llm,
                retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                return_source_documents=True,
                combine_docs_chain_kwargs={'prompt': set_custom_prompt(prompt_templates[mode])}
            )

            chat_history = [
                (msg['content'], st.session_state.messages[i+1]['content'])
                for i, msg in enumerate(st.session_state.messages[:-1])
                if msg['role'] == 'user' and i+1 < len(st.session_state.messages) and st.session_state.messages[i+1]['role'] == 'assistant'
            ]

            response = qa_chain.invoke({'question': prompt, 'chat_history': chat_history})

            result = response["answer"]
            source_documents = response["source_documents"]
            result_to_show = result
            st.chat_message('assistant',avatar="🌟").markdown(result_to_show)
            st.session_state.messages.append({'role': 'assistant', 'content': result_to_show})

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
