import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import ipfshttpclient
import os
import pandas as pd

# --- 1. Train a simple ML model ---
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
print("Model trained successfully.")

# --- 2. Save the model to a .pkl file ---
model_filename = 'logistic_regression_model.pkl'
joblib.dump(model, model_filename)
print(f"Model saved as {model_filename}")

# --- 3. Upload the .pkl file to IPFS ---
print("\n3. Uploading model to IPFS...")
try:
    # Connect to local IPFS daemon (default port is 5001)
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
    
    # Add the file to IPFS
    res = client.add(model_filename)
    ipfs_cid = res['Hash']
    print(f"Model uploaded to IPFS. CID: {ipfs_cid}")

    # Optionally, pin the file to ensure it's retained
    client.pin.add(ipfs_cid)
    print(f"Model CID {ipfs_cid} pinned on IPFS.")

except Exception as e:
    print(f"Error connecting to IPFS or uploading: {e}")
    print("Please ensure your IPFS daemon is running (run 'ipfs daemon' in a separate terminal).")
    ipfs_cid = None # Indicate failure

finally:
    # Clean up the local model file
    if os.path.exists(model_filename):
        os.remove(model_filename)
        print(f"Cleaned up local file: {model_filename}")

# --- 4. Store the IPFS CID (will be used in the smart contract) ---
if ipfs_cid:
    print(f"\n--- IMPORTANT ---")
    print(f"Your IPFS CID to store on-chain is: {ipfs_cid}")
    print(f"You will use this CID in the next step (Solidity/Smart Contract).")
