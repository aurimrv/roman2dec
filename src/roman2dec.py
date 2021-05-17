class Roman2Decimal:
	table = {'I':1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}

	def converte(self,roman):
		return self.table.get(roman)