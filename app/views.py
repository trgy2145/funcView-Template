from django.shortcuts import render

# from django.http import HttpResponse

""" def home(request):
    return HttpResponse("Weicome My Page") """
def home(request):

    context = {
        'title' : 'clarusway',
        'dict1' : {'django': 'best framework'},
        'my_list' : [1,2,3]
    }
    return render(request,"app/home.html",context)
