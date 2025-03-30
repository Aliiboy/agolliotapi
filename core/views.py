from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Vue pour la page d'accueil"""

    template_name = "home.html"


class FlowBiteView(TemplateView):
    """Vue pour la page de Flowbite"""

    template_name = "flowbite.html"
