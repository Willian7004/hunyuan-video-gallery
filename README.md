hunyuan-video-gallery

本项目内容为本人使用Hunyuan Video生成的有提示词的视频内容，比之前的无提示词流程出片率高。可以选择随机显示或显示特定文件夹的内容。虽然使用ConfyUI官方工作流时能生成图片，但考虑到是视频模型，本项目只包含视频内容。

本项目逻辑部分使用LLM辅助生成，对话记录位于streamlit_app.md

本项目已部署到Streamlit Cloud，域名为https://william7004-hunyuan-video-gallery.streamlit.app

本地部署流程

建议使用Python=3.10环境

1.安装依赖
```bash
pip install -r requirements.txt
```
2.运行应用
```bash
streamlit run streamlit_app.py
```
