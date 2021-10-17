import pandas as pd
from sklearn.model_selection import cross_val_score
import numpy as np

# our 5 classification models
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold

import yaml


def replace_true_with_1(df: pd.DataFrame):
    for i in (df.columns.tolist()):
        df[i] = df[i].replace(True,1)


def print_scoring_metrics(clf: LogisticRegression, X: np.ndarray, y: np.ndarray):
    classifiers = [RandomForestClassifier(n_estimators=5, random_state=42), GaussianNB(), LogisticRegression(solver='liblinear'), DecisionTreeClassifier(criterion='gini'), KNeighborsClassifier(n_neighbors=6)]
    clf_names = ['RandomForest','GausianNB','LogisticRegression','DecisionTreeClassRegressor', 'KNeighbors']
    metric_names = ['roc_auc','f1','accuracy','precision','recall']

    scv = StratifiedKFold(n_splits=20)

    scores_df = pd.DataFrame(index=metric_names,columns=clf_names)
    clf_scores = []
    for clf, name in zip(classifiers, clf_names):
        print('-----------------------------------------------------------------------------------------------------------')
        print('Classifier: ',clf)
        print('')
        print("Scoring Metrics: ")
        for metric in metric_names:
            score = cross_val_score(clf,X,y,scoring=metric, cv=scv).mean()
            clf_scores.append(score)
            print('\t*',metric,'score: ', score)
        scores_df[name] = clf_scores
        clf_scores = []
        

def load_conf_file(config_file):
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        csv_conf = config["csv"]
        params_conf = config["params"]
    return csv_conf, params_conf
        

csv_conf, params_conf = load_conf_file("config.yaml")
