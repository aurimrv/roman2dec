class Roman2Decimal:
	table = {'I':1, 'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}

	def converte(self,roman):
		sumup = 0
		last_left_number = 0
		# Invert string and process
		for symbol in roman[::-1]:
			current = self.table.get(symbol)

			mult = 1
			if current < last_left_number:
				mult = -1

			sumup = sumup + (mult * current)

			last_left_number = current

		return sumup