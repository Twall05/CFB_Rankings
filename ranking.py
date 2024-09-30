import pandas as pd
import streamlit as st
from PIL import Image
import datetime
import os

st.title('Ranking')


def load_image(logo, number):
    logo = logo.replace(' ', '_')
    image = Image.open(f"images/{logo}.png")
    new_image = image.resize((250, 250))
    st.image(new_image)
    logo = logo.replace('_', ' ')
    st.write(f"{number} - {logo}")


# Load in all the teams
teams_df = pd.read_csv('teams.csv')
team_names = teams_df['team_name'].tolist()

number_of_teams = len(team_names)
ranked_teams = st.sidebar.radio("How many teams would you like to rank?", [5, 10, 12, 25])

col1, col2, col3, col4, col5 = st.columns(5)

# Create a list to hold selected team names
selected_teams = []

def rank_team(number, column):
    ranking = st.sidebar.selectbox(f'Ranking {number}', [''] + team_names)
    if ranking != '':
        with column:
            load_image(ranking, number)
        # Remove the selected team from the list
        team_names.remove(ranking)
        selected_teams.append(ranking)


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

# Command that gives exact date and time
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Add a condition to enable the submit button only if the correct number of teams is selected
if len(selected_teams) == ranked_teams:
    if st.button("Submit"):
        st.success(f"Successfully ranked {ranked_teams} teams!")
        
        # Save the selected teams to a DataFrame
        selected_teams_df = pd.DataFrame(selected_teams, columns=['team_name'])

        # Specify the directory
        directory = "C:\\Users\\taylo\\CFB_ranking\\Data"
        
        # Make sure the directory exists
        os.makedirs(directory, exist_ok=True)
        
        # Create the full file path
        file_path = os.path.join(directory, f"{ranked_teams}_teams_ranked_teams_{now}.csv")

        # Save the DataFrame to the specified directory
        selected_teams_df.to_csv(file_path, index=False)

        # Convert the DataFrame to CSV format in memory for download
        csv = selected_teams_df.to_csv(index=False).encode('utf-8')
        
        # Create a download button to download the CSV file
        st.download_button(
            label="Download Ranked Teams CSV",
            data=csv,
            file_name=f"{ranked_teams}_teams_ranked_teams_{now}.csv",
            mime="text/csv"
        )
else:
    st.warning(f"Please rank exactly {ranked_teams} teams.")
