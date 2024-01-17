from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
author = {
       "Имя": "Иван",
       "Отчество": "Петрович",
       "Фамилия": "Иванов",
       "телефон": "8-923-600-01-02",
       "email": "vasya@mail.ru",
}

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]

context = {
    'fruits': ['apple', 'banana', 'cocos']
}

def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "author": author,
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    for item in items:
        if item['id'] == item_id:
            context = {
                'item_name': item['name'],
                'item_quantity': item['quantity'],
            }
            return render(request, "item.html", context)
    return HttpResponseNotFound(f'Item with id={item_id} not found')

def get_items(request):
    context = {
        'items': items,
    }
    return render(request, "items.html", context)