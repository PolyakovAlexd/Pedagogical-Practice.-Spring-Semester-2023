from dataclasses import dataclass


@dataclass
class Candidate_List:
    id: int = 0
    name: str = ''
    age: int = 0

    def __init__(self):
        self.class_type = 0

    def __str__(self):
        return f'{self.id}, {self.name}, {self.age}'

    def Show(self):
        return "Таблица кандидата: "

    def Input(self, io):
        self.id = int(io.Input('id'))
        self.name = io.Input('name')
        self.age = int(io.Input('age'))

    def Output(self, io):
        return io.Output(self)

    def DBLoad(self, r):
        self.id = r['id']
        self.name = r['name']
        self.age = r['age']

    def DBStore(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into candidate values (NULL, ?, ?, NULL, NULL, NULL, NULL, 0)",
                       (self.name, self.age))
        else:
            db.execute("update candidate set name = ?, age = ?, Specialization = NULL, experience = NULL, "
                       "Military_operations = NULL, Rewards = NULL, class_type = 0 where id = ?",
                       (self.name, self.age, self.id))