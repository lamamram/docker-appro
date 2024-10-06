"""
module hosting class Client
"""
from datetime import datetime
from bank.factories import store
from time import sleep
from random import randint


class Person:
    """
    class handling a person

    puclic methods
    --------------

    get_full_name -> str
    """

    def __init__(self, first, last):
        self.firstname =first
        self.lastname = last
    
    def get_full_name(self) -> str:
        sleep(randint(1,3))
        return f"{self.firstname.capitalize()} {self.lastname.upper()}"


class Client(Person):
    """
    class handling a bank Client

    puclic methods
    --------------

    show_balance() -> str
    show_overdraft() -> bool
    """

    _date_format = "%Y-%m-%d"
    _model = "clients"

    def __init__(self, _id, source="json", _format=""):
        self.__id = _id
        data = store.get_factory(source, self._model).get_model(self.__id)
        super().__init__(data["firstname"], data["lastname"])
        self.date_joint = datetime.strptime(data["date_joint"], _format or self._date_format)


    def getDateJoint(self, _format=""):
        return self.date_joint if not _format else self.date_joint.strftime(_format) 


