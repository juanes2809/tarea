import unittest
import json
from api.model_api import ModelAPI

class ModelApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ModelAPI()
        cls.client = cls.api.app.test_client()
        cls.api.app.testing = True

    def test_predict(self):
        payload = {
            "features": [1, 2, 3, 4]
        }
        response = self.client.post('/predict', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('predictions', json.loads(response.data))

    def test_predict_batch(self):
        payload = {
            "batch_features": [
                [1, 2, 3, 4],
                [5, 6, 7, 8]
            ]
        }
        response = self.client.post('/predict_batch', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('predictions', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()

