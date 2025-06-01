from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="gemma3:1b", streaming=True)

template = """
You are a helpful assistant who knows about a pizza restuarant. Answer the user's question accurately.

Here are some relevant reviews: {reviews}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n----------------------------------------------")
    question = input("Enter your question (or type 'q' to quit): ")
    print("\n\n")
    if question.lower() == 'q':
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)
