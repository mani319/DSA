

ops_preference = {'*': 2,
                  '/': 2,
                  '+': 1,
                  '-': 1}


def is_digit(ch):
    return (ch >= '0' and ch <= '9')


def is_operator(ch):
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')


def has_more_or_equal_preference(op1, op2):
    return (ops_preference[op1] >= ops_preference[op2])


def apply_operator(val1, op, val2):
    if(op == '+'):
        return val1+val2
    elif(op == '-'):
        return val1-val2
    elif(op == '*'):
        return val1*val2
    elif(op == '/'):
        return val1//val2
    else:
        return


def infix_evaluate_expression(exp):
    values = []
    ops = []

    i = 0
    while(i < len(exp)):
        if(exp[i] == '('):
            ops.append(exp[i])
            i += 1

        elif(is_digit(exp[i])):
            temp = ""
            while(i < len(exp) and is_digit(exp[i])):
                temp += exp[i]
                i += 1
            values.append(int(temp))

        elif(is_operator(exp[i])):
            while(len(ops) > 0 and
                    is_operator(ops[len(ops)-1]) and
                    has_more_or_equal_preference(ops[len(ops)-1], exp[i])):
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_operator(val1, op, val2))
            ops.append(exp[i])
            i += 1

        elif(exp[i] == ')'):
            while((len(ops) > 0) and
                    ops[len(ops)-1] != '('):
                op = ops.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(apply_operator(val1, op, val2))
            ops.pop()
            i += 1

        else:
            i += 1
            pass

    while(len(ops) != 0):
        op = ops.pop()
        val2 = values.pop()
        val1 = values.pop()
        result = apply_operator(val1, op, val2)
        values.append(result)

    return values.pop()


if __name__ == "__main__":
    strings = ["10 + 40 * (6 + 2)",
               "10 + 2 * 6",
               "100 * 2 + 12",
               "100 * ( 2 + 12 )",
               "100 * ( 2 + 12 ) / 14",
               "(10 * (10 + 3))"]

    for string in strings:
        print(infix_evaluate_expression(string))
