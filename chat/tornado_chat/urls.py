from django.urls import path, include
from django.contrib import admin
from tornado_chat import views

urlpatterns = [
    #url(r'^send_message/$', 'send_message_view'),
    #url(r'^send_message_api/(?P<thread_id>\d+)/$', 'send_message_api_view'),
    #url(r'^chat/(?P<thread_id>\d+)/$', 'chat_view'),
    path('admin/', admin.site.urls),
    path('', views.chat)
]