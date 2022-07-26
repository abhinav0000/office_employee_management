
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emp_app.urls'))   #will include all urls of emp_app
]
