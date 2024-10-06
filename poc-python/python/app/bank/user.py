"""
module hosting class UserProxy
"""
from datetime import datetime
from bank.factories import store

class User:
    """
    class handling a user


    get_full_name -> str
    """

    _model = "users"

    def __init__(self, _id, source="json"):
        self._id = _id
        self._factory = store.get_factory(source, self._model)
    
    def get_id(self):
        return self._id



class UserProxy(User):
    """
    class handling a connexion to user
    """

    def __init__(self, user, passwd, source="json"):
        super().__init__(0, source)
        obj = self.__auth(user, passwd)
        if obj:
            self._id = obj["id"]
        

    def __auth(self, user, passwd):
        return self._factory.get(username=user, passwd=passwd)


