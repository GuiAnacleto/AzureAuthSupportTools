from uuid import uuid4

class User:
    __id: str
    __name: str
    __age: int

    def __init__(self, name: str = "Anonimous", age: int = 0):
        self.__id = uuid4()
        self.__name = name
        self.__age = age

    def get_userid(self, ) -> str:
        return self.__id

    def get_username(self, ) -> str:
        return self.__name
    
    def get_userage(self, ) -> str:
        return self.__age