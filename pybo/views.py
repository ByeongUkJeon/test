from django.shortcuts import render
import json
from rest_framework import viewsets
from pybo.models import User
from pybo.serializers import UserSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def signup(request):

    if request.method == 'POST':
        try:

            InputData = json.loads(request.body)
            try:
                ID_DUPLICATE = User.objects.get(account=InputData['account'])
                if ID_DUPLICATE:
                    return JsonResponse({"message": "ID 중복"})
            except:
                print(InputData)
                serializer_class = UserSerializer(data=InputData)
                if serializer_class.is_valid():
                    serializer_class.save()
                return JsonResponse({"message": "가입 성공"})


        except KeyError:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")

def login(request):

    if request.method == 'POST':
        try:
            InputData = json.loads(request.body)
            try:
                queryset = User.objects.filter(Q(account=InputData['account']) and Q(passwd=InputData['passwd']))

                if queryset:
                    ACCOUNT = User.objects.get(account=InputData['account'])
                    serializer_class = UserSerializer(ACCOUNT,many=False)

                    print(serializer_class.data)
                return JsonResponse(serializer_class.data)
            except:
                print("로그인 X")
                return JsonResponse({"message": "로그인 실패"}, status=400)


        except KeyError:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")



