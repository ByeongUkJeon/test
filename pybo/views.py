import traceback

from django.shortcuts import render
import json
from rest_framework import viewsets
from pybo.models import User
from pybo.serializers import UserSerializer, TaleSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def idCheck(request):

    if request.method == 'POST':
        InputData = json.loads(request.body)
        try:
            ID_DUPLICATE = User.objects.filter(account=InputData['account'])
            if ID_DUPLICATE:
                print("중복 있따")
                return JsonResponse({"message": "ID_DUPLICATE"})
            else:
                print("아이디 중복 없음!")
                return JsonResponse({"message": "ID_AVAILABLE"})
        except:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")

def nicknameCheck(request):

    if request.method == 'POST':
        InputData = json.loads(request.body)
        try:
            NICKNAME_DUPLICATE = User.objects.filter(account=InputData['nickname'])
            if NICKNAME_DUPLICATE:
                print("닉네임 중복")
                return JsonResponse({"message": "NICKNAME_DUPLICATE"})
            else:
                print("닉네임 중복 없음!")
                return JsonResponse({"message": "NICKNAME_AVAILABLE"})
        except:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")


def signup(request):

    if request.method == 'POST':
        try:

            InputData = json.loads(request.body)
            # try:
            #     ID_DUPLICATE = User.objects.get(account=InputData['account'])
            #     if ID_DUPLICATE:
            #         return JsonResponse({"message": "ID 중복"})
            #except:
            print(InputData)
            serializer_class = UserSerializer(data=InputData)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse({"message": "success"})
            else:
                return JsonResponse({"message": "failure"})



        except KeyError:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")

def login(request):

    if request.method == 'POST':
        try:
            InputData = json.loads(request.body)
            queryset = User.objects.filter(Q(account=InputData['account']) and Q(passwd=InputData['passwd']))

            if queryset:
                ACCOUNT = User.objects.get(account=InputData['account'])
                serializer_class = UserSerializer(ACCOUNT,many=False)
                RDATA = {
                    'member_info' : serializer_class.data,
                    'member_setting' : {"VOICE_TYPE" : "3", "VOICE_SPEED" : "1.0"},
                    'message' : "success",

                }
                print(RDATA)
                return JsonResponse(RDATA)
            else:
                print("로그인 X")
                return JsonResponse({"message": "로그인 실패"})
        except KeyError:
            return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")

def addTale(request):
    if request.method == 'POST':
        # try:

            InputData = json.loads(request.body)
            # try:
            #     ID_DUPLICATE = User.objects.get(account=InputData['account'])
            #     if ID_DUPLICATE:
            #         return JsonResponse({"message": "ID 중복"})
            # except:
            print(InputData)
            serializer_class = TaleSerializer(data=InputData)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse({"message": "UPLOAD_SUCCESS"})
            else:
                return JsonResponse({"message": "FALURE"})
            # if serializer_class.is_valid():
            #     serializer_class.save()
            #     return JsonResponse({"message": "UPLOAD_SUCCESS"})
            # else:
            #     return JsonResponse({"message": "FAILURE"})
        #
        # except KeyError:
        #     return JsonResponse({"message": "연결 오류"}, status=400)
    else:
        return render(request, "pybo/index.html")

