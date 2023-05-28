from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
import requests

def get_books(request):
    # Get book data from external API
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    headers = {"accept": "text/plain; v=1.0"}
    response = requests.get(url, headers=headers)
    books_data = response.json()

    context = {
        'books': books_data
    }
    return render(request, 'books.html', context)

def get_book_by_id(request):
    if request.method == 'POST':
        book_id = request.POST.get('id')
        url = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{book_id}"
        headers = {
            "accept": "text/plain;v=1.0"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            book_data = response.json()
            return render(request, 'book_detail.html', {'book': book_data})
        else:
            error_message = 'Failed to fetch the book'
            return render(request, 'get_book.html', {'error_message': error_message})

    return render(request, 'get_book.html')

@api_view(['GET', 'POST'])
def create_book(request):
    if request.method == 'POST':
        # Extract book data from the request
        book_data = {
            "id": request.POST.get("id"),
            "title": request.POST.get("title"),
            "description": request.POST.get("description"),
            "pageCount": request.POST.get("pageCount"),
            "excerpt": request.POST.get("excerpt"),
            "publishDate": request.POST.get("publishDate"),
        }

        # Send a POST request to the external API to create a book record
        url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=book_data, headers=headers)

        if response.status_code == 201:
            created_book = response.json()
            return render(request, 'create_book.html', {'created_book': created_book})
        else:
            error_message = {"error": "Failed to create the book"}
            return render(request, 'create_book.html', {'error_message': error_message})

    # Handle the case when the request method is GET
    return render(request, 'create_book.html')

def delete_book(request, book_id):
    if request.method == 'POST':
        url = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{book_id}"
        headers = {
            "accept": "*/*"
        }
        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            return redirect('get_books')
        else:
            error_message = 'Failed to delete the book'
            return render(request, 'delete_book.html', {'book_id': book_id, 'error_message': error_message})

    return render(request, 'delete_book.html', {'book_id': book_id})
