import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Báo Cáo Đồ Án Machine Learning! 👋")

st.sidebar.success("Select a demo above.")

image = Image.open('images/Machine-Learning.jpg')
st.image(image)
st.markdown(
    """
    ### Môn học: 
    - Học Máy
    ### Giảng Viên: 
    - Thầy Trần Tiến Đức
    ### Thông tin sinh viên:
    - Cao Huỳnh Bảo An 20126087
    ### Giới thiệu đề tài:
    Đề tài gồm có 6 chức năng chính:
    - Phát hiện khuôn mặt
    - Nhận diện khuôn mặt
    - Dự đoán giá nhà Cali
    - Nhận diện chữ số viết tay
    - Xử lý ảnh
    - Phân loại chó mèo
    ### Link Github 
    - https://github.com/CaoHuynhBaoAn
"""
)
