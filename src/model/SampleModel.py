# we're just wrapping a normal ML algorithm for illustrative purposes. 
from sklearn.base import RegressorMixin, BaseEstimator
import numpy as np
import pandas as pd
class SampleModel(BaseEstimator, RegressorMixin):
    """As an illustrative example, i'm rewriting a custom
       least squares estimator to illustrate the concept of wrapping
       custom ML functions
    """    
    def __init__(self):
        pass

    def fit(self, X: pd.DataFrame, Y: pd.DataFrame):
        local_X = X.to_numpy()
        local_Y = Y.to_numpy()
        local_X = np.c_[local_X, np.ones(local_X.shape[0])]  # add bias term
        self.beta_hat = np.linalg.lstsq(local_X, local_Y, rcond=None)[0]
        return self

    def predict(self, X: pd.DataFrame):
        local_X = X.to_numpy()
        local_X = np.c_[local_X, np.ones(local_X.shape[0])] 
        Z = np.sum(local_X * self.beta_hat[:,0], axis=1)
        return(Z)     
    
    def fit_transform(self, X: pd.DataFrame, Y: pd.DataFrame):
        self.fit(X, Y)
        return(self.predict(X))
    
