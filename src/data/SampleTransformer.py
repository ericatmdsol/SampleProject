from sklearn.base import TransformerMixin
import numpy as np


class SampleTransformer(TransformerMixin):
    """ Centers the mean of all given columns to be 0
    Basically a simple transformation that has to memorize something with respect
    The underlying distribution (Most comments about what the class does should go here)
    """    
    def __init__(self, *args, **kwargs):
        self.means = None
    
    def fit(self, X: np.array):
        self.means = X.mean(axis=0)
    
    def transform(self, X):
        return X - self.means

    def fit_transform(self, X, y=None):
        self.fit(X)
        self.transform(X)


