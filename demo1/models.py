from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=128, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    rank = models.IntegerField(verbose_name='名次', null=True,blank=True,validators=[MinValueValidator(1)])

    def __str__(self):
        return self.username

class PlayerScoreRanking(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='客户')
    client_port = models.CharField(max_length=128, verbose_name='客户端口')
    #  索引优化
    grade = models.IntegerField(default=0, verbose_name='分数', validators=[MaxValueValidator(10000000), MinValueValidator(1)],db_index=True)

    def __str__(self):
        return f'客户端:{self.client_port} - {self.grade}'

    class Meta:
        verbose_name = '分数登记表'
        verbose_name_plural = verbose_name

