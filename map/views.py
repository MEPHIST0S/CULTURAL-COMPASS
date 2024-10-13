from django.shortcuts import render
from core.models import Landmark, City, Category

def map_view(request):
    cities = City.objects.all()
    categories = Category.objects.all()
    
    selected_city = request.GET.get('city')
    selected_category = request.GET.get('category')

    # Начинаем с пустого QuerySet для landmarks
    landmarks = Landmark.objects.none()

    if selected_city or selected_category:
        landmarks = Landmark.objects.all()  
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
    }

    return render(request, 'map.html', context)

