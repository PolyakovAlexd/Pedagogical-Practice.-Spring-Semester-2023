import os, pickle
from Candidate import Candidate_List

selfpath = 'data/asm2204/st22/'

class PickleStorage:

    def __init__(self, candidate):
        self.candidate = candidate
        try:
            self.Load()
        except:
            self.items = {}
            self.maxid = 0

    def Store(self):
        with open(selfpath + 'list_of_candidates.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def Load(self):
        if not os.path.exists(selfpath):
            os.mkdir(selfpath)
        with open(selfpath + 'list_of_candidates.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def GetItem(self, id):
        if id <= 0:
            return Candidate_List()
        else:
            return self.items[id]

    def Add(self, item):
        if item.id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[item.id] = item

    def Delete(self, id):
        del self.items[id]

    def GetItems(self):
        for (id, item) in self.items.items():
            yield(item)

