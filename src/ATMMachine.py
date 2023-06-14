import copy
import dataclasses
import math


@dataclasses.dataclass
class Money:
    quantity: int = 0
    value: int = 0
    type: str = ""


class InsufficientFundsError(ValueError):
    pass


class ATMMachine:
    def __init__(self, available_money: list[Money]):
        self.__available_notes_and_coins = available_money

    def request(self, amount: int) -> list[Money]:
        available_money_pre_transaction = copy.deepcopy(self.__available_notes_and_coins)
        amount, money = self.__process_request(amount)
        if amount > 0:
            self.__available_notes_and_coins = available_money_pre_transaction
            raise InsufficientFundsError("The ATM machine has not enough money, please go to the nearest atm machine")
        return money

    def __process_request(self, amount):
        money = []
        for available in self.__available_notes_and_coins:
            if 0 < math.floor(amount / available.value) <= available.quantity:
                money.append(Money(quantity=math.floor(amount / available.value),
                                   value=available.value, type=available.type))
                available.quantity -= math.floor(amount / available.value)
                amount -= available.value * math.floor(amount / available.value)
            elif available.quantity > 0 and math.floor(amount / available.value) > 0:
                money.append(Money(quantity=available.quantity, value=available.value,
                                   type=available.type))
                amount -= available.value * available.quantity
                available.quantity = 0
        return amount, money
