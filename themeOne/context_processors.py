from .models import NavbarItem

def navbar_links(request):
    navbar_items = NavbarItem.objects.filter(is_active=True)

    return {
        'navbar_items': navbar_items
    }

from .models import Footer

def footer_data(request):
    footer = Footer.objects.first()

    return {
        'footer': footer
    }