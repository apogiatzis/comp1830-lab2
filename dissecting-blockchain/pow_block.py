import hashlib
from typing import List

from block import Block

class PoWBlock(Block):

    def __init__(self, *args, nonce: int = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.nonce = nonce

    def pow(self):
        """
        Proof of work. Add nonce to block.
        """        
        nonce = 0
        while self.valid(nonce) is False:
            nonce += 1
        self.nonce = nonce
        print("Block {0} mined!".format(self.index))
        return nonce
    
    def ghash(self, nonce):
        """
        Block hash generate.
        """        
        header_hash = self.header_hash()
        token = ''.join((header_hash, str(nonce))).encode('utf-8')
        return hashlib.sha256(token).hexdigest()
    
    def valid(self, nonce):
        """
        Validates the Proof
        """
        prefix = "00000"
        return self.ghash(nonce)[:len(prefix)] == prefix
    
    def __str__(self):
        return "Block<{0}, {1}, Previous<{2}>, {3}, {4}, {5}>".format(
            self.index, self.ghash(self.nonce), self.previous_block, int(self.timestamp.timestamp()), self.data, self.nonce
        )

class PoWBlockchain:
    def __init__(self, genesis=None, blocks=None):
        self.genesis = genesis or PoWBlock(0, "Genesis Block", None)
        self.blocks = ([PoWBlock(**block) for block in blocks] if blocks else None) or [self.genesis]

    def append_block(self, data: PoWBlock):
        """
        Add new block to blockchain
        """
        block = PoWBlock(self.blocks[-1].index + 1, data, self.blocks[-1].ghash(self.blocks[-1].nonce))
        block.pow()
        new_blockchain = self.blocks + [block]
        PoWBlockchain.validate(new_blockchain)
        self.blocks = new_blockchain

    def get_last_block(self):
        return self.blocks[-1]

    def __str__(self):
        return "\n".join(str(block) for block in self.blocks)

    @classmethod
    def validate(cls, blocks: List[PoWBlock]) -> bool:
        """
        Validate given blockchain
        """
        for i in range(1, len(blocks)):
            if blocks[i - 1].ghash(blocks[i - 1].nonce) != blocks[i].previous_block or not blocks[i].valid(blocks[i].nonce):
                return False
        return True