from web3 import Web3

# Connect to the Ethereum node (replace with your node's URL)
node_url = "http://localhost:8545"
web3 = Web3(Web3.HTTPProvider(node_url))

# Check connection
if web3.is_connected():
    print("Successfully connected to the Ethereum node!")
    
    # Get the latest block number
    latest_block = web3.eth.block_number
    print(f"Latest Block Number: {latest_block}")
    
    # Get details of the latest block
    block = web3.eth.get_block(latest_block)
    print(f"Block Hash: {block.hash.hex()}")
    print(f"Block Transactions: {len(block.transactions)}")
else:
    print("Failed to connect to the Ethereum node.")  # Fixed the unmatched parenthesis
