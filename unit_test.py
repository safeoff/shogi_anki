import sys
import unittest
import AddAnki


class TestAddAnki(unittest.TestCase):

	# カードを登録
	def test_addAnki(self):
		# arrange
		front = "<img src=\'http://sfenreader.appspot.com/sfen?sfen=lnsgkgsnl%2F1r5b1%2Fppppppppp%2F9%2F9%2F9%2FPPPPPPPPP%2F1B5R1%2FLNSGKGSNL%20b%20-%201\'>次の一手は？"
		back = "△6八銀"
		deck = "学習::将棋::実践次の一手"
		expected_value = b"1 new words\n"
		# act
		result = AddAnki.addAnki(front, back, deck)
		# assert
		self.assertEqual(expected_value, result)