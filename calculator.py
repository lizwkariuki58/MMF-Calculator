import streamlit as st
import plotly.graph_objects as go
import numpy as np 

#set name of page
st.set_page_config(
    page_title="MMF Compound Interest Calculator")
#header 1
st.title("MMF Compound Interest Calculator")

st.header("**Investing a Lumpsum**")
#define columns
Principalcolumn, Interestcolumn, Frequencycolumn, Timecolumn = st.columns(4)

#get input from user
with Principalcolumn:
    principal = st.number_input("Enter amount to invest (Ksh): ", min_value=0.0, format='%f')
with Interestcolumn:
    interest_rate = st.number_input("Enter the interest rate p/a(%): ", min_value=0.0, format='%f')
with Frequencycolumn:
    compounding_frequency = st.selectbox('How often will the interest be compounded?', ('Daily', 'Monthly', 'Annually'))
with Timecolumn:
    time_to_invest = st.number_input("Enter the time to invest in months: ", min_value=0.0, format='%f')

frequency = 1

#formula to calculate compound interest
def compound_interest(principle, rate, time):
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    return CI

returned_interest = compound_interest(principal, interest_rate, frequency)

st.header("**Returns**")
st.subheader("Total Amount: " + str(principal+returned_interest))
st.subheader("Initial Amount: " + str(principal))
st.subheader("Total Interest: " + str(returned_interest))