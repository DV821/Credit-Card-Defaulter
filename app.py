import numpy as np
import pickle
import streamlit as st
pickle_in = open("model.pkl","rb")
model = pickle.load(pickle_in)


def predict(features):
    prediction = model.predict(features)
    if prediction[0]==1:
        return "Defaulter!!"
    else:
        return "Not A Defaulter!!"


def main():

    html_temp = """
    <div style="background-color: yellowgreen; padding : 10px">
    <h2 style="color:white; text-align:center;">Credit Card Defaulter Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    limit_bal = st.number_input('Balance Limit', min_value=0 )
    edu = ["1 - Graduate School", "2 - University", "3 - High School", "4 - Others"]
    mrrg = ["1 - Married", "2 - Single", "3 - Others"]
    pay1 = ["account started that month with a zero balance, and never used any credit",
        "account had a balance that was paid in full",
        "at least the minimum payment was made, but the entire balance wasn't paid",
        "payment delay for 1 month",
        "payment delay for 2 month",
        "payment delay for 3 month",
        "payment delay for 4 month",
        "payment delay for 5 month",
        "payment delay for 6 month",
        "payment delay for 7 month",
        "payment delay for 8 month"]
    education = edu.index(st.selectbox( "Education", tuple(edu) ))+1
    marriage = mrrg.index(st.selectbox( "Marital Status", tuple(mrrg) ))+1
    age = st.number_input("Age (in Years)", min_value=0)
    pay1 = pay1.index(st.selectbox( "Pay_1", tuple(pay1) ))-2
    bill_amt1 = st.number_input("Last month Bill Amount ", min_value=0 )
    bill_amt2 = st.number_input("Last 2nd month Bill Amount  ", min_value=0 )
    bill_amt3 = st.number_input("Last 3rd month Bill Amount  ", min_value=0 )
    bill_amt4 = st.number_input("Last 4th month Bill Amount  ", min_value=0 )
    bill_amt5 = st.number_input("Last 5th month Bill Amount  ", min_value=0 )
    bill_amt6 = st.number_input("Last 6th month Bill Amount  ", min_value=0 )

    pay_amt1 = st.number_input("Amount paid in Last Month  ", min_value=0 )
    pay_amt2 = st.number_input("Amount paid in Last 2nd month  ", min_value=0 )
    pay_amt3 = st.number_input("Amount paid in Last 3rd month  ", min_value=0 )
    pay_amt4 = st.number_input("Amount paid in Last 4th month  ", min_value=0 )
    pay_amt5 = st.number_input("Amount paid in Last 5th month  ", min_value=0 )
    pay_amt6 = st.number_input("Amount paid in Last 6th month  ", min_value=0 )


    if st.button("Predict"):
        features=[limit_bal,education,marriage,age,pay1,
        bill_amt1,bill_amt2,bill_amt3,bill_amt4,bill_amt5,bill_amt6,
        pay_amt1,pay_amt2,pay_amt3,pay_amt4,pay_amt5,pay_amt6]
        features = [np.array(features)]
        output = predict(features)
        st.success(output)


if __name__=='__main__':
    main()