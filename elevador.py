from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(
        self, total_andares_predio: int, capacidade_max: int,
        andar_atual: int, total_pessoas: int
    ):
        self.__total_andares_predio = total_andares_predio
        self.__capacidade_max = capacidade_max
        self.__andar_atual = andar_atual
        self.__total_pessoas = total_pessoas

    def descer(self) -> str:
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            return 'O elevador desceu um andar'
        else:
            raise ElevadorJahNoTerreoException

    def entra_pessoa(self) -> str:
        if self.__total_pessoas < self.__capacidade_max:
            self.__total_pessoas += 1
            return 'Uma pessoa entrou no elevador'
        else:
            raise ElevadorCheioException

    def sai_pessoa(self) -> str:
        if self.__total_pessoas > 0:
            self.__total_pessoas -= 1
            return 'Uma pessoa saiu do elevador'
        else:
            raise ElevadorJahVazioException

    def subir(self) -> str:
        if self.__andar_atual < self.__total_andares_predio:
            self.__andar_atual += 1
            return 'O elevador subiu um andar'
        else:
            raise ElevadorJahNoUltimoAndarException

    @property
    def capacidade(self) -> int:
        return self.__capacidade_max

    @property
    def total_pessoas(self) -> int:
        return self.__total_pessoas

    @property
    def total_andares_predio(self) -> int:
        return self.__total_andares_predio

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
        self.__total_andares_predio = total_andares_predio
