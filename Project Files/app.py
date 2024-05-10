import streamlit as st
import numpy as np
from google.cloud import translate_v2 as translate

# setting up the api key configuration
api_key = '<Enter your API KEY>'

translator = translate.Client(api_key=api_key)

st.title("Language-Translator")

# setting up the dropdown list of the languages
option = st.selectbox(
    'Which language would you choose to type',
    ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))

option1 = st.selectbox('Which language would you like to translate to',
                       ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))

sent = "Enter the text in "+option+" language in the text-area provided below"

# setting up the dictionary of languages to their keywords
language_lib = {'English': 'en', 'Arabic': 'ar',
                'Hindi': 'hi', 'Spanish': 'es', 'German': 'de', 'Korean': 'ko'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select different Language for Translation")
        else:
            translate_code = language_lib[option]+'-'+language_lib[option1]
            translation = translator.translate(
                sentence, target_language=language_lib[option1], source_language=language_lib[option])

            ans = translation['translatedText']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except Exception as e:
        st.write("An error occurred: ", str(e))
        st.write("Please do cross check if the text-area is filled with sentences or not")
