"""
Block chain : Reversed linked list.


begens - > Genesys Block.

Genesis-Block
{
    index:0,
    timestamp: curr-time.
    data: Any-obj,
    proof: 3,  // Result of a mathematical computation.
    prev_hash: 0
} -> hash() - > i34iucc

    # Adding new block in chain. hash(<BLOCK> ) - > sha256 code.

{
    index: 1,
    timestamp: t2,
    data : data-2
    proof: 34
    prev_hash: i34iucc.

} -> hash() - > yiau232

{
    index: 2,
    timestamp: t2,
    data : data-2
    proof: 34
    prev_hash: yiau232

}

""" 



# ipython 
- create blockchain
- mine
- verify.


# uvicorn main:app --reload
goto: http://127.0.0.1:8000/docs
