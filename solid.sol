// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract MyCon{ // various datatypes.
    uint public cnt =0;
    int public x = -1; // state variable.
    uint256 public y = 23; 
    string public ms = "Mahi";
    address public myadr  = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
 
    uint[] public ar = [1,34,55];
    string[] public sar = ["a","b"];
    
    function addVal(string memory _value) public {
        sar.push(_value);
    }
    // function shows() public {
    //     for (uint i=0; i< ar.length; i++)    
    //     {
    //         ar[i];
    //     };
    // }

    struct Node {
        uint level;
        string name;
    }

    Node public head = Node(1,"Hello");
    
    // pure functions can only perform ops on local variables and args.
    function changer() public pure returns (uint){
       uint xx  = 9;  // local variables.

        return xx*37;
    }


    // local variables.
    function incr() public {
        cnt+=1;
    }
}