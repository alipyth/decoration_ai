#pip install -q -U google-generativeai
#pip install ipython
#pip install pillow
#PIP INSTALL STREAMLIT
import streamlit as st
from PIL import Image
import google.generativeai as genai
from deep_translator.google import GoogleTranslator

#api = st.text_input('put your api')

API = "Put Your API Here"

genai.configure(api_key=API)
model = genai.GenerativeModel('gemini-pro-vision')
picture = st.camera_input("Take a picture")
pr = 'How can i improve Design of my room ? and tell me what you see in the image'
but = st.button('Lets Go')
if picture and but :
    img = Image.open(picture)
    response = model.generate_content([pr , img])
    st.image(img)
    st.markdown(response.text)
    translated = GoogleTranslator(source='auto', target='fa').translate(response.text)
    st.markdown(translated)

st.info('Developed By : Ali Jahani satreyek@gmail.com')
