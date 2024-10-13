from django.shortcuts import render, get_object_or_404
from .models import City, Category, Landmark, Restaurant, Hotel

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
    
    top_landmarks = Landmark.objects.order_by('-rating')[:3]
    y = [1, 2, 3, 4, 5]

    context = {
        'top_landmarks': top_landmarks,
        'y': y
    }

    return render(request, 'index.html', context)

def landmark_detail(request, landmark_id):

    landmark = get_object_or_404(Landmark, id=landmark_id)

    return render(request, 'landmark_detail.html', {'landmark': landmark})

def guide_view(request):
    date = request.GET.get('date')
    selected_cities = request.GET.getlist('cities')  # Use getlist for multiple selections
    selected_categories = request.GET.getlist('categories')

    # Initialize landmarks, hotels, and restaurants as empty lists
    landmarks = []
    hotels = []
    restaurants = []
    y = [1, 2, 3, 4, 5]

    # Fetch cities and categories for the form
    cities = City.objects.all()
    categories = Category.objects.all()

    # Only filter if form is submitted
    if date and selected_cities and selected_categories:
        landmarks = Landmark.objects.filter(city__id__in=selected_cities, category__id__in=selected_categories)
        hotels = Hotel.objects.filter(city__id__in=selected_cities).order_by('-rating')[:5]
        restaurants = Restaurant.objects.filter(city__id__in=selected_cities).order_by('-rating')[:5]

    context = {
        'landmarks': landmarks,
        'hotels': hotels,
        'restaurants': restaurants,
        'date': date,
        'cities': cities,
        'categories': categories,
        'selected_cities': selected_cities,  # Pass the selected cities
        'selected_categories': selected_categories,  # Pass the selected categories
        'form_submitted': bool(landmarks or hotels or restaurants),
        'y': y
    }
    return render(request, 'guides.html', context)

def about(request):
    return render(request, 'about.html')

def premium(request):
    return render(request, 'premium.html')