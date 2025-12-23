import pandas as pd
import numpy 

print(pd.__version__)

df = pd.read_csv("Exam_Score_Prediction.csv")

#Shows the initial data set
print("Initial dataset:")
print(df.head()) 

#mean of study hours
mean_studyhours = df['study_hours'].mean()
print("The average study hours is: ", mean_studyhours)

#sorts the Study Hours data in ascending order
sort_studyhours = df.sort_values(by='study_hours', ascending=True)

#study hours minimum and maximum value
minimum = df['study_hours'].min()
maximum = df['study_hours'].max()

print("The minimum study hours is: ", minimum, " The maximum study hours is: ", maximum)

#Outliers using the IQR method
Q1 = df['study_hours'].quantile(0.25)
Q3 = df['study_hours'].quantile(0.75)
IQR = Q3 - Q1

print("The first quartile is: ", Q1)
print("The third quartile is: ", Q3)
print("The interquartile is: ", IQR)

lower_bound = Q1 - (1.5*IQR)
upper_bound = Q3 + (1.5*IQR)

outliers = df[(df['study_hours'] < lower_bound) | (df['study_hours'] > upper_bound)]
print('The outliers are in rows: ', outliers)

#mean of exam_score
mean_examscore = df['exam_score'].mean()
print("The average exam score is: ", mean_examscore)

#find correlation between examscore and study hours
studyhoursXexamscore_corr = df['study_hours'].corr(df['exam_score'])
print("The correlation between study hours and exam score is: ", studyhoursXexamscore_corr)

