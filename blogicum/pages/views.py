from django.shortcuts import render
from django.views.generic import TemplateView


class AboutPage(TemplateView):
    template_name = 'pages/about.html'

# def about(request):
#     """Рендеринг страницы о проекте."""
#     return render(request, 'pages/about.html')


class RulesPage(TemplateView):
    template_name = 'pages/rules.html'


# def rules(request):
#     """Рендеринг страницы с правилами."""
#     return render(request, 'pages/rules.html')


def permission_denied(request, exception):
    return render(request, "pages/403.html", status=403)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    return render(request, "pages/500.html", status=500)
