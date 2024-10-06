from abc import ABC, abstractmethod
import json, os
from base import base_path
from time import sleep
from random import randint

class AbsFactory(ABC):
    @abstractmethod
    def get_model(self, _id):
        pass

class JsonFactory(AbsFactory):

    __EXT = ".json"

    def __init__(self, model, models_path=f"{base_path}/models/"):
        self.__MODELS_PATH = models_path
        self._file = self.__MODELS_PATH + model + self.__EXT
        # if not os.path.exists(models_path):
        #     raise FileNotFoundError(f"{models_path}: wrong path !")
        # if not os.path.exists(self._file):
        #     raise FileNotFoundError(f"{model + self.__EXT}: wrong name !")
    
    def get_model(self, _id):
        with open(self._file) as f:
            return json.loads(f.read())[str(_id)]
    
    def get(self, **fields):
        with open(self._file, "r") as f:
            json_data = json.loads(f.read())
            for _id, obj in json_data.items():
                matches = 0
                for label, value in fields.items():
                    if label in obj and obj[label] == value:
                        matches +=1
                if matches == len(list(fields)):
                    obj["id"] = _id
                    return obj
        return {}

class FactoryStore:

    def __init__(self):
        self._factories = {}

    def register_source(self, source, factory_class):
        self._factories[source] = factory_class

    def get_factory(self, source, model):
        factory = self._factories.get(source)
        if not factory:
            raise ValueError("{source} not implemented !")
        return factory(model)

store = FactoryStore()
store.register_source('json', JsonFactory)


if __name__ == "__main__":
    pass

