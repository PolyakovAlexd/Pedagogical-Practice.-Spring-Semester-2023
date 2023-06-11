{% extends "base.tpl" %}

{% block content %}
    {% for it in items %}
        {% include "item.tpl"%}
    {% else %}
        нет кандидатов
    {% endfor %}

{% include "add.tpl"%}
{% endblock %}