#--- Import modul yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#--- Inisiasi fungsi yang akan digunakan
def buat_rental_musim(df): #--- Fungsi untuk membuat list berdasarkan "season"
    rental_season=df.groupby(by="season").cnt.nunique().reset_index()
    rental_season.rename(columns={
        "cnt":"customer_count"
    }, inplace=True)
    return rental_season

def buat_rental_jam(df):#--- Fungsi untuk membuat list berdasarkan "hr"
    rental_jam=df.groupby(by="hr").cnt.nunique().reset_index()
    rental_jam.rename(columns={
        "cnt":"customer_count"
    }, inplace=True)
    return rental_jam

def buat_berdasarkan_cuaca(df):#--- Fungsi untuk membuat list berdasarkan "wheatersit"
    berdasarkan_cuaca=df.groupby(by="weathersit").agg({
    "instant": "nunique",
    "cnt": "sum"
    }).reset_index()
    return berdasarkan_cuaca

#--- Memanggil data
day_df=pd.read_csv("Dashboard\day_data.csv")
hour_df=pd.read_csv("Dashboard\hour_data.csv")

#--- Memanggil fungsi
season_favorite=buat_rental_musim(day_df)
hour_favorite=buat_rental_jam(hour_df)
weather_favorite=buat_berdasarkan_cuaca(day_df)

st.header('Dashboard Bike Sharing :bicyclist::star2:')#--- Membuat judul Dashboard
st.subheader("Statistic	:1234:")#--- Membuat sub judul Dashboard

#--- Membuat sidebar
with st.sidebar:
    st.subheader("Background")
    st.write(
        """
       
        Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
        back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
        back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
        over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
        environmental and health issues. 

        Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
        these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
        of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
        a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
        events in the city could be detected via monitoring these data.
        """
    )

col1,col2,col3=st.columns(3)#--- Membuat 3 kolom

#--- kolom jumlah rental
with col1:
    total_rent=day_df['cnt'].sum()
    st.metric("Total Rental",value=total_rent)

#--- jumlah rental pelanggan yang mempunyai member
with col2:
    member_rent=day_df['registered'].sum()
    st.metric("Member Rental", value=member_rent)

#--- jumlah rental pelanngan non member
with col3:
    casual_rent=day_df['casual'].sum()
    st.metric("Non Member Rental", value=casual_rent)

st.subheader("Customer's favorite season	:sunny:	:cloud:")

#--- membuat bar chart berdasarkan "seeson"
fig, ax=plt.subplots(figsize=(20,10))

colors_ = ["#D3D3D3",  "#D3D3D3","#72BCD4", "#D3D3D3"]

sns.barplot(
    y="customer_count",
    x="season",
    data=season_favorite.sort_values(by="customer_count", ascending=False),
    palette=colors_,
    ax=ax
)
ax.set_title("Number of Customer by Season", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

st.subheader("Description")
st.write(
    """
    #
    1: Springer
	2: Summer
	3: Fall
	4: Winter 
    """
)

st.subheader("Customer's favorite and hate hour	:smile::triumph:")

#--- membuat bar chart berdasarkan "hr"
fig, ax=plt.subplots(figsize=(20,10))
colors_ = ["#D3D3D3",  "#D3D3D3", "#D3D3D3","#D3D3D3",  "#D91656", "#D3D3D3",
           "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3",  "#D3D3D3", "#D3D3D3",
           "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3",  "#D3D3D3", "#72BCD4",
           "#D3D3D3","#D3D3D3"
]

sns.barplot(
    y="customer_count",
    x="hr",
    data=hour_favorite.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
ax.set_title("Number of Customer by hours", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)
