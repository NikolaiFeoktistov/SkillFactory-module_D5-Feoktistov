from django import template


register = template.Library()

censor_words = {
    'плохое': 'хорошее',
    'нежелательное': 'желательное',
    'нецензурное': 'цензурное',
}


@register.filter(name='censor')
def censor(value):
    censored_text = value
    for word, replacement in censor_words.items():
        censored_text = censored_text.replace(word, replacement)
    return censored_text
