{% extends 'markdown.tpl' %}

{% block stream %}
``` nb-output
{{ output.text }}
```
{% endblock stream %}

{% block data_text %}
``` nb-output
{{ output.data['text/plain'] }}
```
{% endblock data_text %}

{% block traceback_line  %}
``` nb-output
{{ line | strip_ansi }}
```
{% endblock traceback_line  %}