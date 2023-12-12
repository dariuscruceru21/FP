from modelle.dish import Dish

class Cooked_Dish(Dish):
    def __init__(self, id, portionsize, price, prep_time):
        self.prep_time = prep_time
        Dish.__init__(self, portionsize, price, id)
