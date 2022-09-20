import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('v1_2023_predictions.csv').drop(['Unnamed: 0'], axis = 1)

st.title('2022-2023 NBA Fantasy Score Predictions')

st.markdown("""
This app pulls historical data from Basketball-Reference.com, including college, international, and regular season stats. After compiling everything,
it runs a combination of several machine learning algorithms to predict all of the traditional stats for each player this coming season.
""")

st.sidebar.header('User Input Features')

# Sidebar - Team Selection
sorted_team_unique = list(df['Player_Team'].unique())
sorted_team_unique.append('!ALL')
sorted_team_unique = sorted(sorted_team_unique)
selected_team = st.sidebar.selectbox('Team', sorted_team_unique, sorted_team_unique)

# Filtering data
if selected_team != '!All':
  df_selected_team = df[df['Player_Team'].isin(selected_team)]
else:
  df_selected_team = df[~df['Player_Team'].isin(['no-team'])]

st.header('Display Players on Selected Team')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)
