from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Bot:
    
    def __init__(self,command):
        self.command = command

    def set_comand(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

