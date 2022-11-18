from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.api_home),
    # path('fizzbuzz/', include('fizzbuzz.urls'))
]