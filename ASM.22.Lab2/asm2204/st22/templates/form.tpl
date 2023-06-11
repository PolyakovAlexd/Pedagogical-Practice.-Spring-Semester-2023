{% extends "base.tpl" %}

{% block content %}
<h2>{{it.Show()}}</h2>

<form action = '/add' method=POST>
<input type=hidden name=id value={{it.id}}>
Имя:<input type=text name=name value={{it.name}}><br>
Возраст:<input type=numeric name=age value={{it.age}}><br>
<br>
Данные для ранга кандидата<br>
<br>
Специализация:<input type=text name=Specialization value={{it.Specialization}}><br>
Опыт:<input type=numeric name=experience value={{it.experience}}><br>
<br>
Данные для достижений кандидата<br>
<br>
Количество военных операций:<input type=numeric name=Military_operations value={{it.Military_operations}}><br>
Количество наград:<input type=numeric name=Rewards value={{it.Rewards}}><br>

<br><input type=submit name="Rank" value="Ввести данные ранга">
<br><input type=submit name="Achievements" value="Ввести данные досижений">
</form>

{% endblock %}