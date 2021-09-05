from django.contrib import admin
from django.urls import path,include

import student

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', include('student.urls', namespace='student'))
    path('student/', include('student.urls'))
]
