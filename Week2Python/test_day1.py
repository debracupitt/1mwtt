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
        self.assertEqual(hw.check_chr(hw.lc_alice_test, hw.alphabet_count_test), [['a', 2], ['b', 1], ['c', 2], ['d', 1], ['e', 4], ['f', 0], ['g', 2], ['h', 0], ['i', 1], ['j', 1], ['k', 0], ['l', 1], ['m', 0], ['n', 1], ['o', 1], ['p', 1], ['q', 0], ['r', 2], ['s', 2], ['t', 2], ['u', 1], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]])

unittest.main()
