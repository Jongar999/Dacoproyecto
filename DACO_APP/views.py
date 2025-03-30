from django.shortcuts import render

def mi_vista(request):
    return render(request, 'daco/index.html')  # Usa 'daco/index.html'
