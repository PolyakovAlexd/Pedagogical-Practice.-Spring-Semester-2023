from flask import render_template, request
from PickleStorage import PickleStorage
from Achievements import Achievements
from Rank import Rank
from FlaskIO import FlaskIO
from DBStorage import DBStorage


class Container:
    def __init__(self):
        self.storage = DBStorage(self)
        self.io = FlaskIO(request)

    def ShowForm(self, id):
        return self.storage.GetItem(id).Output(self.io)

    def ShowCandidate(self):
        return render_template('candidate.tpl', items=self.storage.GetItems(),
                               selfurl='/' + request.url_rule.rule.split('/')[1])

    def Add(self):
        class_type = Achievements if request.form.get('Achievements') else Rank
        item = self.storage.GetItem(int(self.io.Input('id')))
        item.__class__ = class_type
        item.class_type = 1 if __class__ == Achievements else 2
        item.Input(self.io)
        self.storage.Add(item)
        return self.ShowCandidate()

    def Delete(self, id):
        self.storage.Delete(id)
        return self.ShowCandidate()