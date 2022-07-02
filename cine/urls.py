from django.contrib import admin
from django.urls import path, include
from peliculas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('peliculas/', include('peliculas.urls'))
]
