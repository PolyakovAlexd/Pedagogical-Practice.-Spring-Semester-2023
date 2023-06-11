from Candidate import Candidate_List



class Achievements(Candidate_List):

    Military_operations: int = 0
    Rewards: int = 0

    def __init__(self):
        self.class_type = 1

    def __str__(self):
        return f'{self.name},  {self.age}, {self.Military_operations}, {self.Rewards}'

    def Show(self):
        return "Правки достижений"

    def Input(self, io):
        Candidate_List.Input(self, io)
        self.Military_operations = int(io.Input('Military_operations'))
        self.Rewards = int(io.Input('Rewards'))

    def DBLoad(self, r):
        Candidate_List.DBLoad(self, r)
        self.Military_operations = r['Military_operations']
        self.Rewards = r['Rewards']

    def DBStore(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into Candidates values(NULL, ?, ?, Null, Null, ?, ?, 1)",
                       (self.name, self.age, self.Military_operations, self.Rewards))
        else:
            db.execute("update Candidates set name = ?, age = ?, Military_operations = ?, "
                       "Rewards = ?, class_type = 1 where id = ?",
                       (self.name, self.age, self.Military_operations, self.Rewards, self.id))