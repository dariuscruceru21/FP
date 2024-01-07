class Student:
    def __init__(self, id, name, adress):
        self.id = id
        self.name = name
        self.adress = adress



    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"id = {self.id} , name = {self.name}, adress = {self.adress}"


