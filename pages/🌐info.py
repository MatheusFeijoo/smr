import streamlit as st

st.set_page_config(layout = "wide",
                   page_title = "SMR Info",
                   page_icon = "🌐")


title1, title2, title3 = st.columns((0.9,1,0.9)) 

with title2:
    st.title('SMR Self-Assessment Tool 🌐')
    st.image('qrcode_smr_tool.png', width = 500)
    st.subheader('https://smr-tool.streamlit.app/', divider='gray')