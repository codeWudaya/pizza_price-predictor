import streamlit as st
import joblib
import numpy as np
import pandas as pd


def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Pizza Price Predictor</h2>
    </div>
    
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('pizza_price_predict')

    p1 = st.slider('Enter Company ', 0, 4)
    p2 = st.number_input('Enter size', 7, 23)
    p3 = st.number_input("Enter topping", 0, 12)
    p4 = st.number_input("variant", 1, 20)
    p5 = st.slider('Enter size', 0, 5)

    s6 = st.selectbox("Enter extra_sauce", ("Yes", "No"))
    if s6 == 'Yes':
        p6 = 1
    else:
        p6 = 0

    s7 = st.selectbox("Enter extra_cheese", ("Yes", "No"))
    if s7 == 'Yes':
        p7 = 1
    else:
        p7 = 0

    s8 = st.selectbox("Enter extra_extra_mushrooms", ("Yes", "No"))
    if s8 == 'Yes':
        p8 = 1
    else:
        p8 = 0

    if st.button('Predict'):
        df = pd.DataFrame({
            'company': p1,
            'diameter': p2,
            'topping': p3,
            'variant': p4,
            'size': p5,
            'extra_sauce': p6,
            'extra_cheese': p7,
            'extra_mushrooms': p8
        }, index=[0])
        result = model.predict(df)
        st.balloons()
        st.success('Predicted Pizza cost should be {}'.format(result))

        st.success('')


if __name__ == '__main__':
    main()