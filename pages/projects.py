import streamlit as st
from PIL import Image

# st.set_page_config(page_title='Projects', page_icon='🗂️' )


st.title('Projects')

st.write('---')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assests/p2.png'))
  with col2:
    st.subheader("Object Detection for Yolov5 Models")
    st.write("""Created a web app where user can upload there yolov5 model and check how their model is performing, with few clicks.""")

    st.markdown('`Computer Vision`, `Streamlit`, `openncv-python`, `Yolov5`, `Roboflow`, `colab` ')
    col1, col2 = st.columns((1,2))
    with col1:
        g2 = '[GitHub](https://github.com/Bala-Vignesh-Reddy/Object-Detection-Yolov5)'
        st.markdown(g2)
    with col2:
        g3 = '[Live-Site](https://object-detection-yolov5.streamlit.app/)'
        st.markdown(g3)

st.write('---')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assests/p1.jpg'))
  with col2:
    st.subheader("Smart AI Exhibit")
    st.write("""
    This project is an innovative solution for real-time monitoring and defect detection in museum exhibits using AI and computer vision, enhancing maintenance and visitor engagement.
             """)

    st.markdown('`Python`, `Raspberry Pi`, `Cameras`, `Yolo`,  `Flask`, `React`, `Vite`, `Typescript`, `OpenCv`, `Supabase`')

    g6 = '[GitHub](https://github.com/Bala-Vignesh-Reddy/inception_frontend)'
    st.markdown(g6)

st.write('---')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./assests/p3.png'))
  with col2:
    st.subheader("Deadly Animal Detection")
    st.write("""
   Custom object detection model that detects wild animals and generates an alert to notify the people living near by.
             """)

    st.markdown('`Computer Vision`, `openncv-python`, `Streamlit` , `Yolo`, `Roboflow`, `colab` ')

    g1 = '[GitHub](https://github.com/Bala-Vignesh-Reddy/WildLife-Detection)'
    st.markdown(g1)

st.write('---')

with st.container():
  col5,col6 = st.columns((1, 2))
  with col5:
    st.image(Image.open('./assests/p4.png'))
  with col6:
    st.subheader("Pi-hole: Personal Ad-Blocker")
    st.write("""
    Pi-hole is a network-wide ad blocker that filters DNS request and block ads and trackers, it can be easily set up on a raspberry pi or any linux machine.
    """)

    st.markdown('`Raspberry Pi`, `Pi-hole`, `Linux`')

    g3 = '[GitHub](https://gist.github.com/Bala-Vignesh-Reddy/a75f6f957c01846e6fbf4ad21238d72a)'
    st.markdown(g3)

st.write('---')

st.subheader("More Projects are Cooking and left to add in list ...")