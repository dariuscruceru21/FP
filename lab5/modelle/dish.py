from modelle.identifiable import Identifiable

class Dish(Identifiable):
    def __init__(self, id, portionsize, price):
        self.portionsize = portionsize
        self.price = price
        Identifiable.__init__(self, id)
