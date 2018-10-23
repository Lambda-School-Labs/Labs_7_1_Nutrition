"""Dont_Eat_That URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.authtoken import views

from rest_framework import routers
from DET_App.api import RecipeViewSet, IngredientsViewSet, NutritionInfoViewSet, UserRecipeViewSet

# To add route, We register it here with the 'r' <- regex and we will not need to add them to urlpatterns
router = routers.DefaultRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'ingredients', IngredientsViewSet)
router.register(r'nutritionInfo', NutritionInfoViewSet)

## Routes will need to be edited to show the proper names for pages, but for now, it renders each schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token),
]
