from flask import render_template, request


class FlaskIO:

    def __init__(self, request):
        self.form = request.form

    def Input(self, field):
        return self.form.get(field)

    def Output(self, item):
        return render_template('form.tpl', it=item, selfurl='/' + request.url_rule.rule.split('/')[1])