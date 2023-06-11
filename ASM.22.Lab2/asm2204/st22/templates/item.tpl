Имя: {{it.name}}<br>
Возраст: {{it.age}}<br>
{% if it.__class__.__name__ == "Achievements" %}
	Военные операции:	{{it.Military_operations}}<br>
	Награды:		 	{{it.Rewards}}<br>
	{% elif it.__class__.__name__ == "Rank"	%}		
	Специализация: 		{{it.Specialization}}<br>
	Опыт:		   		{{it.experience}}<br>		
{% endif %}
<a href="/showform/{{it.id}}">Edit</a>
<a href="/delete/{{it.id}}">Delete</a>
<br><br><br><br>