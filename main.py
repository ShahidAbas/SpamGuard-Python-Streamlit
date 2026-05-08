import streamlit as st
import pickle 
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# make a function which will work for all as mentioned above in heading 3

def transform_text(text):
    
    text = text.lower() # to sole the lower case
    
    text = nltk.word_tokenize(text) # to solve tokenization
    
    y = []
    for i in text:         #we noly keep the alphabate and alphanumerics
        if i.isalnum():    #special characters will be removed
            y.append(i)
            
            
    text = y [:]
    y.clear()             #clear the set
                          #removing stop words and punctuation
                         
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()           
    
                         #clear the same meaning words only 
                         #reurn base form of word
    for i in text:
        y.append(ps.stem(i))
        
                           #joining strings
    return " ".join(y)
#####

model = pickle.load(open('model_spam.pkl','rb'))
tfidf = pickle.load(open('vectorizer_spam.pkl','rb'))

st.title("SpamGaurdAi")

input_text = st.text_area("Enter the message")

if st.button('Predict'):

    #1. preprocess
    transformed_sms = transform_text(input_text)
    #2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    #4. display
    if result == 1:

       st.header("Spam")

    else:

      st.header("Not Spam")





