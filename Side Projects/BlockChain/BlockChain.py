import hashlib

#Create simple Python Blockchain

class GeekCoinBlock:
    def __init__(self,previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()
    
    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0",["Genesis Block"]))
    
    def create_block_from_transaction(self,transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(GeekCoinBlock(previous_block_hash,transaction_list))
    
    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i+1}: {self.chain[i].block_data}")
            print(f"Hash {i+1}: {self.chain[i].block_hash} \n ")
    
    @property
    def last_block(self):
        return self.chain[-1]

t1 = "Spencer sends 5 GC to Charles"
t2 = "Hugo sends 5.4 GC to Alexis"    
t3 = "fdp sends 5.6 GC to pd"
t4 = "Alex envoie 1 GC to Alexis"
t5 = "Charlie sends 0.5 GC to David"
t6 = "Paul sends 4.1 GC to Murielle"

myblockchain = BlockChain()

myblockchain.create_block_from_transaction([t1,t2])
myblockchain.create_block_from_transaction([t3,t4])
myblockchain.create_block_from_transaction([t5,t6])

myblockchain.display_chain()