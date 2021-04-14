### 启动项目流程:

- 1. 创建数据库'playerscore', 数据库版本:mysql5.6,

- 2. 修改数据库密码|端口|用户 , 文件流程: PlayerScore-->PlayerScore-->settings.py-->DATABASES 配置项

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'playerscore',
             'USER': 'root',   ### 需要修改
             'PASSWORD': '123', ### 需要修改
             'HOST': '127.0.0.1', ### 酌情修改
             'PORT': 3306
         }
     }
     ```

     

- 3. 在manage.py目录执行命令

     ```python
     python  manage.py makemigrations
     
     python  manage.py migrate
     ```

- 4. 默认登录接口: 本机ip+8000端口

     ```python
     python manage.py runserver 8000
     ```

- 5. 已关闭debug模式,ALLOWED_HOSTS设置为`*`便于访问 

