from modelle.identifiable import Identifiable

class Client(Identifiable):
    def __init__(self, id, name, adress):
        self.name = name
        self.adress = adress
        Identifiable.__init__(self, id)
