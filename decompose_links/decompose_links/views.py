from django.shortcuts import redirect


def redirect_view(request):
    return redirect('/api/v1/links/', permanent=True)
