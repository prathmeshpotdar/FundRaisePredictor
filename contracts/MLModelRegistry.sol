// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract MLModelRegistry {
    // Structure to hold model information
    struct Model {
        string ipfsCid;
        string version;
        string description;
        uint256 timestamp;
        address deployer;
    }

    // Mapping to store models, perhaps by a unique ID or name
    // For simplicity, we'll just store the latest model for now.
    // In a real app, you might map a model name to its latest version's CID,
    // or use an array of models.
    Model public latestModel;

    // Event to log model updates
    event ModelRegistered(
        string indexed ipfsCid,
        string version,
        string description,
        uint256 timestamp,
        address deployer
    );

    constructor() {
        // Initialize with empty data or a default if needed
        latestModel = Model({
            ipfsCid: "",
            version: "",
            description: "",
            timestamp: 0,
            deployer: address(0)
        });
    }

    /**
     * @dev Registers a new ML model's IPFS CID and metadata.
     * @param _ipfsCid The IPFS Content ID of the serialized ML model.
     * @param _version The version of the ML model (e.g., "1.0", "2023-10-26").
     * @param _description A brief description of the model.
     */
    function registerModel(
        string memory _ipfsCid,
        string memory _version,
        string memory _description
    ) public {
        require(bytes(_ipfsCid).length > 0, "IPFS CID cannot be empty");

        latestModel = Model({
            ipfsCid: _ipfsCid,
            version: _version,
            description: _description,
            timestamp: block.timestamp,
            deployer: msg.sender
        });

        emit ModelRegistered(_ipfsCid, _version, _description, block.timestamp, msg.sender);
    }

    /**
     * @dev Retrieves the latest registered ML model's information.
     * @return ipfsCid The IPFS Content ID.
     * @return version The model version.
     * @return description The model description.
     * @return timestamp The timestamp of registration.
     * @return deployer The address that registered the model.
     */
    function getLatestModel()
        public
        view
        returns (
            string memory ipfsCid,
            string memory version,
            string memory description,
            uint256 timestamp,
            address deployer
        )
    {
        return (
            latestModel.ipfsCid,
            latestModel.version,
            latestModel.description,
            latestModel.timestamp,
            latestModel.deployer
        );
    }
}