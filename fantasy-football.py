import streamlit as st
import pandas as pd
import numpy as np

st.title('NFL Fantasy Football Stats Explorer')

st.markdown("""
This app performs simple webscraping of NFL Football fantasy players data from 1970 to 2022!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

st.sidebar.header('Filter by year, role and team')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1970,2023))))


@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/fantasy.htm#fantasy"
    # url = "https://www.pro-football-reference.com/years/1970/fantasy.htm#fantasy"

    # if skill == 'rushing':
    #     html = pd.read_html(url, header=1)
    # else:
    html = pd.read_html(url, header=1)
    df = html[0]
    playerstats = df.drop(['Rk','Fmb','FL','2PM','2PP'], axis=1)[0:100]
    return playerstats

playerstats = load_data(selected_year)

# Sidebar - Position selection
unique_pos = ['RB','QB','WR','TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Teams (clic X to exclude from search)', sorted_unique_team, sorted_unique_team)


# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.FantPos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
# st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Download player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806


