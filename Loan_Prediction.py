# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AI3oNV3h1KFMmUqfGV2UBnSjIoSpNvFH
"""

# Commented out IPython magic to ensure Python compatibility.
# import libraries
# %matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# load the  dataset
loan = pd.read_excel("/content/drive/MyDrive/dataset/loan-predictionUC.csv .xlsx")

# take a look at the top 5 rows of the train set, notice the column "Loan_Status"
loan.head()

loan.shape

loan.dtypes

# frequency table of a variable will give us the count of each category in that variable
loan['Loan_Status'].value_counts()

# percentage distribution can be calculated by setting the normalize=True to show proportions instead of number
loan['Loan_Status'].value_counts(normalize=True)

# bar plot to visualize the frequency
loan['Loan_Status'].value_counts().plot.bar()

# Visualizing categorical features
# plt.figure(1)
plt.subplot(231)
loan['Gender'].value_counts(normalize=True).plot.bar(figsize=(20,10), title= 'Gender')

plt.subplot(232)
loan['Married'].value_counts(normalize=True).plot.bar(title= 'Married')

plt.subplot(233)
loan['Self_Employed'].value_counts(normalize=True).plot.bar(title= 'Self_Employed')

plt.subplot(234)
loan['Credit_History'].value_counts(normalize=True).plot.bar(title= 'Credit_History')

plt.subplot(235)
loan['Education'].value_counts(normalize=True).plot.bar(title= 'Education')

plt.show()

# Visualizing remaining categorical features
# plt.figure(1)
plt.subplot(121)
loan['Dependents'].value_counts(normalize=True).plot.bar(figsize=(12,4), title= 'Dependents')

plt.subplot(122)
loan['Property_Area'].value_counts(normalize=True).plot.bar(title= 'Property_Area')

plt.show()

# Visualizing ApplicantIncome
# plt.figure(1)
plt.subplot(121)
sns.distplot(loan['ApplicantIncome']);

plt.subplot(122)
loan['ApplicantIncome'].plot.box(figsize=(16,5))

plt.show()

loan.boxplot(column='ApplicantIncome', by = 'Education')
plt.suptitle("")

# plt.figure(1)
plt.subplot(121)
sns.distplot(loan['CoapplicantIncome']);

plt.subplot(122)
loan['CoapplicantIncome'].plot.box(figsize=(16,5))

plt.show()

# plt.figure(1)
plt.subplot(121)
df=loan.dropna()
sns.distplot(df['LoanAmount']);

plt.subplot(122)
loan['LoanAmount'].plot.box(figsize=(16,5))

plt.show()

# frequency table of a variable will give us the count of each category in that variable
loan['Loan_Amount_Term'].value_counts()

# plot bar chart
loan['Loan_Amount_Term'].value_counts(normalize=True).plot.bar(title= 'Loan_Amount_Term')

print(pd.crosstab(loan['Gender'],loan['Loan_Status']))

Gender = pd.crosstab(loan['Gender'],loan['Loan_Status'])
Gender.div(Gender.sum(1).astype(float), axis = 0).plot(kind="bar", stacked=True, figsize=(4,4))
plt.xlabel('Gender')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Married'],loan['Loan_Status']))

Married = pd.crosstab(loan['Married'],loan['Loan_Status'])
Married.div(Married.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))
plt.xlabel('Married')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Dependents'],loan['Loan_Status']))

Dependents=pd.crosstab(loan['Dependents'],loan['Loan_Status'])
Dependents.div(Dependents.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.xlabel('Dependents')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Education'],loan['Loan_Status']))

Education=pd.crosstab(loan['Education'],loan['Loan_Status'])
Education.div(Education.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))
plt.xlabel('Education')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Self_Employed'],loan['Loan_Status']))

Self_Employed=pd.crosstab(loan['Self_Employed'],loan['Loan_Status'])
Self_Employed.div(Self_Employed.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))
plt.xlabel('Self_Employed')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Credit_History'],loan['Loan_Status']))

Credit_History=pd.crosstab(loan['Credit_History'],loan['Loan_Status'])
Credit_History.div(Credit_History.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))
plt.xlabel('Credit_History')
p = plt.ylabel('Percentage')

print(pd.crosstab(loan['Property_Area'],loan['Loan_Status']))

Property_Area=pd.crosstab(loan['Property_Area'],loan['Loan_Status'])
Property_Area.div(Property_Area.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
plt.xlabel('Property_Area')
P = plt.ylabel('Percentage')

# check for missing values
loan.isnull().sum()

# replace missing values with the mode
loan['Gender'].fillna(loan['Gender'].mode()[0], inplace=True)
loan['Married'].fillna(loan['Married'].mode()[0], inplace=True)
loan['Dependents'].fillna(loan['Dependents'].mode()[0], inplace=True)
loan['Self_Employed'].fillna(loan['Self_Employed'].mode()[0], inplace=True)
loan['Credit_History'].fillna(loan['Credit_History'].mode()[0], inplace=True)

loan['Loan_Amount_Term'].value_counts()

# replace missing value with the mode
loan['Loan_Amount_Term'].fillna(loan['Loan_Amount_Term'].mode()[0], inplace=True)

# replace missing values with the median value due to outliers
loan['LoanAmount'].fillna(loan['LoanAmount'].median(), inplace=True)

# check whether all the missing values are filled in the Train dataset
loan.isnull().sum()

train =loan.iloc[1:300]

train

test=loan.iloc[300:614]

test

# drop "Loan_Status" and assign it to target variable
X = loan.drop('Loan_Status', axis=1)
y = loan['Loan_Status']

# adding dummies to the dataset
X = pd.get_dummies(X)
train = pd.get_dummies(train)
test = pd.get_dummies(test)

X.shape,train.shape, test.shape

X.head()

# import library
from sklearn.model_selection import train_test_split

# split the data into train and cross validation set
x_train, x_cv, y_train, y_cv = train_test_split(X, y, test_size=0.3, random_state=0)

# take a look at the dimension of the data
x_train.shape, x_cv.shape, y_train.shape, y_cv.shape

# import libraries
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# fit the model
model = LogisticRegression()
model.fit(x_train, y_train)

# make prediction
pred_cv = model.predict(x_cv)

# calculate accuracy score
accuracy_score(y_cv, pred_cv)

# import confusion_matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_cv, pred_cv)
print(cm)

# f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(cm, annot=True, fmt="d")
plt.title('Confusion matrix of the classifier')
plt.xlabel('Predicted')
plt.ylabel('True')

# import classification_report
from sklearn.metrics import classification_report
print(classification_report(y_cv, pred_cv))