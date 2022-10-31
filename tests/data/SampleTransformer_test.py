import unittest
from src.data.SampleTransformer import SampleTransformer
import numpy as np
import pandas as pd

class SampleTransformerTest(unittest.TestCase):
    def test_transformer(self):
        
        data = pd.DataFrame({'a':[1,2,3,4], 'b': [4,3,2,1], 'c': [1,1,1,1]})
        t = SampleTransformer()
        t.fit(data)
        output = t.transform(data)
        test_output  = pd.DataFrame({'a':[-1.5, -0.5, 0.5, 1.5], 'b': [1.5, 0.5, -0.5, -1.5], 'c': [0.0,0.0,0.0,0.0]})
        self.assertTrue(output.equals(test_output), 'done')
        # self.assertTrue(np.array_equal(output, np.array([[-1.5, -1.5, -1.5],[1.5, 1.5, 1.5]])), "Does not do what it says on the tin")


if __name__ == '__main__':
    unittest.main()