from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate

import os

# GETTING THE API KEY from os environment
openai_api_key = os.environ.get('OPENAI_API_KEY')

video_captions = './captions.vtt'

with open(video_captions, 'r') as file:
    captions = file.read()

llm = OpenAI(temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-instruct")

llm.get_num_tokens(captions)

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n"], chunk_size=5000, chunk_overlap=400)

docs = text_splitter.create_documents([captions])

num_docs = len(docs)
num_tokens_first_doc = llm.get_num_tokens(docs[0].page_content)
print (f"Now we have {num_docs} documents and the first one has {num_tokens_first_doc} tokens")


template = """
Summarize the following SBV subtitles from a video in one single topic and add the time it started and ended, returning the output in only this JSON format {{"start":"00:00:00","end":"00:00:00","topic":"..."}}:
{doc}
"""

prompt = PromptTemplate(
    input_variables=["doc"],
    template=template
)

for doc in docs:
  summary_prompt = prompt.format(doc=doc.page_content)
  num_tokens = llm.get_num_tokens(summary_prompt)
  summary = llm(summary_prompt)
  print (summary.strip())
