{% extends 'markdown.tpl' %}


{% block stream %}
{{ '{{< output >}}' }}
```nb-output
{{ output.text }}
```
{{ '{{< /output >}}' }}
{% endblock stream %}



{% block data_text %}
{{ "{{< output >}}" }}
```nb-output
{{ output.data['text/plain'] }}
```
{{ "{{< /output >}}" }}
{% endblock data_text %}



{% block traceback_line  %}
{{ "{{< output >}}" }}
```nb-output
{{ line | strip_ansi }}
```
{{ "{{< /output >}}" }}
{% endblock traceback_line  %}