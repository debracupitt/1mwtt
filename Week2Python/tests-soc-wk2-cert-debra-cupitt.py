import unittest
import soc_wk2_cert_debra_cupitt as hw
# hw = soc_wk2_cert_debra_cupitt
# from soc_wk2_cert_debra_cupitt import check_chr, cypher

class TestHomework(unittest.TestCase):
    # Alice alphabet counter list
    def test0(self):
        self.assertEqual(hw.check_chr(hw.lc_alice_test, hw.alphabet_count_test), [['a', 2], ['b', 1], ['c', 2], ['d', 1], ['e', 4], ['f', 0], ['g', 2], ['h', 0], ['i', 1], ['j', 1], ['k', 0], ['l', 1], ['m', 0], ['n', 1], ['o', 1], ['p', 1], ['q', 0], ['r', 2], ['s', 2], ['t', 2], ['u', 1], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]])
    def test1(self):
        self.assertEqual(hw.cypher("Hey", 1), [73, 102, 122])
    def test3(self):
        self.assertEqual(hw.print_board(hw.world2), ["water", "land", "water", "water", "land", "land"])
    def test4(self):
        self.assertEqual(hw.print_board_reverse(hw.world2), [["land", "land", "water"], ["water", "land", "water"]])
    def test5(self):
        self.assertEqual(hw.continent_counter(hw.world, 1, 4), 11)
    # Alice alphabet counter dict
    def test6(self):
        self.assertEqual(hw.check_chr_dict(hw.lc_alice_test_dict, hw.alphabet_count_test_dict), {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'e': 4, 'f': 0, 'g': 2, 'h': 0, 'i': 1, 'j': 1, 'k': 0, 'l': 1, 'm': 0, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 2, 's': 2, 't': 2, 'u': 1, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})


unittest.main()
