import unittest
from task1 import modified_levenshtein

class TestModifiedLevenshtein(unittest.TestCase):
    def assertDistance(self, s, t, expected):
        D = modified_levenshtein(s, t)
        self.assertEqual(D[len(s)][len(t)], expected,
                         f"distance({s!r}, {t!r}) should be {expected}, got {D[len(s)][len(t)]}")

    def test_both_empty(self):
        self.assertDistance("", "", 0)

    def test_empty_to_nonempty(self):
        self.assertDistance("", "abc", 1+2+3)

    def test_nonempty_to_empty(self):
        self.assertDistance("abc", "", 1+2+3)

    def test_same_single_letter(self):
        self.assertDistance("a", "a", 0)

    def test_substitution_single(self):
        self.assertDistance("a", "b", 1)

    def test_delete_vs_replace(self):
        self.assertDistance("ab", "a", 2)

    def test_replace_chain(self):
        self.assertDistance("ab", "bc", 2)

    def test_longer_example(self):
        self.assertDistance("kit", "sit", abs(11-19) + 0 + 0)

if __name__ == "__main__":
    unittest.main()
