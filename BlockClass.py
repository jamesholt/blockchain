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