from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca) -> None:
        super().__init__(nome, idade)

        self.__raca = raca

    def Get_raca(self):
        return self.__raca
    
    def Set_raca(self, raca):
        self.__raca = raca

    def mostrar(self):
        return f"O gato com o nome {self.Get_nome()}, possui {self.Get_idade()} anos de idade e a raça dele é {self.Get_raca()}."
    
pass
