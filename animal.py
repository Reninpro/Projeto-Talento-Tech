from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade

    @abstractmethod
    def mostrar(self):
        pass

    def Get_nome(self):
        return self.__nome

    def Get_idade(self):
        return self.__idade

    def Set_nome(self, nome):
        self.__nome = nome

    def Set_idade(self, idade):
        self.__idade = idade