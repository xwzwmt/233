"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from myDjango.views import index,chart,chart_dq,chart_pp,bj_chart,gz_chart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('chart/',chart,name='chart'),
    path('chart_dq/', chart_dq, name='chart_dq'),
    path('chart_pp', chart_pp, name='chart_pp'),
    path('bj_chart', bj_chart, name='bj_chart'),
    path('gz_chart', gz_chart, name='gz_chart'),
]
