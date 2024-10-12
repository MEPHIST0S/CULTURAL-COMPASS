from django.shortcuts import render
from .models import City, Category, Landmark

def landmark_list(request):
    cities = City.objects.all()
    categories = Category.objects.all()
    
    selected_city = request.GET.get('city')
    selected_category = request.GET.get('category')
    
    y = [1, 2, 3, 4, 5]

    # Начинаем с пустого QuerySet для landmarks
    landmarks = Landmark.objects.none()

    # Проверяем, были ли выбраны город или категория
    if selected_city or selected_category:
        landmarks = Landmark.objects.all()  # Загружаем все, если есть выбор
        if selected_city and selected_city != "None":  # Проверяем, выбран ли город
            landmarks = landmarks.filter(city__id=selected_city)
        if selected_category and selected_category != "None":  # Проверяем, выбрана ли категория
            landmarks = landmarks.filter(category__id=selected_category)

    context = {
        'landmarks': landmarks,
        'cities': cities,
        'categories': categories,
        'selected_city': selected_city,
        'selected_category': selected_category,
        'y': y
    }

    return render(request, 'landmark.html', context)

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')