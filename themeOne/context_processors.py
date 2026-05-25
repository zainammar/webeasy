from .models import NavbarItem

def navbar_links(request):
    navbar_items = NavbarItem.objects.filter(is_active=True)

    return {
        'navbar_items': navbar_items
    }