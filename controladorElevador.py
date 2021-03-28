from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def subir(self) -> str:
        return self.__elevador.subir()

    def descer(self) -> str:
        return self.__elevador.descer()

    def entra_pessoa(self) -> str:
        return self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        return self.__elevador.sai_pessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializar_elevador(
        self, andar_atual: int, total_andares_predio: int,
        capacidade: int, total_pessoas: int
    ):
        if (
                isinstance(andar_atual, int) and
                isinstance(total_andares_predio, int) and
                isinstance(capacidade, int) and
                isinstance(total_pessoas, int)
        ) and (
            andar_atual >= 0 and
            total_andares_predio >= 0 and
            capacidade >= 0 and
            total_pessoas >= 0
        ) and (
            andar_atual <= total_andares_predio and
            total_pessoas <= capacidade
        ):
            self.__elevador = Elevador(
                total_andares_predio, capacidade, andar_atual, total_pessoas)
            return self.__elevador
        else:
            raise ComandoInvalidoException
