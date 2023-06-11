from Candidate import Candidate_List



class Rank(Candidate_List):

    Specialization: str = ''
    experience: int = 0

    def __init__(self):
        self.class_type = 2

    def __str__(self):
        return f'{self.name},  {self.age}, {self.Specialization}, {self.experience}'

    def Show(self):
        return "Ранговые правки"

    def Input(self, io):
        Candidate_List.Input(self, io)
        self.Specialization = io.Input('Specialization')
        self.experience = int(io.Input('experience'))

    def DBLoad(self, r):
        Candidate_List.DBLoad(self, r)
        self.Specialization = r['Specialization']
        self.experience = r['experience']

    def DBStore(self, db):
        if not self.id or int(self.id) == 0:
            db.execute("insert into Candidates values(NULL, ?, ?, ?, ?, Null, Null, 2)",
                       (self.name, self.age, self.Specialization, self.experience))
        else:
            db.execute("update Candidates set name = ?, age = ?, Specialization = ?, experience = ?, class_type = 2 where id = ?",
                       (self.name, self.age, self.Specialization, self.experience, self.id))