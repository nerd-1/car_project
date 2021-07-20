"""car_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data.views import CarGenericView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("<pk>/", CarGenericView.as_view({'get': 'retrieve'})),
    path("", CarGenericView.as_view({'get':'list', 'post': 'create'}))
]

import socketserver
import struct
import threading
from data.models import Cardata, CardataRecord

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        # conn.sendall(b"Welcome to login...")
        print("Client connect...")
        while True:
            print("Waitting for recving message...")
            # 接收消息
            message = conn.recv(1024)
            s = struct.Struct("iiiiii")
            data = s.unpack(message)
            print(data)
            context = {}
            context['car_id'] = data[0]
            context['front_left'] = data[1]
            context['front_right'] = data[2]
            context['back_left'] = data[3]
            context['back_right'] = data[4]
            context['co'] = data[5]
            Cardata.objects.update_or_create(**context)
            CardataRecord.objects.create(**context)
            print("保存/更新成功！")
            print("数据也保存成功啦！")

def server_thread():
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 6000), MyServer)
    server.serve_forever()

t = threading.Thread(target=server_thread)
t.start() 