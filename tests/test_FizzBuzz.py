from src.FizzBuzz import fizzbuzz


class TestFizzBuzz:
    def test_fizz(self):
        assert fizzbuzz(3) == "Fizz"

    def test_buzz(self):
        assert fizzbuzz(5) == "Buzz"

    def test_fizzbuzz(self):
        assert fizzbuzz(15) == "FizzBuzz"

    def test_number(self):
        assert fizzbuzz(7) == "7"

