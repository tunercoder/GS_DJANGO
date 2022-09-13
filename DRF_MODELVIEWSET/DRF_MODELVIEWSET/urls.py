from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename='student')
router.register('studentroapi',views.StudentReadOnlyViewSet,basename='studentro')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
