from array import array


class BitVector:

    def __init__(self, max_value=10):
        self._max_value = max_value
        self._array = array('B', [0 for i in range( int(self._max_value/8 + 1)) ])

        self._set_bit_masks = {
            0: 128,
            1: 64,
            2: 32,
            3: 16,
            4: 8,
            5: 4,
            6: 2,
            7: 1,
        }

        self._unset_bit_masks = {
            0: 127,
            1: 191,
            2: 223,
            3: 239,
            4: 247,
            5: 251,
            6: 253,
            7: 254,
        }

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
        if number > self._max_value or number < 0:
            raise ValueError('{0} is outside bit vector capacity'.format(number))
        index, offset = divmod(number, 8)
        return index, offset

    def set(self, number):
        index, offset = self._index_offset(number)
        print('index {0} offset {1}'.format(index, offset))
        print('{0:08b}'.format(self._array[index]))
        self._array[index] = self._array[index] | self._set_bit_masks[offset]
        print('{0:08b}'.format(self._array[index]))

    def unset(self, number):
        index, offset = self._index_offset(number)
        print('index {0} offset {1}'.format(index, offset))
        print('{0:08b}'.format(self._array[index]))
        self._array[index] = self._array[index] & self._unset_bit_masks[offset]
        print('{0:08b}'.format(self._array[index]))

    def __str__(self):
        return '{0} max_count {1}'.format(self._array, self._max_value)


if __name__ == '__main__':
    bv = BitVector(10)

    print('set bit masks')
    for key, value in bv.set_bit_masks.items():
        print(key, "{0:08b}".format(value))

    print('unset bit masks')
    for key, value in bv.unset_bit_masks.items():
        print(key, "{0:08b}".format(value))

    for i in range(11):
        bv.set(i)

    print('bits')
    for byte in bv.array:
        print("{0:08b}".format(byte))

    for i in range(11):
        bv.unset(i)

    print('bits')
    for byte in bv.array:
        print("{0:08b}".format(byte))
