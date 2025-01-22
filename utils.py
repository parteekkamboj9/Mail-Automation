from typing import AnyStr, Any
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_pinecone import PineconeVectorStore
import app_config

embed =  OpenAIEmbeddings(model='text-embedding-3-small', dimensions=512)
index_name = app_config.PINECONE_INDEX_NAME
temp = 0.5
prompt = ''

def retrieving_pinecone(query: AnyStr):
    # getting response from the stored vector
    docsearch = PineconeVectorStore(embedding=embed)
    # docsearch = Pinecone.from_existing_index(index_name, getHuggingFaceEmbeddingModel(embed_model), namespace=namespace)
    prompt_template = prompt + """

    {context}

    Question: {question}
    Answer: 
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}

    llm = OpenAI(temperature=temp)

    similarDocs = docsearch.similarity_search(query=query)

    chainQA = load_qa_chain(llm, chain_type="stuff")

    # response = chainQA({"input_documents": similarDocs, "question": query}, return_only_outputs=True)
    response = chainQA.run(input_documents=similarDocs, question=query)
    print("Response >>>", response)
    print("Similar Docs >>>", similarDocs)
    # qa = RetrievalQA.from_chain_type(
    #     ,
    #     chain_type="stuff",
    #     retriever=docsearch.as_retriever(),
    #     return_source_documents=True,
    #     chain_type_kwargs=chain_type_kwargs
    # )
    # # response = qa.run(query)
    # response = qa({"query": query})

    # return response['result'], response['source_documents']
    return response, similarDocs


def generate_response(query: AnyStr):
    response, _ = retrieving_pinecone(query)
    return response

