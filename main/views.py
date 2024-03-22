from django.shortcuts import render

from main.models import Product


def home(request):
    product_list = Product.objects.all
    context = {'object_list': product_list
    }
    return render(request, 'main/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}: {phone}: {message}:')
    return render(request, 'main/contacts.html')