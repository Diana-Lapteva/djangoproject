from django.shortcuts import render, redirect
import urllib.parse

def index(request):
    path_value = "Добро пожаловать!"
    return render(request, "greet.html", {"key": path_value})

def greet(request, path_value): 
    print(path_value)
    context = {"key": path_value}
    return render(request, "greet.html", context)

def search_price(request, path_value=None):
    sorted_items = []
    
    # Получаем данные из URL, если они переданы
    if path_value:
        product_data = urllib.parse.unquote(path_value) 
    else: # если не через ссылку, то через форму
        product_data = request.POST.get('product_data', '')

    if product_data:
        products = product_data.split(";")
        
        price_dict = {}
        for product in products:
            if ":" not in product:
                continue  
            
            name, prices = product.split(":", 1)  
            price_list = list(map(int, prices.split(",")))
            avg_price = sum(price_list) / len(price_list)
            price_dict[name.strip()] = avg_price  

        sorted_items = sorted(price_dict.keys(), key=lambda x: (price_dict[x], x))

    return render(request, 'search_price.html', {'sorted_items': sorted_items, 'default_value': path_value or ''}) 

def money_exchange(request, path_value=None):
    bills = [500, 100, 10, 2] 
    exchange_result = None  # храним результат
    error_message = None  # ошибка

    if path_value is not None:  
        try:
            amount = int(urllib.parse.unquote(path_value))  # Декодируем и преобразуем в число
        except ValueError:
            amount = None
    else:
        amount = request.POST.get('amount')
        if amount:
            try:
                amount = int(amount)
            except ValueError:
                amount = None

    if amount is not None and amount >= 0:
        exchange_result = {}
        remaining_amount = amount  

        for bill in bills:
            exchange_result[bill], remaining_amount = divmod(remaining_amount, bill)

        if remaining_amount > 0:
            exchange_result = None
            error_message = f"Невозможно полностью разменять {amount} руб."

    return render(request, 'money_exchange.html', {
        'exchange_result': exchange_result,
        'error_message': error_message,
        'default_value': path_value or '',
    })



def pages(request, path_value): 
    print("path_value: ", path_value)
    print(request.path)
    context = {"path_value": path_value}
    if path_value == "first":
        return render(request, "search_price.html", context)
    elif path_value == "second":
        return render(request, "money_exchange.html", context)
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
    user_info = {
        'name': 'Лаптева Диана Дмитриевна',
        'photo': 'renderApp/images/me.png',
        'email': 'ddlapteva@edu.hse.ru',
        'phone': '+7 977 111 22 33',
        'program_name': 'Математика',
        'program_description': 'Описание программы: Программа сочетает теоретические основы математики с практическими навыками, что позволяет студентам не только усваивать фундаментальные концепции, но и применять их в реальных научных и практических задачах. Студенты программы изучают широкий спектр дисциплин, включая алгебру, анализ, геометрию, теорию вероятностей и статистику. Также внимание уделяется математической логике и методам численного анализа. Кроме того, программа включает курсы по прикладной математике, что позволяет студентам изучать, как математические методы применяются в различных областях, таких как экономика, информатика, физика и инженерия.',
        'manager': {
            'name': 'Походня Наталья Витальевна',
            'photo': 'renderApp/images/s1.png',
            'email': 'prekrasnayazhenshina@mail.ru',
        },
        'colleagues': [
            {
                'name': 'Ханна Монтана',
                'photo': 'renderApp/images/s2.png',
                'email': 'zhivudvezhizni@gmail.com',
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
