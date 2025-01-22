使用streamlit写一个程序，实现以下功能：

1.设置layout=wide。在侧边栏创建复选框，文字为“随机选择文件夹”，默认选中。选中时在下面显示刷新按钮，未选中时隐藏刷新按钮。

2.读取当前目录下files文件夹中的文件夹的视频。选中复选框时，在页面上显示随机文件夹的所有视频，点击刷新按钮切换到另一个随机文件夹。未选中复选框时，在侧边栏创建与当前目录下files文件夹中的文件夹名称相同的单选按钮，选中单选按钮时在页面上显示对应文件夹中的视频。

要使用Streamlit实现你描述的功能，可以按照以下步骤编写代码。以下是一个完整的示例代码：

```python
import os
import random
import streamlit as st

# 设置页面布局为wide
st.set_page_config(layout="wide")

# 获取当前目录下files文件夹中的所有文件夹
def get_folders():
    base_dir = "files"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    return folders

# 获取指定文件夹中的所有视频文件
def get_videos(folder):
    base_dir = "files"
    folder_path = os.path.join(base_dir, folder)
    videos = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mkv'))]
    return videos

# 在侧边栏创建复选框
random_folder = st.sidebar.checkbox("随机选择文件夹", value=True)

# 根据复选框的状态显示不同的内容
if random_folder:
    # 如果选中了“随机选择文件夹”，显示刷新按钮
    if st.sidebar.button("刷新"):
        pass  # 刷新按钮的逻辑在下面处理

    # 获取所有文件夹
    folders = get_folders()
    if folders:
        # 随机选择一个文件夹
        selected_folder = random.choice(folders)
        st.sidebar.write(f"当前选择的文件夹: {selected_folder}")

        # 获取该文件夹中的所有视频
        videos = get_videos(selected_folder)
        if videos:
            # 在页面上显示视频
            for video in videos:
                video_path = os.path.join("files", selected_folder, video)
                st.video(video_path)
        else:
            st.write("该文件夹中没有视频文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
else:
    # 如果未选中“随机选择文件夹”，在侧边栏创建单选按钮
    folders = get_folders()
    if folders:
        selected_folder = st.sidebar.radio("选择文件夹", folders)
        
        # 获取该文件夹中的所有视频
        videos = get_videos(selected_folder)
        if videos:
            # 在页面上显示视频
            for video in videos:
                video_path = os.path.join("files", selected_folder, video)
                st.video(video_path)
        else:
            st.write("该文件夹中没有视频文件。")
    else:
        st.write("files文件夹中没有子文件夹。")
```

### 代码说明：
1. **设置页面布局**：使用`st.set_page_config(layout="wide")`将页面布局设置为宽屏模式。
2. **获取文件夹和视频**：
   - `get_folders()`函数获取`files`文件夹中的所有子文件夹。
   - `get_videos(folder)`函数获取指定文件夹中的所有视频文件。
3. **侧边栏复选框**：使用`st.sidebar.checkbox`创建复选框，用于控制是否随机选择文件夹。
4. **随机选择文件夹**：
   - 如果复选框被选中，随机选择一个文件夹，并在页面上显示该文件夹中的所有视频。
   - 点击“刷新”按钮时，会重新随机选择一个文件夹并显示其中的视频。
5. **手动选择文件夹**：
   - 如果复选框未选中，在侧边栏创建单选按钮，用户可以选择特定的文件夹，并在页面上显示该文件夹中的所有视频。

### 运行程序：
1. 将代码保存为`app.py`。
2. 在终端中运行`streamlit run app.py`。
3. 打开浏览器，访问Streamlit提供的本地URL，即可看到效果。

### 注意事项：
- 确保在`files`文件夹中存在子文件夹，并且子文件夹中包含视频文件（如`.mp4`, `.avi`, `.mkv`等格式）。
- 如果`files`文件夹不存在，程序会自动创建它，但你需要手动添加子文件夹和视频文件。

希望这个示例代码能帮助你实现所需的功能！