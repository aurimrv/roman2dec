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

	def test_entender_dois_simbolos_como_II(self):
		romano = Roman2Decimal()
		numero = romano.converte('II')
		assert numero == 2

	def test_entender_quatro_simbolos_como_XXII(self):
		romano = Roman2Decimal()
		numero = romano.converte('XXII')
		assert numero == 22

	def test_entender_numeros_como_IX(self):
		romano = Roman2Decimal()
		numero = romano.converte('IX')
		assert numero == 9