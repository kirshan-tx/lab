class Account:
    def __init__(self, name: str) -> None:
        """
        Initializes object with given account name and a default account balance of 0

        :param name: Account name
        :return: None
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Takes an amount to add to the account balance

        :param amount: Amount to be deposited
        :return: True if successful and False if not
        """

        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Takes an amount to subtract from the account balance

        :param amount: Amount to be withdrawn
        :return: True if successful and False if not
        """

        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> str:
        """
        Returns the account balance

        :return: current account balance
        """

        return self.__account_balance

    def get_name(self) -> str:
        """
        Returns the account name

        :return: current account name
        """
        return self.__account_name