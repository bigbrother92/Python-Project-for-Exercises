# To import required libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

# to read the file
df = pd.read_csv("googleplaystore.csv")

#To check dataset
df.info()

# To check column and row numbers of dataset
df.shape

#To calculate summary statistics for numerical columns
df.describe

#To show every values in columns and rows in the df
z = df.values

#To check columns of the df
df.columns

#To check the index of the df
df.index

#To check data types of a dataframe
df.dtypes

#to sort values by their Size(ascending = increasing, descending = decreasing)
df1= df.sort_values("Size",ascending=False)

#Subsetting the Rating column whose ratings are greater than 3
df2 = df["Rating"]
df2 = df[df["Rating"]>3]
df2_greater = df2[df2["Rating"]>3]
df2 = df[df["Rating"]>3]
df2.dtype
#Adding a new column called Rating_Half
df["Rating_Half"] = df["Rating"] / 2

#SUMMARY STATISTICS
df["Rating"].mean()
df["Rating"].median()
df["Rating"].mod()
df["Rating"].min()

#To get the 30th percentile for column
def pct30(column):
    return column.quantile(0.3)
df["Rating"].agg(pct30)

#DATA CLEANING PROCESS
#Removing Symbols from the values
df["Size"] = df["Size"].str.strip("M")

#To change the datatype of the chosen column
df["Size"] = df["Size"].astype("float")

df.dtypes