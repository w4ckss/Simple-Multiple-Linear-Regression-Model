import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

#Linear Regression
X = df['study_hours']
Y = df['exam_score']

m, b = np.polyfit(X, Y, 1)

regression_line = m*X + b

plt.scatter(X, Y)
plt.plot(X, regression_line)
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Study Hours and Exam Scores correlation')
plt.plot(X, regression_line, label='Line of Best Fit')
#plt.show()

predict_hours = int(input("How many hours will you be studying? "))

predict_score = round(m*predict_hours + b, 2)

print("If you study for ", predict_hours, " hours, then, on average, you can get an estimated score of ", predict_score, 'percent')

if predict_hours > mean_studyhours:
    print("You study more than the average study hours")
else:
    print("You study less than the average hours")

if predict_score > mean_examscore:
    print("Your score is higher than the average")
else:
    print("Your score is lower than the average")

