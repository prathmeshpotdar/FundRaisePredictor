
import requests
X_test= pd.read_csv('X_test.csv')
y_test= pd.read_csv('y_test.csv')
response = requests.post("http://localhost:5000/predict", json={"size": sqft})
print("Prediction:", response.json())
