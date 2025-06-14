// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FundRaisePredictor {
    address public owner;
    string public ipfsModelHash;

    event PredictionRequested(address requester, uint sizeInSqFt);

    constructor(string memory _ipfsModelHash) {
        owner = msg.sender;
        ipfsModelHash = _ipfsModelHash;
    }

    function requestPrediction(uint sizeInSqFt) public {
        emit PredictionRequested(msg.sender, sizeInSqFt);
    }

    function updateModelHash(string memory newHash) public {
        require(msg.sender == owner, "Not owner");
        ipfsModelHash = newHash;
    }
}
