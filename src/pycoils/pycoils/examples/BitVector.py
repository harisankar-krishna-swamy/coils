from pycoils.misc.bit_vector import BitVector


def display_vector(bv):
    for index, byte in enumerate(bv.vector):
        print("{0}: {1:08b}".format(index, byte))

# create bit vector that can hold numbers 0 to 10
bv = BitVector(10)


print('Vector bits string')
display_vector(bv)

# set numbers in bit vector
numbers = (1, 3, 4)
for number in numbers:
    bv.set(number)


print('Vector bits string')
display_vector(bv)

print(bv.has(4))
print(bv.has(7))

bv.unset(4)
print(bv.has(4))

print('Vector bits string')
display_vector(bv)