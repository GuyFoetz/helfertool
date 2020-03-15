from django import template

register = template.Library()


@register.filter
def lookup_helpersgifts_delivered(h, key):
    return h['delivered_' + str(key)]


@register.filter
def lookup_helpersgifts_present(h, key):
    return h['present_' + str(key)]


@register.simple_tag
def gifts_for_shift(form, shift):
    return form.deservedgifts_for_shift(shift)


@register.simple_tag
def helper_has_missed_shift(helper, shift):
    return helper.has_missed_shift(shift)
