import pytest

from roman2dec import Roman2Decimal

class TestConversorRomanoDecimal():
	def test_entender_o_simbolo_I(self):
		romano = Roman2Decimal()
		numero = romano.converte('I')
		assert numero == 1

	def test_entender_o_simbolo_V(self):
		romano = Roman2Decimal()
		numero = romano.converte('V')
		assert numero == 5