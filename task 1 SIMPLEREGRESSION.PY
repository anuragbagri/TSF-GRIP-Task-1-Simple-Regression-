#the sparks foundation:Data science and Business analytics Internship
#
#Task 1:Prediction using Supervised Machine Learning Alogrithms
# 
#Problem statement:Predict percentage of student based on numbers  of hours studied
#AUTHOR:Anurag Bagri

#importing required libraries
import pandasd as pd
import numpy as np
#for data visualization ,
import matplotlib.pyplot as plt
%matplotlib inline

#reading data 
data=pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
data.head(10)

#Exploring the data
data.shape()

data.columns

#cheching the columns and rows in data
data.info()

#checking the columns data types 
data.dtypes

#now data-preprocessing steps 
#checking for null values in data ,columnwise
data.isna().sum()

#replacing null values with means values of the particular column
mean_values=data["scores"].mean()
data["scores"].replace(np.nan,mean_values,inplace=True)

