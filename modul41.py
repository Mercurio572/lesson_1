# N ** 2
def strcounter(s):
    for sum in s:
        counter = 0
        for sub_sum in s:
            if sum == sub_sum:
              counter += 1
        print(sum, counter)

#strcounter('aaaabbcccd')

# N * M

