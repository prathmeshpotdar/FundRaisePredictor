Instruction for running

run fundRaisePrediction.ipynb
ipfs daemon
npx hardhat node
python3 ipfscid.py and paste cid in deploy.js file
npx hardhat run  scripts/deploy.js --network localhost and paste deployed to account in model_inference.py file
python3 model_inference.py
