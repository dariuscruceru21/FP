from modelle.dish import Dish

class Drink(Dish):
    def __init__(self, id,  portionsize, price, alcohol_volume):
        self.alcohol_volume = alcohol_volume
        Dish.__init__(self, portionsize, price, id)
