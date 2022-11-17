import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account("001-John")

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == "001-John"
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(2) is True
        assert self.a1.get_balance() == 2

        assert self.a1.deposit(-3) is False
        assert self.a1.get_balance() == 2

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 2

        assert self.a1.deposit(1.5) is True
        assert self.a1.get_balance() == pytest.approx(3.5, abs=0.001)

    def test_withdraw(self):
        self.a1.deposit(7)

        assert self.a1.withdraw(5) is True
        assert self.a1.get_balance() == 2

        assert self.a1.withdraw(5) is False
        assert self.a1.get_balance() == 2

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 2

        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == 2
