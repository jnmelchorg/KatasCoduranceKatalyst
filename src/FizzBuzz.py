def fizzbuzz(param: int) -> str:
    if param % 5 == 0 and param % 3 == 0:
        return "FizzBuzz"
    elif param % 5 == 0:
        return "Buzz"
    elif param % 3 == 0:
        return "Fizz"
    else:
        return str(param)
