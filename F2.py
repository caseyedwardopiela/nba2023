import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('v1_2023_predictions.csv').drop(['Unnamed: 0'], axis = 1).sort_values('Fantasy Score', ascending = False)
 
st.title('2022-2023 NBA Fantasy Score Predictions')

st.markdown("""
This app pulls historical data from Basketball-Reference.com, including college, international, and regular season stats. After compiling everything,
it runs a combination of several machine learning algorithms to predict all of the traditional stats for each player this coming season. 
##### Last Updated: 20 September 2022
""")



st.header('Displaying Player(s)...')
st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
st.dataframe(df)
