'''
'''


def power_iterative(x, y):
    result = 1

    while(y > 0):
        if(y & 1):
            result *= x

        x *= x

        y >>= 1

    return result


def power_recursive(x, y):
    if(y == 0):
        return 1

    result = power_recursive(x, int(y/2))
    if(y % 2 == 0):
        return result * result
    else:
        if(y > 0):
            return result * result * x
        else:
            return ((result * result) / x)


if __name__ == "__main__":
    x = 2
    y = 5
    y1 = -2
    print(power_iterative(x, y))
    print(power_recursive(x, y))
    print(power_recursive(x, y1))
