from django.urls import path, include

urlpatterns = [
    path('batch_jobs/', include('myapp.urls'))
]
