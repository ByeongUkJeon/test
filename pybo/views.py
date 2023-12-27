from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
# Create your views here.

def post(request, *args, **kwargs):
    try:
        data = json.loads(request.body)
        print(data)
        product_id = data["id"]
        skintype = data["skintype"]

        return render(request, "pybo/index.html", data)
    except KeyError:
        return JsonResponse({"message": KEY_ERROR}, status=400)

def index(request):


    return render(request,"pybo/index.html")
