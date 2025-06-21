const hre = require("hardhat");

async function main() {
  const MLModelRegistry = await hre.ethers.getContractFactory("MLModelRegistry");
  const mlModelRegistry = await MLModelRegistry.deploy();

  await mlModelRegistry.waitForDeployment();

  console.log(`MLModelRegistry deployed to ${mlModelRegistry.target}`);

  // You can now interact with this contract, e.g., register a model
  // Remember to replace "YOUR_IPFS_CID_FROM_PYTHON" with the actual CID
  const ipfsCid = "Qmb8CttvpncT9WmwJNkNd1AUW4MknGEhu6b1BmnRnJ2tTW"; // <-- REPLACE THIS
  const version = "1.0";
  const description = "Fundraise Dataset";

  console.log(`\nRegistering model with CID: ${ipfsCid}...`);
  const tx = await mlModelRegistry.registerModel(ipfsCid, version, description);
  await tx.wait();
  console.log("Model registered successfully on-chain!");

  // Verify by fetching
  const [retrievedCid, retrievedVersion, retrievedDesc, retrievedTimestamp, retrievedDeployer] = await mlModelRegistry.getLatestModel();
  console.log("\nRetrieved Model Info:");
  console.log(`  IPFS CID: ${retrievedCid}`);
  console.log(`  Version: ${retrievedVersion}`);
  console.log(`  Description: ${retrievedDesc}`);
  console.log(`  Timestamp: ${new Date(Number(retrievedTimestamp) * 1000).toLocaleString()}`);
  console.log(`  Deployer: ${retrievedDeployer}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});