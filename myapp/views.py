from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.

def home(request):
    return render(request, 'index.html', locals())

def product(request):
    media_root = settings.MEDIA_ROOT
    relative_path = os.path.join(media_root)
    url = [
        {
            "name" : "點心推薦-虎尾地瓜球",
            "address" : "632雲林縣虎尾鎮忠孝路210號",
            "TEL" : "0930035031",
            "url" : "https://maps.app.goo.gl/y1RwDngYGndkXVDN9",
            "menu" : os.path.join(relative_path, "地瓜球菜單.png"),
            "img" : os.path.join(relative_path, "地瓜球.png")
        },
        {
            "name" : "點心推薦-虎尾韭菜盒子",
            "address" : "632雲林縣虎尾鎮中正路102號",
            "url" : "https://maps.app.goo.gl/rs4PdPzGoqVk8Sss9",
            "menu" : os.path.join(relative_path, "韭菜盒子菜單"),
            "img" : os.path.join(relative_path, "韭菜盒子")
        },
        {
            "name" : "點心推薦-虎技紅豆餅",
            "address" : "632雲林縣虎尾鎮文化路64號",
            "url" : "https://maps.app.goo.gl/SqNfbGge6G8cVi2x5",
            "TEL" : "0963354992",
            "menu" : os.path.join(relative_path, "虎技紅豆餅菜單"),
            "img" : os.path.join(relative_path, "虎技紅豆餅")
        },
        {
            "name" : "天氣太熱時來一碗-虎尾榕樹下 綿綿冰",
            "address" : "632雲林縣虎尾鎮四維街35-5號",
            "url" : "https://maps.app.goo.gl/F4r2d3WRXGne8psR9",
            "TEL" : "056365310",
            "menu" : os.path.join(relative_path, "冰菜單"),
            "img" : os.path.join(relative_path, "冰")
        },
        {
            "name" : "50元便當-鮮如美",
            "address" : "632雲林縣虎尾鎮工專路122號",
            "url" : "https://maps.app.goo.gl/2NEhdDydougBN4wU6",
            "menu" : os.path.join(relative_path, "鮮如美菜單"),
            "img" : os.path.join(relative_path, "鮮如美")
        },
        { 
            "name" : "虎尾王家當歸鴨肉麵線",
            "address" : "632雲林縣虎尾鎮民生路37-8號37-9號",
            "TEL" : "056314629",
            "url" : "https://maps.app.goo.gl/Q6mpNHUrNrw9tZd57",
            "menu": os.path.join(relative_path, "當歸菜單"),
            "img" : os.path.join(relative_path, "當歸"),
        },
    ]
    print(relative_path)
    return render(request, 'product.html', {"url" : url})