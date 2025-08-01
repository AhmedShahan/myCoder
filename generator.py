from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # or any other LLM you're using

def generate_code(prompt: str) -> str:
    llm = OpenAI()
    template = PromptTemplate.from_template("Write Python code to:\n{task}")
    chain = LLMChain(llm=llm, prompt=template)
    return chain.run(task=prompt)
