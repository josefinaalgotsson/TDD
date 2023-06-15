def fizzbuzz(arg):
    if arg % 15 == 0:
        return "fizzbuzz"
    if arg % 3 == 0:
        return "fizz"
    if arg % 5 == 0:
        return "buzz"
    return arg 