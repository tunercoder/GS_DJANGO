from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from api.auth import CustomAuthToken 

router = DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('getauthtoken/', tokenviews.obtain_auth_token)
    path('getauthtoken/', CustomAuthToken.as_view()) #for custom token repsonse
]
