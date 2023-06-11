from flask import Flask, g, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from FlaskIO import FlaskIO
from Container import Container

app = Flask(__name__)

app.secret_key = 'FUb3&Fbv3(C&Fbv4C7v3(c734b'
login_manager = LoginManager()
login_manager.init_app(app)

# Пример модели пользователя
class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username

# Пример базы данных пользователей
users = {
    'admin': User('admin', 'admin'),
    'user': User('user', 'password')
}

# Функция для получения пользователя по его имени
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


# Роут для отображения формы входа
@app.route('/')
def enter():
    return render_template('login.tpl')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = None
    for u in users.values():
        if u.username == username and u.password == password:
            user = u
            break

    if user:
        login_user(user)
        GetCandidate()  # Сохраняем информацию о текущем пользователе в объекте g
        return redirect(url_for('show_form', id=1))  # Замените 123 на нужное значение id

    else:
        flash('Неверное имя пользователя или пароль', 'error')
        return redirect(url_for('enter'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('enter'))


def GetCandidate():
    if 'Candidate' not in g:
        g.Candidate = Container()
    return g.Candidate

@app.route("/")
@login_required
def Candidate_index():
    return GetCandidate().ShowCandidate()

@app.route("/showform/<int:id>")
@login_required
def show_form(id):
    return GetCandidate().ShowForm(id)

@app.route("/delete/<int:id>")
@login_required
def delete_item(id):
    return GetCandidate().Delete(id)

@app.route("/add", methods = ['POST'])
@login_required
def add():
    return GetCandidate().Add()

@app.teardown_request
@login_required
def teardown_candidate(ctx):
    GetCandidate().storage.Store()

if __name__ == '__main__':
    app.run(debug=True)
