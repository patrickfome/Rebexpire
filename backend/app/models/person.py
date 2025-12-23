class Person:
    def __init__(self, id, name, relation=None):
        self.id = id
        self.name = name
        self.relation = relation
        self.documents = []
