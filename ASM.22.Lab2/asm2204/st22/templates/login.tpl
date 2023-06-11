<!DOCTYPE html>
<html>
<head>
    <title>Вход в систему</title>
</head>
<body>
    <h2>Вход в систему</h2>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <form action="{{ url_for('login') }}" method="post">
        <div>
            <label for="username">Имя пользователя:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Пароль:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div>
            <input type="submit" value="Войти">
        </div>
    </form>
</body>
</html>
