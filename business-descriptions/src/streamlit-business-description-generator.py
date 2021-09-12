import streamlit as st
import pandas as pd
import os
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers.optimization import Adafactor 
import time
import warnings
from IPython.display import HTML, display
import spacy
import unicodedata
import string


class ContentGenerator():
    def __init__(self):
        self.checkpoint_path = '../checkpoint/business-description-generator-model.bin'
        self.config_path = '../data/t5-base-config.json'
        self.nlp = spacy.load("en_core_web_sm")
    
    def getTokenizer(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        
    def progress(self, loss,value, max=100):
        return HTML(""" Batch loss :{loss}
            <progress
                value='{value}'
                max='{max}',
                style='width: 100%'
            >
                {value}
            </progress>
        """.format(loss=loss,value=value, max=max))
    
    def loadModel(self):
        return T5ForConditionalGeneration.from_pretrained(self.checkpoint_path, return_dict=True, config=self.config_path)
    
    def generate(self, text):
        torch.manual_seed(0)
        model = self.loadModel()
        model.eval()
        input_ids = self.tokenizer.encode("WebNLG:{} </s>".format(text), return_tensors="pt")
        sample_outputs = model.generate(
            input_ids,
            do_sample=True,
            max_length=100, 
            top_k=4, 
            top_p=0.99,
            num_return_sequences=10
        )

        output = []
        for i, sample_output in enumerate(sample_outputs):
            output.append(self.tokenizer.decode(sample_output, skip_special_tokens=True))
        return output
    
    def getKeywords(self, text):
        doc = self.nlp(text)
        keywords = []
        for token in doc:
            if (not token.is_stop and token.is_alpha) and (token.tag_ == 'NNP' or token.tag_ == 'NN'):
                keywords.append(token.lemma_)
        keywords = pd.Series(keywords).drop_duplicates().tolist()
        keywords = ' | '.join(keywords)
        return keywords

    
obj = ContentGenerator()
obj.getTokenizer()

st.title("Business description generator")
st.subheader("Write keywords about a company")
html = '<p style="color:Grey; font-size: 12px;">Eg; Pied Piper | blockchain | new internet </p>'
st.markdown(html, unsafe_allow_html=True)
text = st.text_input('Enter text')
st.subheader("Generated descriptions")

if len(text) > 0:
#     text = obj.getKeywords(text)
#     st.write('Keywords: ', text)
    output = obj.generate(text)
    
    for i in range(len(output)):
        st.write(i, output[i])