from array import array

BV_DEFAULT_MAX_VALUE = 10

class BitVector:

    def __init__(self, max_value=BV_DEFAULT_MAX_VALUE):
        self._max_value = max_value
        self._array = array('B', [0 for i in range( int(self._max_value/8 + 1)) ])

        self._set_bit_masks = array('B', [128, 64, 32, 16, 8, 4, 2, 1])
        self._unset_bit_masks = array('B', [127, 191, 223, 239, 247, 251, 253, 254])

    @property
    def array(self):
        return self._array

    @property
    def max_value(self):
        return self._max_value

    @property
    def set_bit_masks(self):
        return self._set_bit_masks

    @property
    def unset_bit_masks(self):
        return self._unset_bit_masks

    def _index_offset(self, number):
        if number is None or number > self._max_value or number < 0:
            raise ValueError('{0} is outside bit vector capacity'.format(number))
        index, offset = divmod(number, 8)
        return index, offset

    def set(self, number):
        index, offset = self._index_offset(number)
        self._array[index] = self._array[index] | self._set_bit_masks[offset]

    def unset(self, number):
        index, offset = self._index_offset(number)
        self._array[index] = self._array[index] & self._unset_bit_masks[offset]

    def __str__(self):
        return '{0} max_count {1}'.format(self._array, self._max_value)

    def has(self, number):
        index, offset = self._index_offset(number)
        return bool(self._array[index] & self._set_bit_masks[offset])

    def bit_array_str_(self):
        for index, byte in enumerate(self._array):
            print("{0}: {1:08b}".format(index, byte))


if __name__ == '__main__':
    bv = BitVector(80)

    print('set bit masks')
    for mask in bv.set_bit_masks:
        print("{0:08b}".format(mask))

    print('unset bit masks')
    for mask in bv.unset_bit_masks:
        print("{0:08b}".format(mask))

    for i in range(80):
        if i % 2 == 0:
            bv.set(i)

    print('bits')
    bv.bit_array_str_()

    for i in range(80):
        if i % 2 == 0:
            bv.unset(i)

    print('bits')
    bv.bit_array_str_()