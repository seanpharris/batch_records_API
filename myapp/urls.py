from django.contrib import admin
from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from myapi.views import BatchJobsViewSet

router = routers.DefaultRouter()
router.register('batch_jobs', BatchJobsViewSet, basename='batch_jobs')

urlpatterns = [
    #url('admin/', admin.site.urls),
    url('', include(router.urls)),
]
