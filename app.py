from flask import Flask, jsonify
from web3 import Web3

# Initialize Flask app
app = Flask(__name__)

# Connect to Ethereum Node (use Infura or your own node)
infura_url = "https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Token contract address and ABI (replace with your token's address and ABI)
contract_address = Web3.to_checksum_address("0x488A82038Bc28Cead43a799DC6a40c03BF007aee")
contract_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]

# Initialize contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/total-supply', methods=['GET'])
def get_total_supply():
    try:
        total_supply = int(int(contract.functions.totalSupply().call())/10**9)
        return jsonify(total_supply)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cir-supply', methods=['GET'])
def get_cir_supply():
    try:
        cir_supply = 90000000
        return jsonify(cir_supply)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
