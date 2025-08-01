from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # or any other
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
def generate_code(task: str) -> str:
    prompt_template = PromptTemplate.from_template(
    '''Write only the Python code to:\n{task}\nDo not include any explanation or markdown. Please don't make the MARKDOWN and also other line. 
    Example: 
    # === LangCoder Output ===
```python
def add_numbers(x, y):
  return x + y
```

output will be like just
def add_numbers(x, y):
  return x + y
    
    ''')
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.9)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run(task=task)
