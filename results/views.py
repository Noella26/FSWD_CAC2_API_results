from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.POST.get("author")
        api_url = f'http://127.0.0.1:8000/book/{title}/{author}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        Book = response.json()
        if response.status_code == 200:
            Book = response.json()
            return render(request, 'results.html', {'Book': Book})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch book results. Check Again!'})
    
        
    return render(request, 'index.html')



