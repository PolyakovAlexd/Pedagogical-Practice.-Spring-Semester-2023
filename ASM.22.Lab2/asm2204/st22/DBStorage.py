import os, sqlite3
from Achievements import Achievements
from Rank import Rank
from Candidate import Candidate_List

selfpath = 'asm2204/st22/'

class DBStorage:

    def __init__(self, Candidates):
        self.Load()

    def Load(self):
        if not os.path.exists(selfpath):
            os.makedirs(selfpath)
        self.db = sqlite3.connect('container.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.execute("""
                            create table if not exists Candidates(
                            id integer primary key autoincrement,
                            name text,
                            age integer,
                            Specialization text,
                            experience integer,
                            Military_operations integer,
                            Rewards integer,
                            class_type integer
                            )""")
        self.db.row_factory = sqlite3.Row
        self.dbc = self.db.cursor()

    def Store(self):
        self.db.commit()
        self.db.close()

    def GetItem(self, id):
        item = Candidate_List()
        if id > 0:
            self.dbc.execute("select * from Candidates where id = ?", (id,))
            r = self.dbc.fetchone()
            if r is not None and r[7] == 1:
                item = Achievements()
            elif r is not None and r[7] == 2:
                item = Rank()
            if r is not None:
                item.DBLoad(r)
        return item

    def Add(self, item):
        item.DBStore(self.db)

    def Delete(self, id):
        self.db.execute("delete from Candidates where id = ?", (id,))

    def GetItems(self):
        self.dbc.execute("select * from Candidates order by id desc")
        for r in self.dbc:
            if r[7] == 0:
                item = Candidate_List()
            elif r[7] == 1:
                item = Achievements()
            else:
                item = Rank()
            item.DBLoad(r)
            yield (item)
