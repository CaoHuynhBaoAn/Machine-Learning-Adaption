import cv2 as cv
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Features", ["Smoothing"],
        icons=['house', 'gear','gear'], menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#2C3845"}})



st.title("Image processing")


img_file = st.file_uploader("Choose a image file", type=["jpg","jpeg","png"])
if img_file is not None:
    # Convert the file to an opencv image.
    img_file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    image = cv.imdecode(img_file_bytes,1)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    '''
    Smoothing sections
    '''
    if selected == "Smoothing":
        Smoothing_selected = option_menu("Smoothing", ["Mean", 'Median', 'Gaussian', "Bilateral", "Dilation", "Erosion"],
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={ "container": {"padding": "5!important", "background-color": "#088F8F"},
                                    "icon": {"color": "orange", "font-size": "15px"},
                                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                    "nav-link-selected": {"background-color": "#2C3845"}})

        #Mean smoothing

        if Smoothing_selected == "Mean":
            st.write("**Parameters**")
            col1, col2 = st.columns(2)
            with col1:
                value = st.slider("Kernel value", 3, 63,3,2)
                kernel =(value,value)
                st.write("**Kernel:**", kernel)
            with col2:
                b_types = st.selectbox("Border type", ["CONSTANT", "REPLICATE","REFLECT", "TRANSPARENT", "ISOLATED"])
                if b_types == "CONSTANT":
                    bt = 0
                elif b_types == "REPLICATE":
                    bt = 1
                elif b_types == "REFLECT":
                    bt = 2
                elif b_types == "TRANSPARENT":
                    bt = 5
                elif b_types == "ISOLATED":
                    bt = 16
                st.write("**Border type:**",b_types )
            img = cv.blur(image, kernel,borderType = bt)
            st.write("**Image processed**")
            st.image(img, channels="RGB")

        #Dilation filter

        if Smoothing_selected == "Dilation":
            st.write("**Parameters**")
            value = st.slider("Dilation value", 3, 63, 3, 2)
            st.write("**Dilation value:**", value)
            img = cv.dilate(image, None, iterations=value)
            st.write("**Image processed**")
            st.image(img, channels="RGB")

        #Erosion filter

        if Smoothing_selected == "Erosion":
            st.write("**Parameters**")
            value = st.slider("Erosion value", 3, 63, 3, 2)
            st.write("**Erosion value:**", value)
            img = cv.erode(image, None, iterations=value)
            st.write("**Image processed**")
            st.image(img, channels="RGB")

        #Median smoothing

        if Smoothing_selected == "Median":
            st.write("**Parameters**")
            value = st.slider("Median value", 3, 63,3,2)
            st.write("**Median value:**", value)
            img = cv.medianBlur(image, value)
            st.write("**Image processed**")
            st.image(img, channels="RGB")

         #Gaussian smoothing

        if Smoothing_selected == "Gaussian":
            st.write("**Parameters**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                value = st.slider("Kernel value", 3, 63,3,2)
                kernel =(value,value)
                st.write("**Kernel:**", kernel)
            with col2:
                sigmax = st.slider("SigmaX", 0.0, 100.0,0.0,0.5)
                st.write("**SigmaX:**", sigmax)
            with col3:
                sigmay = st.slider("SigmaY", 0.0, 100.0,0.0,0.5)
                st.write("**SigmaY:**", sigmay)
            with col4:
                b_types = st.selectbox("Border type", ["CONSTANT", "REPLICATE","REFLECT", "ISOLATED"])
                if b_types == "CONSTANT":
                    bt = 0
                elif b_types == "REPLICATE":
                    bt = 1
                elif b_types == "REFLECT":
                    bt = 2
                elif b_types == "ISOLATED":
                    bt = 16
                st.write("**Border type:**",b_types )
            img = cv.GaussianBlur(image, kernel,sigmaX=sigmax, sigmaY=sigmay, borderType = bt)
            st.write("**Image processed**")
            st.image(img, channels="RGB")

        #Bilateral smoothing

        if Smoothing_selected == "Bilateral":
            st.write("**Parameters**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                diameter  = st.slider("Diameter ", 5, 9,5,1)
                st.write("**Diameter:**", diameter)
            with col2:
                sigmac = st.slider("SigmaColor", 0.0, 100.0,0.0,0.5)
                st.write("**Sigma Color:**", sigmac)
            with col3:
                sigmas = st.slider("SigmaSpace", 0.0, 100.0,0.0,0.5)
                st.write("**Sigma Space:**", sigmas)
            with col4:
                b_types = st.selectbox("Border type", ["CONSTANT", "REPLICATE","REFLECT", "ISOLATED"])
                if b_types == "CONSTANT":
                    bt = 0
                elif b_types == "REPLICATE":
                    bt = 1
                elif b_types == "REFLECT":
                    bt = 2
                elif b_types == "ISOLATED":
                    bt = 16
                st.write("**Border type:**",b_types )
            img = cv.bilateralFilter(image, d=diameter,sigmaColor=sigmac, sigmaSpace=sigmas, borderType = bt)
            st.write("**Image processed**")
            st.image(img, channels="RGB", use_column_width=False)