class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bit = f'{num1:08b}'
        number_of_bits = f'{num2:08b}'.count('1')
        new_set = ''
        counted_bits = 0

        length = len(num1_bit)

        for i in range(length):
            if (number_of_bits >= length - i) or (num1_bit[i] == '1' and number_of_bits > 0):
                new_set += '1'
                number_of_bits -= 1
            else:
                new_set += '0'

        return int(new_set + number_of_bits * '1', 2)
