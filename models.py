import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

from utils import Utils

class Models:

    def __init__(self):
        self.reg = {
            'SVC' : SVC(),
            'GRADIENT' : GradientBoostingClassifier()
        }

        self.params = {
           'SVC' : {
               'kernel' : ['linear', 'poly', 'rbf'],
               'gamma' : ['auto', 'scale'],
               'C' : [1,5,10]
           }, 'GRADIENT' : {
               'loss' : ['deviance', 'exponential'],
               'learning_rate' : [0.01, 0.05, 0.1]
           }
        }

    def grid_training(self, X,y):

        best_score = 999
        best_model = None

        for name, reg in self.reg.items():

            grid_reg = GridSearchCV(reg, self.params[name], cv=3).fit(X, y.values.ravel())
            score = np.abs(grid_reg.best_score_)

            if score < best_score:
                best_score = score
                best_model = grid_reg.best_estimator_
        

        utils = Utils()
        utils.model_export(best_model, best_score)