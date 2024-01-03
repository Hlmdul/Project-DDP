import math


class Bilangan: # Superclass
    def __init__(self, bilangan):
        self.string = str(bilangan)
        self.bilangan = bilangan

    def toDesimal(self):
        # raw_desimal = int(self.desimal)
        # raw_string_desimal = str(raw_desimal)
        # string_desimal = raw_string_desimal[2:len(raw_string_desimal)+1]
        # return string_desimal
        return self.desimal

    def toBiner(self):
        raw_biner = bin(self.desimal)
        raw_string_biner = str(raw_biner)
        string_biner = raw_string_biner[2:len(raw_string_biner)+1]
        return string_biner

    def toOktal(self):
        raw_oktal = oct(self.desimal)
        raw_string_oktal = str(raw_oktal)
        string_oktal = raw_string_oktal[2:len(raw_string_oktal)+1]
        return string_oktal

    def toHexa(self):
        raw_hexa = hex(self.desimal)
        raw_string_hexa = str(raw_hexa)
        string_hexa = raw_string_hexa[2:len(raw_string_hexa)+1]
        return string_hexa
    
class Desimal(Bilangan): # Subclass
    def __init__(self, bilangan):
        super().__init__(bilangan)
        self.desimal = int(self.string, 10)

    
class Biner(Bilangan):
    def __init__(self, bilangan):
        super().__init__(bilangan)
        self.desimal = int(self.string, 2)

    
class Oktal(Bilangan):
    def __init__(self, bilangan):
        super().__init__(bilangan)
        self.desimal = int(self.string, 8)

class Hexa(Bilangan):
    def __init__(self, bilangan):
        super().__init__(bilangan)
        self.desimal = int(self.string, 16)

    


