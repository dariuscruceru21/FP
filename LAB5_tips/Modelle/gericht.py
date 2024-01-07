from identifizierbar import Identifizierbar

class Gericht(Identifizierbar):
    def __init__(self, portiongrosse, prei, id):
        self.portiongrosse = portiongrosse
