import pandas as pd
import streamlit as st
import glob
from PIL import Image

st.title('Ranking')


def load_image(logo, number):
    #replace underscores with spaces
    logo = logo.replace(' ', '_')
    image = Image.open(f"images/{logo}.png")
    new_image = image.resize((500, 500))
    st.image(new_image)
    #replce spaces with underscores
    logo = logo.replace('_', ' ')
    st.write(f"{number} - {logo}")
#load_image("Air_Force")

#Load in all the teams, do this by reading in the CSV file and making it so each row is a team
teams_df = pd.read_csv('teams.csv')

# Extract the team names into a list, make any spaces in the team names underscores
#team_names = teams_df['team_name'].str.replace(' ', '_').tolist()
team_names = teams_df['team_name'].tolist()

ranked_teams = st.sidebar.radio("How many teams would you like to rank?", [5, 10, 12, 25])

col1, col2, col3, col4, col5 = st.columns(5)

def rank_team(number, collumn):
    ranking = st.sidebar.selectbox(f'Ranking {number}', [''] + team_names)
    if ranking != '':
        with collumn:
            load_image(ranking, number)
        #remove the team from the list
        #replace underscores with spaces
        team_names.remove(ranking)

if ranked_teams == 5:
    rank_team(1, col1)
    rank_team(2, col2)
    rank_team(3, col3)
    rank_team(4, col4)
    rank_team(5, col5)
elif ranked_teams == 10:
    rank_team(1, col1)
    rank_team(2, col2)
    rank_team(3, col3)
    rank_team(4, col4)
    rank_team(5, col5)
    rank_team(6, col1)
    rank_team(7, col2)
    rank_team(8, col3)
    rank_team(9, col4)
    rank_team(10, col5)
elif ranked_teams == 12:
    rank_team(1, col1)
    rank_team(2, col2)
    rank_team(3, col3)
    rank_team(4, col4)
    rank_team(5, col5)
    rank_team(6, col1)
    rank_team(7, col2)
    rank_team(8, col3)
    rank_team(9, col4)
    rank_team(10, col5)
    rank_team(11, col1)
    rank_team(12, col2)
elif ranked_teams == 25:
    rank_team(1, col1)
    rank_team(2, col2)
    rank_team(3, col3)
    rank_team(4, col4)
    rank_team(5, col5)
    rank_team(6, col1)
    rank_team(7, col2)
    rank_team(8, col3)
    rank_team(9, col4)
    rank_team(10, col5)
    rank_team(11, col1)
    rank_team(12, col2)
    rank_team(13, col3)
    rank_team(14, col4)
    rank_team(15, col5)
    rank_team(16, col1)
    rank_team(17, col2)
    rank_team(18, col3)
    rank_team(19, col4)
    rank_team(20, col5)
    rank_team(21, col1)
    rank_team(22, col2)
    rank_team(23, col3)
    rank_team(24, col4)
    rank_team(25, col5)