{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.username}}
{% endblock %}

{% block body %}
http://{{ domain }}/auth/password-reset-confirm/{{uid}}/{{token}}/
{% endblock %}