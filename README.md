Run an Ethereum Node on Sepholia testnet using Docker:

1. Install Docker
	1.	Install Docker:
	•	Follow the Docker installation guide for your operating system.
	2.	Verify Installation:

`docker --version`

2. Pull the Ethereum Client Image
	1.	Pull the official Ethereum Geth Docker image:

`docker pull ethereum/client-go:latest`

3. Create a Data Directory
	1.	Create a directory to store the node’s blockchain data:

`mkdir -p ~/sepolia-data`

4. Run the Sepolia Node Using Docker
	1.	Start the Ethereum Sepolia testnet node:

`docker run -d \
  --name sepolia-node \
  -v ~/sepolia-data:/root/.ethereum \
  -p 8545:8545 \
  -p 30303:30303 \
  ethereum/client-go:latest \
  --sepolia \
  --http \
  --http.addr "0.0.0.0" \
  --http.port 8545 \
  --http.api "eth,net,web3" \
  --syncmode "snap"`

5. Verify the Node
	1.	Check the logs to ensure the node is running and syncing:

`docker logs -f sepolia-node`


2.	Look for messages indicating the HTTP server is active:

HTTP server started           endpoint=0.0.0.0:8545

6. Install Python
	1.	Check if Python is installed:

`python3 --version`


2.	If not installed, download and install Python from python.org.

7. Install the web3.py Library
	1.	Install the web3 library to interact with your Ethereum node:

`pip install web3`

8. Create the Python Script
	1.	Open a text editor (e.g., Nano, VS Code, PyCharm).
	2.	Write the following code and save it as eth_node.py:

`from web3 import Web3

# Connect to the Ethereum node (replace with your node's URL)
node_url = "http://localhost:8545"
web3 = Web3(Web3.HTTPProvider(node_url))

# Check connection
if web3.is_connected():
    print("Successfully connected to the Ethereum node!")
    
 # Get the latest block number
 latest_block = web3.eth.blockNumber
    print(f"Latest Block Number: {latest_block}")
    
 # Get details of the latest block
 block = web3.eth.get_block(latest_block)
    print(f"Block Hash: {block.hash.hex()}")
    print(f"Block Transactions: {len(block.transactions)}")
else:
    print("Failed to connect to the Ethereum node.")`

9. Run the Python Script
Navigate to the directory where you saved the eth_node.py script:

cd /path/to/your/script


2.	Execute the script:

python3 eth_node.py

Expected Output
	•	If the Ethereum node is running, you’ll see:
	•	Confirmation of the connection.
	•	The latest block number.
	•	Details of the latest block, such as its hash and the number of transactions.

Example Output:

Successfully connected to the Ethereum node!
Latest Block Number: 789123
Block Hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
Block Transactions: 3

With these steps, you’ve successfully set up, run, and interacted with an Ethereum Sepolia node. Let me know if you need help with additional features or next steps!
