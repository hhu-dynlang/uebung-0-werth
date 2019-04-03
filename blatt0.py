import numpy


def is_palindrome1(s):
    return s == s[::-1]


def is_palindrome(s):
    return s == ''.join(reversed(s))


def pascal(n):
    if n < 0:
        raise ValueError('No negatives allowed')
    elif n == 0:
        return [1]
    N = pascal(n-1)
    #Für jede Zeile die Vorgänger addieren
    return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]

def print_pascal(n):
    if n < 0:
        raise ValueError('No negatives allowed')
    for i in range(n):
        print(pascal(i))


def flatten(l):
    result = []
    for i in range(0, len(l)):
        if type(l[i]) is list:
            l_i = flatten(l[i])
            for j in range(0,len(l_i)):
                result.append(l_i[j])
        else:
            result.append(l[i])
    return result


def solve_equation(a,b,c):
    #a*x^2 + b*x +c = 0
    if b == 0 and c == 0:
        return [0.0]
    if b == 0:
        under_root = numpy.negative(c) / a
        if(under_root < 0):
            return []
        else:
            val = numpy.sqrt(under_root)
            result = []
            result.append(val)
            result.append(-val)
            return result
    if c == 0:
        result = []
        x_1 = solve_equation(a,0,0)
        x_2 = solve_equation(0,a,b)
        result.append(x_1)
        result.append(x_2)
        return flatten(result)
    if a == 0:
        result = []
        x = -c/b
        result.append(x)
        return result
    else:
        result = []
        p = b/a
        q = c/a
        under_root = numpy.power(p/2, 2)-q
        if under_root < 0:
            return []
        else:
            x_1 = -p / 2 - numpy.sqrt(under_root)
            x_2 = -p / 2 + numpy.sqrt(under_root)
            result.append(x_1)
            result.append(x_2)
            return result


def fizz_buzz(n):
    result = list(range(1,n+1))
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            result.insert(i, "fizzbuzz")
            result.remove(i)
        elif i%3 == 0:
            result.insert(i, "fizz")
            result.remove(i)
        elif i%5 == 0:
            result.insert(i,"buzz")
            result.remove(i)
    return result


def mybin(i):
    if i == 0:
        return "0b0"
    is_negative = ""
    if i < 0:
        is_negative = "-"
        i = -i
    result = ""
    while i > 0:
        r = i%2
        result += str(r)
        i = int(numpy.floor(i/2))
    return is_negative+"0b"+result[::-1]


def myint(b):
    result = 0
    b = b.replace("0b","")
    b = b[::-1]
    for i in range(0, len(b)):
        result += int(b[i])*numpy.power(2,i)
    return result
