from flask import Flask, render_template, request
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

app = Flask(__name__)

# Directly assign the API key
groq_api_key = "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"

# Set up LLM
llm_grok = ChatGroq(
    api_key=groq_api_key,
    model_name='llama3-8b-8192',
    temperature=0.7
)

# Prompt Template
template = """
You are an expert summarizer. Read the following text carefully and write a clear, concise, and informative summary. 
Focus on the main ideas, key points, and important details. 
Remove any repetition or unnecessary filler. Keep the summary neutral and objective. 
The summary should be understandable to someone who has not read the original content. 
Maintain the original meaning and context. Highlight the most important conclusions, arguments, or results. 
The length of the summary should be medium.

- *short summary:* 1/3 of the input content

Text: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

chain = (
    {"question": RunnablePassthrough()}
    | prompt
    | llm_grok
    | output_parser
)

@app.route('/chat', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        user_input = request.form['input_text']
        summary = chain.invoke(user_input)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
