import fastapi as _fastapi
import blkchn as _bc

blockchain = _bc.Blockchain()
app = _fastapi.FastAPI()

# end point to mine a block.
@app.post("/mine/")
def mine_block(data:str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400,detail="The blockchain is invalid")
    
    block = blockchain.mine_block(data=data)

    return block

#end point to see the blockchain
@app.get("/get-all")
def getChain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400,detail="The blockchain is invalid")
    

    return blockchain.chain



#end point to see the blockchain
@app.get("/validate")
def getValidate():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400,detail="The blockchain is invalid")
    

    return "blockchain is Valid"


