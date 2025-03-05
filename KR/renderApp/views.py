from django.shortcuts import render, redirect

def index(request):  # http://127.0.0.1:8000/renderApp/greet/Иванов
    path_value = "Добро пожаловать!"
    return render(request, "greet.html", {"key": path_value})

def greet(request, path_value):  # http://127.0.0.1:8000/renderApp/greet/Иванов
    print(path_value)
    context = {"key": path_value}
    return render(request, "greet.html", context)


def search_price(request):
    if request.method == 'POST':
        # Получаем введенные данные от пользователя
        input_data = request.POST.get('product_data', '')

        # Разбиваем строку на отдельные товары
        items = input_data.split('; ')

        # Создаем список для хранения товаров и их средней цены
        item_prices = []

        # Обрабатываем каждый товар
        for item in items:
            # Разделяем товар на название и цены
            name, prices = item.split(': ')
            prices = list(map(int, prices.split(',')))  # Преобразуем цены в список чисел
            avg_price = sum(prices) / len(prices)  # Считаем среднюю цену
            item_prices.append((name, avg_price))

        # Сортируем по средней цене, если цены одинаковые - по названию товара
        item_prices.sort(key=lambda x: (x[1], x[0]))

        # Получаем отсортированные товары
        sorted_items = [name for name, _ in item_prices]

        # Передаем отсортированные товары в шаблон
        return render(request, 'search_price.html', {'sorted_items': sorted_items})

    return render(request, 'search_price.html')


def money_exchange(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        bills = [100, 50, 20, 10, 5, 2, 1]  # Номиналы
        exchange = {}
        for bill in bills:
            count, amount = divmod(amount, bill)
            if count > 0:
                exchange[bill] = count
        return render(request, 'money_exchange.html', {'exchange': exchange})
    return render(request, 'money_exchange.html')


def pages(request, path_value):  # http://127.0.0.1:8000/renderApp/pages/01
    print("path_value: ", path_value)
    print(request.path)
    context = {"path_value": path_value}
    if path_value == "first":
        return render(request, "search_price.html", context)
    elif path_value == "second":
        return render(request, "money_exchange.html", context)
    # else: return redirect("renderApp:index")
    else:
        return redirect("renderApp:serach_price", path_value)



def objects_arrays(request):
    goods_array = [
        {
            "id": "1",
            "title": "Ferrari SF90 Stradale",
            "vendor_code": "VC111",
            "description": "Мощность: 1000 лошадиных сил",
            "price": 350,
            "img": "renderApp/images/c1.png",
        },
        {
            "id": "2",
            "title": "Lamborghini Aventador SVJ",
            "vendor_code": "VC222",
            "description": "Мощность: 770 лошадиных сил",
            "price": 340,
            "img": "renderApp/images/c2.png",
        },
        {
            "id": "3",
            "title": "Porsche 911 GT3 RS",
            "vendor_code": "VC333",
            "description": "Мощность: 520 лошадиных сил.",
            "price": 400,
            "img": "renderApp/images/с3.png",
        },
        {
            "id": "4",
            "title": "McLaren 720S",
            "vendor_code": "VC444",
            "description": "Мощность: 720 лошадиных сил.",
            "price": 450,
            "img": "renderApp/images/с4.png",
        },
    ]

    box_array = [
        {"title": "Mercedes-Benz 300SL", "description": "Первый спортивный автомобиль западногерманской торговой марки Mercedes-Benz послевоенного периода. Модель впервые была представлена в Нью-Йоркском автосалоне в 1954 году как уличная версия гоночного автомобиля W194.", "img": "renderApp/images/c5.png"},
        {"title": "Cadillac V-16", "description": "Cadillac V16, оснащенный 16-цилиндровым V-образным двигателем. Никогда ранее в серийные автомобили не устанавливались настолько большие моторы. Машина была выпущена во время «Великой Депрессии».", "img": "renderApp/images/c6.png"},
    ]
    print("goods_array: " ,goods_array)
    print ("box_array: ", box_array)
    dict_of_array = {"goods_array": goods_array, "box_array": box_array}
    context = {"dict_of_array": dict_of_array}
    print("context: ", context)
    return render(request, "objects_arrays.html", context)

from django.shortcuts import render

def programm_info(request):
    # Пример словаря с данными для страницы
    user_info = {
        'name': 'Лаптева Диана Дмитриевна',
        'photo': 'renderApp/images/me.png',
        'email': 'ddlapteva@edu.hse/ru',
        'phone': '+7 977 111 22 33',
        'program_name': 'Математика',
        'program_description': 'Описание программы: очень изучаем математику.',
        'manager': {
            'name': 'Походня Наталья Витальевна',
            'photo': 'renderApp/images/s1.png',
            'email': 'prekrasnayazhenshina@mail.ru',
        },
        'colleagues': [
            {
                'name': 'Ханна Монтана',
                'photo': 'renderApp/images/s2.png',
                'email': 'zhbvudvezhizni@gmail.com',
                'phone': '+7 987 654 3210'
            },
            {
                'name': 'Доктор Хаус',
                'photo': 'renderApp/images/s4.png',
                'email': 'mrdr@best.ru',
                'phone': '+7 999 123 4567'
            },
        ]
    }

    return render(request, 'programm_info.html', {'user_info': user_info})
