# Introduction :bulb:

This is a simple model that uses synthetic data to learn how quantitative variables such as
study hours, sleep hours, class attendance, and age impact the final exam score of a student
a day prior to their final exam. 

# Brief Structure Description :file_folder:

The model utilizes Scikit-learn library -- LinearRegression -- to create a machine learning model.
Given that we have four quantitative variables that may affect academic result, I used a multiple
linear regression model to account for al the variables and it's effects on the result. 

# Model Limitations :collision:

Considering that the model uses synthetic data, it's source may not represent the population. However, with
thorough observation of the raw dataset, I believe that it is close enough to mimic the population data.
Another limitation is the training limit of the model. Since the model is stricted by the maximum and the minimums
of the dataset, extrapolation results are unrealistic and may not give an acceptable result. Therefore, relying 
on the model to provide a guarantee result is not plausible. Though, the model is sufficient enough to provide a
result that can serve as a reference to asses ones academic positioning as long as new data provided is in a realistic
manner and is similar to the training data set. Lastly, the model does not take into consideration the qualitative 
variable of the dataset. I believe that academic strands, individual strengths, and other social factors 
can impact the results of a final exam, however, due to its social factor, it is difficult to represent in a mathematical perspective. As a result, the model will not reflect the impact of the quantitative data. 

