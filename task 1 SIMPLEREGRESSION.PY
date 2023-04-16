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

#now Data visualization step using matplotlibz
#scatter plot
plt.scatter(data["hours"],data["scores"])
plt.xlabel("number of hours studied')
plt.ylabel("percentage")
       y=data["scores"]
           x=data.drop["score"]
           
#now machine learning model making step
           from sklearn.linear_model import LinearRegression
           model=LinearRegression()
           
           #now import train test spilt  odel
           from sklearn.model_selection import train_test_split
           x_train,x_test,y_train,y_test=train_test_split(x,y,tset_size=0.3)
           x_train.size
           x_test.size
           
           #now fitting our trainig data in our machine learing model
           model.fit(x_train,y_train)
           
           #predicting values
           y_test_model=model.predict(x_test)
           print(y_test_model)
           
           #now check for scores of our model
           acc_train=model.score(x_train,y_train)
           acc_test=model.score(x_text,y_test)
           print(acc_test)
           print(acc_train)
           
           #now cost function check
           from sklearn.metices import mean_squared_error
           rmse_train=np.sqrt(mean_squared_error(y_test,y_test_model)
            print("accuracy of our model is "  acc_test)  
             print("root mean squared error is "rmse_train)
                              
            #predicting using our model
             #create a scatter plot and regression line
              plt.scatter(x_test,y_test,label="actual values",color="blue")
              plt.plot(x_train,y_train_model,label="predicted values",color="green")
             plt.xlabel("hours')
              plt.y_label("scores")
               plt.title("hours vs scores")
                        plt.grid()
                        plt.legend()
                        
                        
                        
                        
                        result=model.predict(9)
                        
                        
                        
                        #conclusion 
                        #the final takeaway of this simple projest is the working of the linear regression model on the datasetand understanding thier parameters
                        
          
           

