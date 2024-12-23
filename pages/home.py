import streamlit as st
from form.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

with st.container():
    col1, col2 = st.columns((2, 1), vertical_alignment="center")
    with col1:
        st.title("Hi 👋, I'm Bala Vignesh")
        st.header(
            """
            A Tech Enthusiast, 
            with a strong foundation in Linux and technology, I am continuously exploring diverse areas - from learning Raspberry Pi to implementing Image Processing on Edge devices - demonstrating my passion for innovation and learning.
            """
        )
    st.write('----')

    st.subheader('Connect with me:')
    st.markdown(
        """
        <div style="display: flex; gap: 20px;">
            <a href="https://github.com/Bala-Vignesh-Reddy" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40">
            </a>
            <a href="https://www.linkedin.com/in/bala-vignesh-reddy/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            </a>
            <a href="https://twitter.com/BalaVignesh_1" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="40">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    # st.markdown(
    #     """
    #     [Github](https://github.com/Bala-Vignesh-Reddy) | 
    #     [LinkedIn](https://www.linkedin.com/in/bala-vignesh-reddy/) | 
    #     [X](https://x.com/BalaVignesh_1)
    #     """
    # )
    st.write('----')

    st.subheader("Get in touch:")
    if st.button("📩 Contact Me"):
        contact_form()

    with col2:
        st.image('assests/image.jpeg')
