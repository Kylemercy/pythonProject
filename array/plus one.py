class solution:
    def plusone(self, digits: list[int]):
        digits = digits[::-1]
        # reversing the digits
        carry, i = 1, 0
        # carry rep 1 this the one that is added to each digit
        # i rep the index
        while carry:
            # we loop through our digits aslong as carry = 1
            if i < len(digits):

                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
                    '''here if the first digit is not a 9 we add one to the first digit and then terminate our loop 
                    by making carry = 0,but if the first element == to 9 we turn it to 0 and move to the next we keep 
                    on iterating aslong as the next element is 9 else we end the loop '''
            else:
                # when we are out of bounds when there is no more digits to add to
                digits.append(1)
                carry = 0

            i += 1
        return digits[::-1]


ll = solution()
print(ll.plusone([4, 3, 2, 1]))
