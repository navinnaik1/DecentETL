
from solcx import compile_source

from solcx import install_solc

install_solc(version='0.8.0')

compiled_sol = compile_source('''
    pragma solidity ^0.8.0;

contract test  {
    uint256 entryid=3;

    struct TokenData{
        uint256 tokenId;
        string price;
        uint256 time;
        string indicator1;
        string indicator2;
    }

    mapping (uint256 => TokenData) public collectedDatabyTid;
    mapping (uint256 => TokenData) public collectedDatabyEid;

    function addData(
    uint256 _tokenid,
    string memory _price,
    uint256 _time,
    string memory _indicator1,
    string memory _indicator2) external {
        collectedDatabyTid[_tokenid] = TokenData({tokenId:_tokenid,
        price:_price,
        time:_time,
        indicator1:_indicator1,
        indicator2:_indicator2 });
         collectedDatabyEid[entryid++] = TokenData({tokenId:_tokenid,
        price:_price,
        time:_time,
        indicator1:_indicator1,
        indicator2:_indicator2 });
    }
    
}''',
  output_values=['abi', 'bin']
)

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']
