// SPDX-License-Identifier: MIT
// pragma solidity ^0.6.0;
pragma solidity >= 0.7.0 <0.8.0;

contract Election {

    address public electionOfficialAddr;
    string public electionOfficialName;
    string public proposal;

    // vote str

    struct vote {
        address voterAddr; // address of the voter
        bool chioce; // is proposal ok suported or not?

    }

    struct voter{
        string voterName;
        bool voted; // voted or not?
    }

    // helping variable:
    uint countResult = 0; // counting of vote
    uint public finalResult = 0; // final vote count;
    uint public totalVoter = 0;
    uint totalvote = 0; // how many vote has been done.

    mapping (uint => vote) private  votes; // voter id : vote info
    mapping (address => voter) public voterRegister; // voter address:voter info

    enum State {created,voting,ended}
    State public currState;   

    // modifiers:
    modifier condition(bool _condition){
        require(_condition);
        _;
    }
    modifier onlyOfficial(){
        require(msg.sender == electionOfficialAddr);
        _;
    }
    modifier instate(State _st){
        require(currState == _st);
        _;
    }

    constructor  (
        string memory _ballotofcNm,
        string memory _prop
    ) {
        electionOfficialAddr = msg.sender;
        electionOfficialName = _ballotofcNm;
        proposal = _prop;
        currState = State.created;
        
        
    }


    function addVote(
        address _voterAddr,
        string memory _voterName
    ) public instate(State.created) onlyOfficial {

        voter memory v;
        v.voterName = _voterName;
        v.voted = false;

        voterRegister[_voterAddr] = v; // adding this voter into register.
        totalVoter++;
    }

    function  startVote() public instate(State.created){
        currState = State.voting;
    }

    function  do_vote(bool _choice ) public instate(State.voting) returns (bool voted){
        bool isFound = false; // check of this voter address is registerd

        if(bytes(voterRegister[msg.sender].voterName).length !=0 &&
            voterRegister[msg.sender].voted == false
         ){
            voterRegister[msg.sender].voted = true;
            vote memory v;
            v.voterAddr  = msg.sender;
            v.chioce = _choice;
            
            votes[totalvote++] = v;

            if(_choice==true) countResult++;
            isFound = true;
            
         }

         return isFound;
    }

    function  end_vote() public instate(State.voting) onlyOfficial{
        currState = State.ended;

        finalResult = countResult;
    }
    
    

}