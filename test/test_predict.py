import unittest

from api.Predictor import Predictor

class PredictorTest(unittest.TestCase):

    def setUp(self):
        self.predictor = Predictor

    def test_predict(self):
        self.assertEqual(1, 1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
