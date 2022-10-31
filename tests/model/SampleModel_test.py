import unittest
from sklearn import datasets
import numpy as np
from  src.model.SampleModel import SampleModel
import pandas as pd

class SampleModelTest(unittest.TestCase):
    # each test must start with test_ in order
    # for the test runner to automatically pick up the test
    def test_basic_regression(self):
        data = datasets.load_boston()
        X = pd.DataFrame(data['data'])
        X.columns = data['feature_names']
        y = pd.DataFrame(data['target'])
        model = SampleModel()
        model.fit(X, y)
        y_hat = model.predict(X)
        # basic check to see if the model "worked"
        self.assertTrue(np.corrcoef(y_hat, y[0])[0][0] > 0.5)




if __name__ == '__main__':
    unittest.main()