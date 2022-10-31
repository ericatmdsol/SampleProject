from sklearn.base import TransformerMixin
import numpy as np
import pandas as pd

class SampleTransformer(TransformerMixin):
    """ Centers the mean of all given columns to be 0
    Basically a simple transformation that has to memorize something with respect
    The underlying distribution (Most comments about what the class does should go here)
    """    
    def __init__(self, *args, **kwargs):
        self.means = None
    
    def fit(self, X: pd.DataFrame):
        self.columns = X.columns
        self.means = X.mean(axis=0)
        return self
    
    def transform(self, X: pd.DataFrame):
        return X - self.means

    def fit_transform(self, X: pd.DataFrame, y=None):
        self.fit(X)
        return self.transform(X)


