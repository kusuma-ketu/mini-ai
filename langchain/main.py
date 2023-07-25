import os 
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "7ae33e5734092727a5e20cd937dd841c35f1b6a4240bf9a4717eaf5232809457"

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm1 = ChatOpenAI(model_name = "gpt-3.5-turbo")
llm1("tell me a joke")

prompt = PromptTemplate(
 input_variables=["input"],
 template="Which are the 5 most {input} capital cities?",
)

chain = LLMChain(llm=llm1, prompt=prompt)
