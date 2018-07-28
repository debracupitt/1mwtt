import unittest

from day1 import moo

class TestMoo(unittest.TestCase):

	def test0(self):
		self.assertEqual(moo(0), "")
	def test1(self):
		self.assertEqual(moo(1), "moo")
	def test2(self):
		self.assertEqual(moo(2), "moomoo")

unittest.main()