import streamlit as st

# st.set_page_config(page_title="About Me", page_icon='👨‍💻')


def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt1(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

with st.container():
  col1, col2 = st.columns([5,1])
  with col1:
    st.title("About Me 👨‍💻")
  with col2:
    # st.download_button('Resume)
    pass
 
st.write("----")

with st.container():
  st.write("Hello, I'm Bala Vignesh, an ***Electronics and Communication Engineering*** Undergraduate from ***Vishwakarma Government Engineering College***, Ahmedabad.")
  st.write("I am a hardworking individual with a strong passion for learning and expanding my knowledge and skils. My academic background, \
           combined with my passion drives me to constantly explore and deepen my understanding in these fields.")
  st.write("I am also dedicated to apply my technical skills to solve real-life challenges and contribute to innovative projects. \
           Whether it's working with the Raspberry pi or solving the real-life problem using computer vision technology. \
           I am commited to continuously growing and evolving as a person")

st.write("----")

st.title('Skills & Tools ⚒️')
txt1('Programming Language', '`Python`, `C`, `C++`, `Bash Scripting`, `Javascript`')
txt1('Edge Devices', '`Raspberry Pi`, `Arduino`')
txt1('Databases', '`Mysql`, `PostgreSQL`, `SQLite3`')
txt1('Machine Learning', '`YOLO`, `OpenCV`, `PyTorch`')
txt1('Web development', '`Flask`, `HTML`, `CSS`')
txt1('Tools', '`Docker`, `Colab`, `Roboflow`')
txt1('Operating Systems', '`Linux`, `Windows`')

st.write("----")

st.title('Education 📖')
txt('**Bachelors in Engineering** (Electronics and Communication), *Vishwakarma Government Engineering College*, Ahmedabad',
'2022-2026')
st.markdown('''
- CGPA:  `9.07`
''')

st.write('-----')

txt('**HSC (Class XII)**, *Hillwoods School*, Gandhinagar',
'2022')
st.markdown('''
- Percentage: `90.00`
''')

st.write('-----')

txt('**SSC (Class X)**, *Hillwoods School*, Gandhinagar',
'2020')
st.markdown('''
- Percentage: `88.00`
''')

