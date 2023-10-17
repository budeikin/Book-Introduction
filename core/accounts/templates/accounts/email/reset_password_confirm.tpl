{% extends "mail_templated/base.tpl" %}

{% block subject %}
    Hello
{% endblock %}

{% block body %}
    http://{{ domain }}/auth/password-reset-confirm/{{ uid }}/{{ token }}/
{% endblock %}
