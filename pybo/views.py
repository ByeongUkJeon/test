from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
# Create your views here.



def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)

            return render(request, "pybo/index.html", data)
        except KeyError:
            return JsonResponse({"message": KEY_ERROR}, status=400)


    return render(request,"pybo/index.html")
