"""
module hosting class Account
"""

from bank.factories import store

class Account:
    """
    class handling a bank account

    puclic methods
    --------------

    show_balance() -> str
    show_overdraft() -> bool
    """

    _model = "accounts"

    def __init__(self, _id, client, source="json"):
        self.__id = _id
        self.__client = client
        data = store.get_factory(source, self._model).get_model(self.__id)
        self.__balance = float(data["balance"])
        self.__updateOverdraft()

    def getBalance(self):
        return self.__balance

    def deposit(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self.__update_balance(value)    

    def withdraw(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self.__update_balance(-value)

    def get_client_name(self):
        return self.__client.get_full_name()

    def __update_balance(self, value):
        self.__balance += value
        self.__updateOverdraft()

    def __updateOverdraft(self):
        self.overdraft = bool(self.__balance < 0)
