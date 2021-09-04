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
    compounding_frequency = st.selectbox('How often will the interest be compounded?', ( 'Monthly', 'Annually'))
with Timecolumn:
    time_to_invest = st.number_input("Enter the time to invest in months: ", min_value=0.0, format='%f')

def calculate_compound_interest(principal, rate, compounding_frequency, time):
    if compounding_frequency == "Monthly":
        frequency = 12
    elif compounding_frequency == "Annually":
        frequency = 1
    
    #convert interest rate to percentage
    rate = rate/100
    #convert time to years
    time = time/12

    amount = principal * pow( 1+(rate/frequency), (frequency*time))  
    return amount

total_amount = calculate_compound_interest(principal,interest_rate,compounding_frequency,time_to_invest)


#print("{:,}".format(total_amount))
st.header("**Returns**")
st.subheader("Total Amount: " +"Ksh."+ "{:,.2f}".format(total_amount))
st.subheader("Initial Amount: " +"Ksh."+ "{:,.2f}".format(principal))
st.subheader("Total Interest: " +"Ksh."+ "{:,.2f}".format(total_amount-principal))
