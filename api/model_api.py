import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class ModelAPI:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        with open('path/to/your/model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model

    def predict(self, data):
        return self.model.predict(data)

    def predict_batch(self, data_batch):
        return self.model.predict(data_batch)

