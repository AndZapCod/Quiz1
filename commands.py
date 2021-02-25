from bot import Command

class Encender(Command):
    
    def __init__(self):
        self.message = 'ON'

    def execute(self):
        print(self.message)

class Apagar(Command):
    
    def __init__(self):
        self.message = 'OFF'

    def execute(self):
        print(self.message)

class Hablar(Command):
    
    def __init__(self):
        self.message = 'Hi!'

    def execute(self):
        print(self.message)

class Dormir(Command):
    
    def __init__(self):
        self.message = 'zzZ'

    def execute(self):
        print(self.message)