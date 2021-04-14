from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import reverse, HttpResponse, redirect
from django.conf import settings
import re
from demo1 import models

class CheckLoginMiddleWare(MiddlewareMixin):

    def process_request(self, request):

        if request.path_info == '/login/' or request.path_info == '/register/':
            return

        is_login = request.session.get('is_login')
        if not is_login:
            return redirect('login')

        user_obj = models.Users.objects.filter(pk=request.session.get('user_id')).first()

        request.user_obj = user_obj
