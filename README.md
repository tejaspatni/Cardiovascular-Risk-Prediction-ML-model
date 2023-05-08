# Cardiovascular-Risk-Prediction-ML-model

## Introduction
Cardiovascular diseases (CVDs) are a group of disorders of the heart and blood vessels and include coronary heart disease, cerebrovascular disease, rheumatic heart disease and other conditions.High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease.There were more than 523.2 million cases of cardiovascular disease in 2019, an increase of 26.6% compared with 2010.

## Problem Statement
The data is from an ongoing cardiovascular study on residents of the town of framingham, Massachusetts. The classification goal is to predict whether the patient has a risk of 10 year coronary heart disease(CHD). The dataset provides the patient's information. It includes over 4000 records and 15 attributes. Each attribute is a potential risk factor. There are both demographic, behavoural, and medical risk factor.

## Insights
1. Patients having high colestrol has 18% chance of risk than borderline(14%) and normal(10%)
2. Patients having hypertension 25% chance of risk than prehypertension(14%) and normal(10%)
3. Patients being Underweight and obese has 19% chances of risk than overweight(16%) and healthy(12%)
4. Patients Having heart rate being normal and high has high chance than low.
5. Patient being diabetic has 47% of chance of risk than prediabetic(17%) and normal(14%)
6. Adult above 60 has high chance of risk.
7. Patients smoking large number of cigrettes per day has high on risk


## Variables Description

### Demographic:

1. Sex: male or female ("M" or "F")
2. Age: Age of the patient (Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
3. Education: The level of education of the patient (categorical values - 1,2,3,4)

### Behavioral:

1. is_smoking: whether or not the patient is a current smoker ("YES" or "NO")
2. Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes)

### Medical (history):

1. BP Meds: whether or not the patient was on blood pressure medication (Nominal)
2. Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)
3. Prevalent Hyp: whether or not the patient was hypertensive (Nominal)
4. Diabetes: whether or not the patient had diabetes (Nominal)

### Medical (current):

1. Tot Chol: total cholesterol level (Continuous)
2. Sys BP: systolic blood pressure (Continuous)
3. Dia BP: diastolic blood pressure (Continuous)
4. BMI: Body Mass Index (Continuous)
5. Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
6. Glucose: glucose level (Continuous)

### Predict variable (desired target):

  10-year risk of coronary heart disease CHD(binary: “1”, means “Yes”, “0” means “No”)


## Models

**** Comparison of  Models ****

|          Model           | Test Accuracy | Precision | Recall | F1_score |
|--------------------------|---------------|-----------|--------|----------|
|   Logistic regression    |      0.64     |    0.64   |  0.23  |   0.34   |
| Decision Tree Classifier |      0.38     |    0.18   |  0.9   |   0.3    |
| Random Forest Classifier |      0.53     |    0.21   |  0.79  |   0.33   |
|   K-Nearest Neighbours   |      0.55     |    0.2    |  0.69  |   0.31   |
|   Gaussian Naive Bayes   |      0.81     |    0.29   |  0.32  |   0.3    |
|    XGBoost Classifier    |      0.29     |    0.16   |  0.88  |   0.27   |
|  Support Vector Machine  |      0.63     |    0.7    |  0.24  |   0.36   |

We can Choose Decision Tree classifier from the above model because it has the highest recall value among other. A recall score of 0.90 indicates that out of 100 individuals with the illness, our model will be able to classify 90 as high risk patients, while the remaining 10 will be misclassified. Comparing the other models, this has the best recall rate and able to perform well.


## Conclusion
1. We trained 7 Machine Learning models using the training dataset, and hyperparameter tuning was used in some models to improve the model performance.

2. To build the models, missing values were handled, feature engineering and feature selection was performed, and the training dataset was oversampled using SMOTE to reduce bias on one outcome.

3. Recall was chosen as the model evaluation metric because it was very important that we reduce the false negatives.

4. It is critical that the model we develop has a high recall score. It is OK if the model incorrectly identifies a healthy patient as a high risk patient because it will not result in death, but if a high risk patient is incorrectly labelled as healthy, it may result in fatality.

5. Predicting the risk of coronary heart disease is critical for reducing fatalities caused by this illness. We can avert deaths by taking the required medications and precautions if we can foresee the danger of this sickness ahead of time.

6. As age increases the risk of getting diagnosed with heart disease also increases. Cigarette consumption is also a major factor that causes CHDs.

7. Patients having Diabetes and cholesterol problems show a higher risk of CHDs. Patients with a history of “strokes” have a higher chance of developing CHDs.

8. Finally we can say that, Decision tree Classifier has performed best among all the models with 90% Recall. It is by far the highest score we have achieved.So,It's safe to say that Decision tree Classifier provides an optimal solution to our problem.


Link : https://tejaspatni-cardiovascular-risk-prediction-ml-model-app-iqxzpv.streamlit.app/
