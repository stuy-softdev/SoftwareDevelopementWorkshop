## DISCOVERIES
- render_template() can replace fields in a template using Jinja2
```python
from flask import Flask, render_template

render_template( 'template_name', var1="value1", var2=2, ...)
```
- {{ foo }} replaces with the value of foo
- {% for item in collection %} ... {% endfor %} is a for statement

## QUESTIONS / COMMENTS / CONCERNS
