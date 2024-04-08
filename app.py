import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('model.joblib')
st.title('Etheriom Fraud Detection in 2024')
st.write("""### We need some information to detect Ether fraud""")

column = ['Avg min between sent tnx', 'Avg min between received tnx',
       'Time Diff between first and last (Mins)', 'Sent tnx', 'Received Tnx',
       'Number of Created Contracts', 'max value received ',
       'avg val received', 'avg val sent', 'total Ether sent',
       'total ether balance', ' ERC20 total Ether received',
       ' ERC20 total ether sent', ' ERC20 total Ether sent contract',
       ' ERC20 uniq sent addr', ' ERC20 uniq rec token name']

avg_min_between_sent_tnx = st.slider("Avg min between sent tnx", 0, 1000, 3)
avg_min_between_received_tnx = st.slider("Avg min between received tnx", 0, 1000, 3)
time_diff_between_first_and_last = st.slider("Time Diff between first and last (Mins)", 0, 1000, 3)
sent_tnx = st.slider("Sent tnx", 0, 1000, 3)
received_tnx = st.slider("Received Tnx", 0, 1000, 3)
num_created_contracts = st.slider("Number of Created Contracts", 0, 1000, 3)
max_value_received = st.slider("max value received", 0, 1000, 3)
avg_val_received = st.slider("avg val received", 0, 1000, 3)
avg_val_sent = st.slider("avg val sent", 0, 1000, 3)
total_ether_sent = st.slider("total Ether sent", 0, 1000, 3)
total_ether_balance = st.slider("total ether balance", 0, 1000, 3)
erc20_total_ether_received = st.slider("ERC20 total Ether received", 0, 1000, 3)
erc20_total_ether_sent = st.slider("ERC20 total ether sent", 0, 1000, 3)
erc20_total_ether_sent_contract = st.slider("ERC20 total Ether sent contract", 0, 1000, 3)
erc20_uniq_sent_addr = st.slider("ERC20 uniq sent addr", 0, 1000, 3)
erc20_uniq_rec_token_name = st.slider("ERC20 uniq rec token name", 0, 1000, 3)

def predict(): 
    row = np.array([avg_min_between_sent_tnx, avg_min_between_received_tnx, time_diff_between_first_and_last, sent_tnx, received_tnx, num_created_contracts, max_value_received, avg_val_received, avg_val_sent, total_ether_sent, total_ether_balance, erc20_total_ether_received, erc20_total_ether_sent, erc20_total_ether_sent_contract, erc20_uniq_sent_addr, erc20_uniq_rec_token_name]) 
    X = pd.DataFrame([row], columns = column)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('Cheating is required :thumbsup:')
    else: 
        st.error('No cheating required :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)