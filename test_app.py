import unittest
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class TestTitanicModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Cargar el modelo entrenado desde el archivo
        with open('titanic_model.pkl', 'rb') as file:
            cls.model = pickle.load(file)

    def test_model_instance(self):
        # Verificar que el modelo cargado es una instancia de RandomForestClassifier
        self.assertIsInstance(self.model, RandomForestClassifier)

    def test_model_prediction(self):
        # Crear un dataframe de ejemplo con las mismas columnas que el modelo espera
        test_data = pd.DataFrame({
            'Pclass': [3],
            'Sex': [0],
            'Age': [25],
            'Fare': [7.25],
            'Embarked': [0],
            'Title': [1],
            'IsAlone': [1],
            'Age*Class': [75]
        })

        # Realizar una predicción con el modelo
        prediction = self.model.predict(test_data)
        
        # Verificar que la predicción es un valor esperado (0 o 1)
        self.assertIn(prediction[0], [0, 1])

if __name__ == '__main__':
    unittest.main()
