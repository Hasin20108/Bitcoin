import sys
# sys.path.append('c:/Users/mdhsn/OneDrive/Desktop/Bitcoin')
sys.path.append('c:/Users/Has/Desktop/Academic/Project/Bitcoin')


from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
from Blockchain.Backend.core.Tx import CoinbaseTx

import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        pass

    def genesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
    
    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp =  int(time.time())
        coinbaseInstance = CoinbaseTx(BlockHeight)
        coinbaseTx = coinbaseInstance.CoinbaseTransaction()

        merkleRoot = coinbaseTx.TxId
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        print(f"Block {BlockHeight} mined successfully with nonce value of {blockheader.nonce}")
        self.write_on_disk(Block(BlockHeight, 1, blockheader.__dict__, 1, coinbaseTx.to_dict()).__dict__) 

    def main(self):
        lastBlock = self.fetch_last_block()
        if lastBlock is None:
            self.genesisBlock()
        
        while True:
            lastBlock = self.fetch_last_block()
            BlockHeight = lastBlock["Height"] + 1
            prevBlockHash = lastBlock["BlockHeader"]["blockHash"]
            self.addBlock(BlockHeight, prevBlockHash)


if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.main()
