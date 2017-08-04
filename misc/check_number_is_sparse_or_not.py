"""
Q: Check if a given number is sparse or not
A num is said to be a sparse num,
    if in binary representation of num, no two or more consecutive bits are set

Logic:
If we observer carefully,
    then we can notice that if we can use bitwise AND of binary representation
    of the “given number and its “right shifted number”
    to figure out whether the number is sparse or not.

Result of AND operator would be 0 if number is sparse and non-zero if not.
"""


def checkSparse(num):
    return not(num & (num >> 1))


if __name__ == "__main__":
    nums = [72, 12, 2, 3]

    for num in nums:
        print(checkSparse(num))
