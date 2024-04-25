from django.shortcuts import render, redirect
from .models import Product, News, User, Product, ArchivedProduct
from .forms import ProductForm, UserForm, ContactForm
from django.views.generic import TemplateView
import csv
import os
import requests
from io import BytesIO
from PIL import Image



def index(request):
    news_list = read_news_from_csv()
    return render(request, 'index.html', {'news_list': news_list})

class BaraholkaView(TemplateView):
    template_name = 'baraholka.html'

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    image_name = url.split('/')[-1]
    image_path = os.path.join('media', 'images', image_name)
    img.save(image_path)
    return image_path

def baraholka(request):
    products = Product.objects.all()
    return render(request, 'baraholka.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:baraholka')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    if os.path.exists(product.image.path):
        os.remove(product.image.path)

    archived_product = ArchivedProduct(name=product.name, description=product.description, price=product.price)
    archived_product.save()

    return redirect('myapp:baraholka')

def read_news_from_csv():
    news_list = []
    with open('files4mysite.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            news = {
                'title': row.get('body', ""),
                'content': row.get('url', ""),
                'published_date': row.get('video', "")
            }
            news_list.append(news)
    return news_list
