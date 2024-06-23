from flask import Flask, request, jsonify
import pickle
import psycopg2
from psycopg2.extras import RealDictCursor
import json

class ModelAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.model = self.load_model()
        self.conn = self.connect_db()
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.setup_routes()

    def load_model(self):
        with open('api/model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model

    def connect_db(self):
        conn = psycopg2.connect(
            dbname='estimations',
            user='user',
            password='password',
            host='db'
        )
        return conn

    def setup_routes(self):
        @self.app.route('/predict', methods=['POST'])
        def predict():
            data = request.get_json()
            features = data['features']
            predictions = self.model.predict([features])
            
            self.cursor.execute(
                "INSERT INTO predictions (input, prediction) VALUES (%s, %s)",
                (json.dumps(features), json.dumps(predictions.tolist()))
            )
            self.conn.commit()
            
            return jsonify(predictions=predictions.tolist())

        @self.app.route('/predict_batch', methods=['POST'])
        def predict_batch():
            data = request.get_json()
            batch_features = data['batch_features']
            predictions = self.model.predict(batch_features)
            
            self.cursor.execute(
                "INSERT INTO batch_predictions (input, prediction) VALUES (%s, %s)",
                (json.dumps(batch_features), json.dumps(predictions.tolist()))
            )
            self.conn.commit()
            
            return jsonify(predictions=predictions.tolist())

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    api = ModelAPI()
    api.run()

