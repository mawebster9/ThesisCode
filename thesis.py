# Michaela Webster's Thesis Project #
""" This project aims to try to predict the outcome of security clearance appeals cases """

#use this link for scikit learn help: https://www.ritchieng.com/pandas-scikit-learn/

# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals

# imports
import os
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex

#open drugs_query.csv as pandas dataframe
path_to_file = "C:\\Users\\maweb\\Documents\\ThesisCode\\drugs_query.csv"
data = pd.read_csv(path_to_file, encoding='latin-1')

#print bar graph of drugs yes/no vs denied yes/no
print (data.groupby(['Drugs', 'Denied']).size())

#print bar graph to show drugs/denied


# set the featured columns for X (Drugs)
feature_cols = ['Drugs']
# you want all rows, and the feature_cols' columns
X = data.loc[:, feature_cols]
# now we want to create our response vector
y = data.Denied


# START DOING MACHINE LEARNING STUFF
# 1. import
from sklearn.linear_model import LogisticRegression
# 2. instantiate model
logreg = LogisticRegression(penalty='l1',dual=False,max_iter=110, solver='liblinear')
# 3. fit 
logreg.fit(X, y)


# FOR TEST DATA
#open drugs_test.csv as pandas dataframe
path_to_file = "C:\\Users\\maweb\\Documents\\ThesisCode\\drugs_test.csv"
data2 = pd.read_csv(path_to_file, encoding='latin-1')
X_new = data.loc[:, feature_cols]
new_pred_class = logreg.predict(X_new)

#SAVE DATAFRAME TO CSV
# pandas would align them next to each other
# to ensure the first column is PassengerId, use .set_index
#drug_data = pd.DataFrame({'Drugs':test.PassengerId, 'Denied':new_pred_class}).set_index('Drugs')
#drug_data.to_csv('drug_df.csv')

