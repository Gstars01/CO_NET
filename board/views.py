from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reqeust):
    return HttpResponse("안녕하세요 board에 오신걸 환영합니다")