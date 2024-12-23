import streamlit as st
from PIL import Image

def txt(a, b, c, d, name, head, image):
    st.header(head)
    st.image(image)
    st.write(f'{a}')
    st.markdown(f'### Project: `{name}`')
    st.markdown(f'##### {b}: {c}')
    st.markdown(f'#### Project: {d}')


img1 = Image.open("assests/sih.png")
img1 = img1.resize((400,200))
img2= Image.open("assests/hack4.png")
img3 = Image.open("assests/hacknuthon.png")

st.title('Hackathons')

t1, t2, t3= st.tabs(['SIH-2024', 'Hack for India', 'HackNuthon 4.0'])

with t1:
    txt("""I had a incredible opportunity to be part of SIH(Smart India Hackathon - Hardware Category) Finals held at **Manipal University, 
        Jaipur**. It was the best 5 days hardware hackathon worked with a amazing team to develop an innovative solution for the
         Ministry of Culture. Our project used computer vision and image processing technology to detect defects in the museum exhibits,
         learned many things in those 5 days.""",
         'Skills',
         '`Python`, `Flask`, `Yolov5`, `React`, `Vite`, `Typescript`, `OpenCV` ,`Supabase`',
         'https://github.com/Bala-Vignesh-Reddy/inception_frontend',
         'Smart AI Exhibit',
         'Smart India Hackathon 2024 - Hardware Category',
         img1)

with t2:
    txt("""Attended a 36-hour hackathon called Hack for India organized by Indian Oil and Silver Oak University. It was an incredible experience to be a part of this hackathon to showcase our skills and knowledge.
    During the hackathon, we created smart camera for MSMEs, that solves problems like product count, defect detection, Anamoly detection, Risk detection etc. above features are deployed on edge device like Raspberry pi attached with Webcam.
    """,
      'Skills', 
      '`TensorFlow`, `YOLO` , `Object Detection`, `IOT`, `Instance Detection`',
      'https://github.com/mayuras7685/HackNUthon-Unkils',
      'Smart Imaging Device',
      'Hack For India',
    img2)

with t3:
    txt("""I participated in a 24-hour hackathon,  HackNUthon organized by Nirma University, it was a incredible place to showcase our skills and knowledge.
During the hackathon, we worked on problem statment provide by Sponsers - Rapidops, automate or Create new feature for CRM, we create dashboard application that capable of showing sales forecasting, customer segmentation, customer classification etc.. 
       """,
      'Skills', 
      '`TensorFlow`, `Streamlit` , `Data Manuplation`, `pandas`, `numpy`',
      'https://github.com/Bala-Vignesh-Reddy/HackNUthon-Unkils',
      'ML for CRM',
      'HackNUthon 4.0',
      img3)