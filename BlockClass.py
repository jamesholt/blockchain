import haslib
import datetime
import random

class Block: 
	def getPowHash (self, data):
		nonce = str(random.randint(0, 3000000))
		noncedData = data + nonce
		hash = haslib.sha256 (noncedData.encode('utf-8)).hexdigest()
		#hashlib requires data to be encoded before hashed.
		if hash.startswith ("00"): 
				self.nonce = nonce
				return hash
		else: 
				return self.getPowHash (data)

	def __init__ (self, data, previousHash): 
		self.data = data 
		self.nonce = nonce
		self.previousHash = previousHash
		self.timestamp = datatime.datetime.now()
		self.has = self.getPowHash (data)
genesisBlock = Block("I am genesis block!", 0)
secondBlock = Block("I am second block", genesisBlock.hash)
thirdBlock = Block("I am third block", secondBlock.hash)

print ("Genesis Block Hash: ", genesisBlock.hash)
print ("Second Block Hash: ", secondBlock.hash)
print ("Third Block Hash: ", thirdBlock.hash)
