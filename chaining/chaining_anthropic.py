# Langchain Expression Language (LCEL) with the Anthropic language model.
#
# This example reads a positive review and generates a response message.
# 1. Extract the customer's name and sentiment from the review
# 2. Transform the extracted data into a JSON format
# 3. Generate a response message based on the sentiment

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatAnthropic(model="claude-haiku-4-5-20251001", temperature=0)


# Prompt 1
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the customer's name and the sentiment of the review: {review}"
)

# Prompt 2
prompt_details = ChatPromptTemplate.from_template(
    "Transform the following data into a JSON format with 'customer_name' and 'sentiment' as keys: {details}"
)

# Prompt 3
prompt_response = ChatPromptTemplate.from_template(
    "Write a one-paragraph response message based on the sentiment of the review: {details}"
)


# Build the chain using LCEL (Langchain Expression Language)
review_chain = prompt_extract | llm | StrOutputParser()

details_chain = {"details": review_chain} | prompt_details | llm | StrOutputParser()

chain = ({"details": details_chain} | prompt_response | llm | StrOutputParser())


# Invoke the chain.
review = """
    Luis Alberto. As a buyer, the NVIDIA DGX Spark impressed me with the significant AI power it delivers in a compact,
    ready-to-use machine. It is an excellent option for developers and data scientists who want to experiment with and
    prototype models quickly using NVIDIA technology.
    """

result = chain.invoke({"review": review})


print(result)
