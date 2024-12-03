from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte) -> None:
        super().__init__(nome, idade)
        self.__porte = porte

    def Get_porte(self):
        return self.__porte

    def Set_porte(self, porte):
        self.__porte = porte

    def mostrar(self):
        return f"O cachorro com o nome {self.Get_nome()}, possui {self.Get_idade()} anos de idade e tem um porte {self.Get_porte()}"
