import unittest
from src.data.SampleTransformer import SampleTransformer
import numpy as np

class SampleTransformerTest(unittest.TestCase):
    def test_transformer(self):
        t = SampleTransformer()
        data = np.array([[1,2,3],[4,5,6]])
        t.fit(data)
        output = t.transform(data)
        self.assertTrue(np.array_equal(output, np.array([[-1.5, -1.5, -1.5],[1.5, 1.5, 1.5]])), "Does not do what it says on the tin")


if __name__ == '__main__':
    unittest.main()