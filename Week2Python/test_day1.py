import unittest

from day1 import moo
# from homework_week2 import alphabet_setup
import homework_week2
hw = homework_week2

class TestMoo(unittest.TestCase):

	def test0(self):
		self.assertEqual(moo(0), "")
	def test1(self):
		self.assertEqual(moo(1), "moo")
	def test2(self):
		self.assertEqual(moo(2), "moomoo")

class TestAlice(unittest.TestCase):
    def test0(self):
        self.assertEqual(hw.check_chr(hw.lc_alice_test, hw.alphabet_count_test), [['a', 4], ['b', 2], ['c', 4], ['d', 2], ['e', 8], ['f', 0], ['g', 4], ['h', 0], ['i', 2], ['j', 2], ['k', 0], ['l', 2], ['m', 0], ['n', 2], ['o', 2], ['p', 2], ['q', 0], ['r', 4], ['s', 4], ['t', 4], ['u', 2], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]])

unittest.main()
