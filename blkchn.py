import datetime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:

    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(data="Starting Gen",proof=1,previous_hash="0",index=0)
        self.chain.append(genesis_block)

    def mine_block(self,data:str) -> dict:
        previous_block  = self.get_prev_block()
        previous_proof = previous_block["proof"]
        print(previous_proof)
        index = len(self.chain) + 1
        proof = self._proof_of_work(previous_proof=previous_proof,index=index,data=data)
        prev_hash = self._hash_the_block(block=previous_block)
        block = self._create_block(data=data,proof=proof,previous_hash=prev_hash,index=index)

        self.chain.append(block)    

        return block
    

    def _hash_the_block(self,block:dict) -> str:
        """
        Hash the block and  return str.
        """
        encoded_block = _json.dumps(block,sort_keys=True).encode()
        return _hashlib.sha256(encoded_block).hexdigest()
    

    def _to_digest(self,new_proof:int,previous_proof:int,index:str,data:str) -> bytes:
        formula = str(new_proof*2 + previous_proof**2 + index+1) + data
        return formula.encode()
        

    def _proof_of_work(self,previous_proof:str,index:int,data:str) -> int:
        """
        start from a number 1 to inf and find a number which satisfys requirement of a mathematical function.

        """
        new_proof = 1
        check_proof=  False

        while not check_proof:
            # print(new_proof)
            to_digest = self._to_digest(new_proof=new_proof,previous_proof=previous_proof,index=index,data=data)

            hash_value = _hashlib.sha256(to_digest).hexdigest(); # string value of hash.
            if(hash_value[:2]) == "00":
                check_proof = True
            else:
                new_proof+=1
        
        return new_proof
    

    def get_prev_block(self) -> dict:
        return self.chain[-1]
      
    
    def _create_block(self,data:str, proof: int, previous_hash: str, index: int) -> dict:
        block = {

            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash
        }

        print(block)
        return block

    def is_chain_valid(self)->bool:
        current_block = self.chain[0]
        idx = 1

        while idx < len(self.chain):
            next_block = self.chain[idx]
            if next_block.get("previous_hash") != self._hash_the_block(current_block):
                return False

            # calculating next proof of work.
            nxt_digst = self._to_digest(new_proof=next_block["proof"],previous_proof=current_block["proof"],index=next_block["index"],data=next_block["data"])
            dig_hash = _hashlib.sha256(nxt_digst).hexdigest()
            
            if dig_hash[:2] != "00":
                return False


            idx +=1
            current_block = next_block

        return True

      
    