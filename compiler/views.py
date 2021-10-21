from django.shortcuts import render

def csharp(request):
    return render(request, 'compiler/compiler.html')
