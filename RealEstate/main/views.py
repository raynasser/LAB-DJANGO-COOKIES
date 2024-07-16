from django.shortcuts import render, redirect
from django.http import HttpRequest#, HttpResponsett

properties = [
{"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
{"title": "Great home for you in Rimal", "image": "villa2.jpg"},
{"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
{"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]


def home_view(request: HttpRequest):

    theme = request.COOKIES.get('theme', 'dark')
    context = {'theme': theme}
    return render(request, 'main/home.html', context)

    # return render(request, 'main/home.html', {'properties': properties, 'dark_mode': dark_mode})

def properties_view(request):
    theme = request.COOKIES.get('theme', 'dark')
    context = {'theme': theme, 'properties': properties}
    return render(request, 'main/properties.html', context)

def contact(request):
    theme = request.COOKIES.get('theme', 'dark')
    context = {'theme': theme}
    return render(request, 'main/contact.html', context)

def toggle_theme(request):
    theme = request.COOKIES.get('theme', 'dark')
    new_theme = 'light' if theme == 'dark' else 'dark'
    response = redirect('main:home')
    response.set_cookie('theme', new_theme, max_age=365*24*60*60)  # 1 year
    return response


# def toggle_dark_mode(request):

#     response = redirect('home')
#     dark_mode = request.COOKIES.get('dark_mode', 'off')
#     new_mode = 'on' if dark_mode == 'off' else 'off'
#     response.set_cookie('dark_mode', new_mode)

#     return response




