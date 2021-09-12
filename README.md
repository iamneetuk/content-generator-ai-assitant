# Content Writing AI

This library provides an NLP model to generate different types of content based on input keywords.
1. Business Descriptions: This model generates business descriptions that can be used for Google Ads, Facebook Ads, website headlines, etc.
2. Email Autocomplete: Coming soon.

Built by [Kamal Kant](https://kama1kant.com/)

##  How it works
### Dataset
The dataset consists of various business details from Angelist, Linkedin, etc. Example dataset can be found inside the "data" directory.
Using Spacy's named entity recognition We pick out keywords from the business description & store them in a separate file which will act as a Natural-language generation dataset.

### Model
This project use [T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) which is a text-to-text transfer transformer.


### Training
T5 model is trained on the business's NLG dataset, where the model learns the mapping between keywords and their corresponding full text.


## How to run
- Download the repository
- Navigate to "business-descriptions/src/"
- Run the following command
```py
streamlit run streamlit-business-description-generator.py
```

## Libraries used
- Pytorch
- Huggingface Transformers
- T5
- Spacy
- Pandas
- NumPy

## Contact
If you have any questions or feedback, feel free to reach out to me at <kamalkant.k3@gmail.com>