from abc import ABC, abstractmethod

class AbstractElevador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # ElevadorJahNoTerreoException
    @abstractmethod
    def descer(self) -> str:
    	pass
    
    # ElevadorCheioException
    @abstractmethod
    def entra_pessoa(self) -> str:
    	pass
    
    # ElevadorJahVazioException
    @abstractmethod
    def sai_pessoa(self) -> str:
    	pass
    
    # ElevadorJahNoUltimoAndarException
    @abstractmethod
    def subir(self) -> str:
    	pass
    
    @property
    @abstractmethod
    def capacidade(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def total_pessoas(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def total_andares_predio(self) -> int:
    	pass
    
    @property
    @abstractmethod
    def andar_atual(self) -> int:
    	pass
    
    @total_andares_predio.setter
    @abstractmethod
    def total_andares_predio(self, total_andares_predio: int):
    	pass

