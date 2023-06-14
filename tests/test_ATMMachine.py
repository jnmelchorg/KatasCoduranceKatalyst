import pytest

from src.ATMMachine import ATMMachine, Money, InsufficientFundsError


class TestATMMachine:
    def test_request_of_1_returns_1_coin_of_1(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(1)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 1
        assert money[0].type == "coin"

    def test_request_of_2_returns_1_coin_of_2(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(2)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 2
        assert money[0].type == "coin"

    def test_request_of_3_returns_1_coin_of_2_and_1_coin_of_1(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(3)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 2
        assert money[0].type == "coin"
        assert money[1].quantity == 1
        assert money[1].value == 1
        assert money[1].type == "coin"

    def test_request_of_4_returns_2_coins_of_2(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(4)
        assert len(money) == 1
        assert money[0].quantity == 2
        assert money[0].value == 2
        assert money[0].type == "coin"

    def test_request_of_5_returns_1_note_of_5(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(5)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 5
        assert money[0].type == "note"

    def test_request_of_6_returns_1_note_of_5_and_1_coin_of_1(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(6)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 5
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 1
        assert money[1].type == "coin"

    def test_request_of_7_returns_1_note_of_5_and_1_coin_of_2(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(7)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 5
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 2
        assert money[1].type == "coin"

    def test_request_of_10_returns_1_note_of_10(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(10)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"

    def test_request_of_11_returns_1_note_of_10_and_1_coin_of_1(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(11)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 1
        assert money[1].type == "coin"

    def test_request_of_12_returns_1_note_of_10_and_1_coin_of_2(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(12)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 2
        assert money[1].type == "coin"

    def test_request_of_15_returns_1_note_of_10_and_1_note_of_5(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(15)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 5
        assert money[1].type == "note"

    def test_request_of_16_returns_1_note_of_10_and_1_note_of_5_and_1_coin_of_1(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(16)
        assert len(money) == 3
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 5
        assert money[1].type == "note"
        assert money[2].quantity == 1
        assert money[2].value == 1
        assert money[2].type == "coin"

    def test_request_of_17_returns_1_note_of_10_and_1_note_of_5_and_1_coin_of_2(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(17)
        assert len(money) == 3
        assert money[0].quantity == 1
        assert money[0].value == 10
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 5
        assert money[1].type == "note"
        assert money[2].quantity == 1
        assert money[2].value == 2
        assert money[2].type == "coin"

    def test_request_of_20_returns_1_note_of_20(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(20)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 20
        assert money[0].type == "note"

    def test_request_of_30_returns_1_note_of_20_and_1_note_of_10(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(30)
        assert len(money) == 2
        assert money[0].quantity == 1
        assert money[0].value == 20
        assert money[0].type == "note"
        assert money[1].quantity == 1
        assert money[1].value == 10
        assert money[1].type == "note"

    def test_request_of_40_returns_2_notes_of_20(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(40)
        assert len(money) == 1
        assert money[0].quantity == 2
        assert money[0].value == 20
        assert money[0].type == "note"

    def test_request_of_50_returns_1_note_of_50(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(50)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 50
        assert money[0].type == "note"

    def test_request_of_100_returns_1_note_of_100(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(100)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 100
        assert money[0].type == "note"

    def test_request_of_200_returns_1_note_of_200(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(200)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 200
        assert money[0].type == "note"

    def test_request_of_500_returns_1_note_of_500(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(500)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 500
        assert money[0].type == "note"

    def test_request_of_1500_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(1500)
        assert len(money) == 3
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 2
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 1
        assert money[2].value == 100
        assert money[2].type == "note"

    def test_request_of_1800_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(1800)
        assert len(money) == 3
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 2
        assert money[2].value == 100
        assert money[2].type == "note"

    def test_request_of_2200_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(2200)
        assert len(money) == 4
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 2
        assert money[3].value == 50
        assert money[3].type == "note"

    def test_request_of_2750_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(2750)
        assert len(money) == 6
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 12
        assert money[3].value == 50
        assert money[3].type == "note"
        assert money[4].quantity == 2
        assert money[4].value == 20
        assert money[4].type == "note"
        assert money[5].quantity == 1
        assert money[5].value == 10
        assert money[5].type == "note"

    def test_request_of_3120_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(3120)
        assert len(money) == 6
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 12
        assert money[3].value == 50
        assert money[3].type == "note"
        assert money[4].quantity == 20
        assert money[4].value == 20
        assert money[4].type == "note"
        assert money[5].quantity == 2
        assert money[5].value == 10
        assert money[5].type == "note"

    def test_request_of_3610_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(3610)
        assert len(money) == 7
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 12
        assert money[3].value == 50
        assert money[3].type == "note"
        assert money[4].quantity == 20
        assert money[4].value == 20
        assert money[4].type == "note"
        assert money[5].quantity == 50
        assert money[5].value == 10
        assert money[5].type == "note"
        assert money[6].quantity == 2
        assert money[6].value == 5
        assert money[6].type == "note"

    def test_request_of_4105_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(4105)
        assert len(money) == 9
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 12
        assert money[3].value == 50
        assert money[3].type == "note"
        assert money[4].quantity == 20
        assert money[4].value == 20
        assert money[4].type == "note"
        assert money[5].quantity == 50
        assert money[5].value == 10
        assert money[5].type == "note"
        assert money[6].quantity == 100
        assert money[6].value == 5
        assert money[6].type == "note"
        assert money[7].quantity == 2
        assert money[7].value == 2
        assert money[7].type == "coin"
        assert money[8].quantity == 1
        assert money[8].value == 1
        assert money[8].type == "coin"

    def test_request_of_4602_returns_correct_values(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        money = atm.request(4602)
        assert len(money) == 9
        assert money[0].quantity == 2
        assert money[0].value == 500
        assert money[0].type == "note"
        assert money[1].quantity == 3
        assert money[1].value == 200
        assert money[1].type == "note"
        assert money[2].quantity == 5
        assert money[2].value == 100
        assert money[2].type == "note"
        assert money[3].quantity == 12
        assert money[3].value == 50
        assert money[3].type == "note"
        assert money[4].quantity == 20
        assert money[4].value == 20
        assert money[4].type == "note"
        assert money[5].quantity == 50
        assert money[5].value == 10
        assert money[5].type == "note"
        assert money[6].quantity == 100
        assert money[6].value == 5
        assert money[6].type == "note"
        assert money[7].quantity == 250
        assert money[7].value == 2
        assert money[7].type == "coin"
        assert money[8].quantity == 2
        assert money[8].value == 1
        assert money[8].type == "coin"

    def test_request_of_5101_raises_insufficient_funds_error(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        with pytest.raises(InsufficientFundsError):
            atm.request(5101)

    def test_request_works_after_raising_insufficient_funds_error(self):
        self.__define_available_money_for_atm()
        atm = ATMMachine(self.__available_money)
        with pytest.raises(InsufficientFundsError):
            atm.request(5101)
        money = atm.request(100)
        assert len(money) == 1
        assert money[0].quantity == 1
        assert money[0].value == 100
        assert money[0].type == "note"

    def __define_available_money_for_atm(self):
        self.__available_money = []
        self.__available_money.append(Money(2, 500, "note"))
        self.__available_money.append(Money(3, 200, "note"))
        self.__available_money.append(Money(5, 100, "note"))
        self.__available_money.append(Money(12, 50, "note"))
        self.__available_money.append(Money(20, 20, "note"))
        self.__available_money.append(Money(50, 10, "note"))
        self.__available_money.append(Money(100, 5, "note"))
        self.__available_money.append(Money(250, 2, "coin"))
        self.__available_money.append(Money(500, 1, "coin"))
