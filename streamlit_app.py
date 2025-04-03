import streamlit as st

st.set_page_config(layout="wide")

st.title("Hunyuan Video Gallery")
st.subheader("1.创建和修改原因",divider=True)
st.write("本项目创建时展示我使用Hunyuan Video生成的视频内容。后面由于改用速度更快的Wan2.1 1.3b进行视频生成，本项目没有合并到gallery项目。")
st.write("近期改用Cogview4进行图片生成，gallery项目中的AI图片部分也改用Cogview4生成的内容，此前使用Hunyuan Video生成的图片移动到本项目，不再保留更早的无提示词项目。")

st.subheader("2.项目细节",divider=True)
st.write("Hunyuan Video虽然是图片视频统一生成模型，但图片生成的细节表现一般。后面尝试了q6_k精度的模型，显存占用较大，不适合视频生成但图片生成效果有一定改善。提示词方面，复用了之前使用Flux.1的提示词，移除了生成效果一般的内容。")
st.write("视频部分创建早一些，测试了Hunyuan Video可用的最大分辨率，综合显存占用因素选择了1584x896分辨率。使用这一分辨率在8g显存下最多生成长度21帧的视频，本项目的视频也使用这一规格。")

