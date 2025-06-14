
from flask import Flask, request, jsonify
from web3 import Web3
import pickle

app = Flask(__name__)

with open("fundraiseprediction_model.pkl", "rb") as f:
    model = pickle.load(f)

w3 = Web3(Web3.HTTPProvider('https://rpc-mumbai.maticvigil.com'))
contract_address = '0xYourContractAddress'
contract_abi = [ ... ]  # Replace with actual ABI

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    sqft = data['size']
    price = model.predict([[sqft]])[0]
    return jsonify({'predicted_price': round(price, 2)})

if __name__ == "__main__":
    app.run(debug=True)
