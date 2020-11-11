import unittest

from pycoils.misc.bit_vector import BitVector, BV_DEFAULT_MAX_VALUE


class TestBitVectorDefaultInstance(unittest.TestCase):

    def setUp(self):
        self.bv = BitVector()

    def test_default_max(self):
        self.assertEqual(self.bv.max_value, BV_DEFAULT_MAX_VALUE)

    def test_item_size(self):
        self.assertEqual(self.bv.array.itemsize, 1)

    def test_set_negative(self):
        with self.assertRaises(ValueError):
            self.bv.set(number=-1)

    def test_set_zero(self):
        self.bv.set(number=0)
        self.assertTrue(self.bv.has(0))

    def test_set_gt_max_value(self):
        with self.assertRaises(ValueError):
            self.bv.set(number=self.bv.max_value + 1)

    def test_has_on_empty(self):
        for i in range(BV_DEFAULT_MAX_VALUE + 1):
            self.assertFalse(self.bv.has(i))

    def test_set_even(self):
        for i in range(BV_DEFAULT_MAX_VALUE + 1):
            if i % 2 == 0:
                self.bv.set(number=i)

        for i in range(BV_DEFAULT_MAX_VALUE + 1):
            if i % 2 == 0:
                self.assertTrue(self.bv.has(i), '{0} has to be in bit vector'.format(i))
            else:
                self.assertFalse(self.bv.has(i), '{0} should not be in bit vector'.format(i))

