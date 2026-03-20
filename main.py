import streamlit as st
from unit import generate_script
st.title("## 视频脚本生成器")
with st.sidebar:
    api_key=st.text_input("please input API",type="password") # sk-RDLwY6GavCOj6zhvxozaEfbcfpNgruq8sU3FG5eHMCJuJvGX
    api_base=st.text_input("please input API URL",type="password")   #  https://aigc789.top/v1
    st.markdown("[get API](https://api.whatai.cc/personal)")

subject=st.text_input("please input the theme of video")
video_length=st.number_input("please input the time of video(min)",min_value=0.1,max_value=10.0,step=0.1)
creativity=st.slider("please input the creativity of video",min_value=0.0,max_value=2.0,step=0.1)
submit=st.button("生成脚本")
if submit and not api_key:
    st.info("input API")
    st.stop()
if submit and not subject:
    st.info("input subject")
    st.stop()
if submit and not video_length>=0.1:
    st.info("video_length should be greater than 0.1")

if submit:
    with st.spinner(("waiting...")):
        title,script=generate_script(subject,video_length,creativity,api_key,api_base)
    st.success("completed")
    st.subheader("title:")
    st.write(title)
    st.subheader("script:")
    st.write(script)