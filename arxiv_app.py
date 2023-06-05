from dotenv import load_dotenv

import streamlit as st
import arxiv
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

import os

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ChatVectorDBChain
from langchain.llms import OpenAI
import requests

load_dotenv()

embeddings = OpenAIEmbeddings()

url = 'https://arxiv.org/category_taxonomy'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
pairings = []

for div in soup.find_all('div', class_='columns divided'):
    h4 = div.find('h4')
    code = h4.contents[0].strip()
    span = h4.find('span')
    if span:
        name = span.text.strip('()')
        pairings.append({'Code': code, 'Name': name})

# Function to fetch arxiv data
def fetch_data(category_code):
    search = arxiv.Search(
        query=f'cat:{category_code}',
        max_results=100,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    papers = list(search.results())
    dataset = []

    for result in papers:
        result.pdf_url = re.sub(r'v\d+$', '', result.pdf_url)

        dataset.append({
            'authors': result.authors,
            'categories': result.categories,
            'pdf_url': result.pdf_url,
            'summary': result.summary,
            'title': result.title,
        })

    return pd.DataFrame(dataset)

# UI for selecting category
st.title('ArXiv Paper Browser')
category = st.selectbox('Select a category:', options=pairings, format_func=lambda x: f"{x['Code']} ({x['Name']})")

if st.button('Fetch Papers'):
    st.write(f"Fetching papers for category {category['Name']} ({category['Code']})...")
    df = fetch_data(category['Code'])
    clean = df[['title', 'summary', 'authors', 'categories', 'pdf_url']]

    for index, row in clean.iterrows():
        pdf_url = f"https://export.{row['pdf_url'].split('://')[-1]}.pdf"
        
        st.markdown(f"### [{row['title']}]({pdf_url})")
        st.write(f"**Authors:** {', '.join([str(author) for author in row['authors']])}")
        st.write(f"**Categories:** {', '.join(row['categories'])}")

        expander = st.expander('Read Summary')
        if expander:
            expander.write(row['summary'])
        
        pdf_content = requests.get(pdf_url).content
        st.download_button('Download PDF', pdf_content, f"{row['title']}.pdf")




