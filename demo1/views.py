from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.urls import reverse
from django.views import View

from . import models
from .forms import PlayerScoreRankingFrom, RegForm


### 登录
def login(request):
    error = ''
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = models.Users.objects.filter(username=uname, password=pwd
                                               ).first()
        if not user_obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

        request.session['user_id'] = user_obj.pk
        request.session['is_login'] = True

        return redirect(reverse('client_list'))

    return render(request, 'login.html', {'error': error})


### 注册
def register(request):
    reg_obj = RegForm()

    if request.method == 'POST':
        reg_obj = RegForm(request.POST)
        if reg_obj.is_valid():
            reg_obj.save()
            return redirect('login')

    return render(request, 'register.html', {'reg_obj': reg_obj})


### 上传分数
def upload_grade(request):
    customer_form_obj = PlayerScoreRankingFrom(request)

    if request.method == 'POST':
        customer_form_obj = PlayerScoreRankingFrom(request, request.POST)
        if customer_form_obj.is_valid():
            customer_form_obj.save()

            # 排名表数据更新
            grade_soreted = [p_obj.id for p_obj in models.PlayerScoreRanking.objects.all().order_by('-grade')]
            n = 1
            for gs in grade_soreted:
                gs.user.rank = n
                n += 1
            return redirect('client_list')
    return render(request, 'upload_grade.html', {'customer_form_obj': customer_form_obj})


### 展示 + 搜索
class Customer_list(View):

    def get(self, request):
        all_customers = models.PlayerScoreRanking.objects.all().order_by('-grade')

        return render(request, 'search_grade.html',
                      {'all_customers': all_customers, })

    def post(self, request,*args,**kwargs):
        start = self.request.POST.get('start', '')
        end = self.request.POST.get('end', '')
        if start.isdecimal() and end.isdecimal():
            all_customers = models.PlayerScoreRanking.objects.all().order_by('-grade')[int(start)-1:int(end)]
        else:
            # 默认展示的条数
            all_customers = models.PlayerScoreRanking.objects.all().order_by('-grade')[:settings.DEFAULT_ITEMS]

        return render(request, 'search_grade.html',
                      {'all_customers': all_customers, })