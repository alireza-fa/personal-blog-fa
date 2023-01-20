from core.models import AboutMe


def about_me(request):
    return {"me": AboutMe.objects.first()}
