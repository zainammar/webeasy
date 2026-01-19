from django import template

register = template.Library()

@register.filter
def images(page):
    # Returns a list of all 4 image fields
    return [page.image1, page.image2, page.image3, page.image4]
