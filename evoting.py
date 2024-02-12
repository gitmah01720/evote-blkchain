from fastapi import FastAPI, HTTPException
import uvicorn
import hashlib
import time

app = FastAPI()

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Endpoints

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blockchain E-Voting System"}

@app.post("/initialize")
def initialize_blockchain():
    global blockchain
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    return {"message": "Blockchain initialized"}

@app.post("/post-new-vote/{voter_id}")
def post_new_vote(voter_id: str, candidate: str):
    global blockchain, previous_block

    data = f"Vote: {voter_id} for {candidate}"
    new_block = create_new_block(previous_block, data)
    blockchain.append(new_block)
    previous_block = new_block

    return {"message": "Vote added successfully", "block_index": new_block.index, "hash": new_block.hash}

@app.get("/get-current-vote")
def get_current_vote():
    global blockchain
    return {"current_votes": [{"index": block.index, "hash": block.hash, "data": block.data} for block in blockchain]}

@app.get("/count-vote")
def count_vote():
    global blockchain
    # Count votes based on the data in each block
    votes_count = {}
    for block in blockchain[1:]:
        data_parts = block.data.split(" ")
        voter_id = data_parts[0]
        candidate = data_parts[3]
        if candidate not in votes_count:
            votes_count[candidate] = 1
        else:
            votes_count[candidate] += 1

    return {"vote_count": votes_count}

# Run the FastAPI app
if __name__ == "__main__":

    uvicorn.run("evoting:app", host="127.0.0.1", port=8000,reload=True)
    
