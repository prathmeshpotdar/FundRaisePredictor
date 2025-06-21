require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.28",
  networks: {
    // You can add configurations for Sepolia, Goerli, Polygon Mumbai, etc. here
    // example:
    // sepolia: {
    //   url: "YOUR_SEPOLIA_RPC_URL", // Get from Alchemy, Infura, etc.
    //   accounts: ["YOUR_PRIVATE_KEY"] // DANGER: For production, use environment variables or KMS
    // }
  }
};