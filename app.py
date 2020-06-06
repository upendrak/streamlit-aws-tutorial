import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

st.markdown("<h1 style='text-align: left; color: green;'>Club and Nationality App</h1>", unsafe_allow_html=True)
st.write("")

@st.cache
def load_data():
	df = pd.read_csv("football_data.csv")
	df.drop(['Unnamed: 0', 'ID'], axis = 1, inplace=True)
	return df

if st.checkbox("Select this checkbox to look at the data"):
	st.write(load_data())

df = load_data()

clubs = st.sidebar.multiselect('Select Players for clubs', df['Club'].unique())
nationalities = st.sidebar.multiselect('Select Players from Nationalities', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]


if clubs and nationalities is not None:
	if len(new_df) != 0:
		st.write("Summary of the selected combination of club and nationality:")
		st.write(new_df)
		st.write("Simple chart between player age and overall age of all the players")
		fig = px.scatter(new_df, x ='Overall',y='Age', color='Name')
		st.plotly_chart(fig)
	else:
		# st.markdown("### No player with that combination was found!!!")
		st.markdown(
		"""

		This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities

		👈 Select one or more clubs and nationalities

		"""
		)

