import pytest

from roman2dec import Roman2Decimal

class TestConversorRomanoDecimal():
	def test_entender_o_simbolo_I(self):
		romano = Roman2Decimal()
		numero = romano.converte('I')
		assert numero == 1