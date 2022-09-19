from home.models import Logo


def logo_view(request):
    site_logo = Logo.objects.last()

    context = {
        'site_logo': site_logo,
    }
    return context
