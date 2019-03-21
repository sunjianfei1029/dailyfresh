from django.shortcuts import render

def index(request):
    return render(request,'df_index/index.html')
