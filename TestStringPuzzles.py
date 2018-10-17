from unittest import TestCase

from StringPuzzles import cat_dog
from StringPuzzles import count_code
from StringPuzzles import other_end


class TestStringPuzzles(TestCase):
    # Cat Dog Tests
    def test_cat_dog1(self):
        self.assertEqual(cat_dog('catdog'), True)

    def test_cat_dog2(self):
        self.assertEqual(cat_dog('catcat'), False)

    def test_cat_dog3(self):
        self.assertEqual(cat_dog('1cat1cadodog'), True)

    def test_cat_dog4(self):
        self.assertEqual(cat_dog('1cat1cadodog'), True)

    def test_cat_dog6(self):
        self.assertEqual(cat_dog('cat'), False)

    def test_cat_dog7(self):
        self.assertEqual(cat_dog('ca'), True)

    def test_cat_dog8(self):
        self.assertEqual(cat_dog('c'), True)

    def test_cat_dog9(self):
        self.assertEqual(cat_dog(''), True)

    def test_cat_dog10(self):
        self.assertEqual(cat_dog('catxdogxdogxcat'), True)

    #  +++ Other End Tests +++
    def test_other_end1(self):
        self.assertEqual(other_end('Hiabc', 'abc'), True)

    def test_other_end2(self):
        self.assertEqual(other_end('AbC', 'HiaBc'), True)

    def test_other_end3(self):
        self.assertEqual(other_end('Hiabc', 'BC'), True)

    def test_other_end4(self):
        self.assertEqual(other_end('Z', 'z'), True)

    def test_other_end5(self):
        self.assertEqual(other_end('12', '12'), True)

    def test_other_end6(self):
        self.assertEqual(other_end('abc', 'abc'), True)

    def test_other_end7(self):
        self.assertEqual(other_end('ab', '12ab'), True)

    def test_other_end8(self):
        self.assertEqual(other_end('Hiabcx', 'bc'), False)

    def test_other_end9(self):
        self.assertEqual(other_end('abcXYZ', 'abcDEF'), False)

    def test_other_end10(self):
        self.assertEqual(other_end('ab', 'ab12'), False)

    def test_other_end11(self):
        self.assertEqual(other_end('Hiabc', 'abcd'), False)

    def test_other_end12(self):
        self.assertEqual(other_end('yz', '12xz'), False)

    # +++ Count Code Tests +++
    def test_count_code1(self):
        self.assertEqual(count_code('aaacodebbb'), 1)

    def test_count_code2(self):
        self.assertEqual(count_code('cozexxcope'), 2)

    def test_count_code3(self):
        self.assertEqual(count_code('xxcozeyycop'), 1)

    def test_count_code4(self):
        self.assertEqual(count_code('AAcodeBBcoleCCccoreDD'), 3)

    def test_count_code5(self):
        self.assertEqual(count_code('abcxyz'), 0)

    def test_count_code6(self):
        self.assertEqual(count_code('coe'), 0)
