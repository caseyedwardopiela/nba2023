import streamlit as st
import pandas as pd
#import base64
#import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('v1_2023_predictions.csv').drop(['Unnamed: 0'], axis = 1).sort_values('Fantasy_Score', ascending = False)
 
st.title('2022-2023 NBA Fantasy Score Predictions')

st.markdown("""
This app pulls historical data from Basketball-Reference.com, including college, international, and regular season stats. After compiling everything,
it runs a combination of several machine learning algorithms to predict all of the traditional stats for each player this coming season. 

##### Last Updated: 20 September 2022
""")

st.sidebar.header('User Input Selection')

# Sidebar - Team Selection
sorted_team_unique = list(df['Player_Team'].unique())
sorted_team_unique = sorted(sorted_team_unique)
sorted_position_unique.insert(0,'All Teams')
selected_team = st.sidebar.selectbox('Which team would you like to see?',
    sorted_team_unique)

# Sidebar - Position Selection
sorted_position_unique = list(df['Player_Position'].unique())
sorted_position_unique = sorted(sorted_position_unique)
sorted_position_unique.insert(0,'All Positions')
selected_position = st.sidebar.selectbox('Which position would you like to see?',
    sorted_position_unique) 

# Filtering data - Team
if selected_team == 'All Teams':
    df_selected_team = df
else:
    df_selected_team = df[df['Player_Team'] == selected_team]
  
# Filtering data - Position
if selected_position == 'All Positions':
    df_selected_team = df_selected_team
else:
    df_selected_team = df_selected_team[df_selected_team['Player_Position'] == selected_position]


st.header('Displaying Player(s)...')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)
