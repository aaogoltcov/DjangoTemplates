from django import template

register = template.Library()


@register.filter
def get_color(value):
    try:
        if float(value) < 0.0:
            return '#008000'
        elif 1.0 < float(value) <= 2.0:
            return '#FFA07A'
        elif 2.0 < float(value) <= 5.0:
            return '#FF6347'
        elif float(value) > 5.0:
            return '#FF4500'
        else:
            return 'FFFFFF'
    except ValueError:
        return 'FFFFFF'
