"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from app.views.index import IndexView
from app.views.log import AppLoginView, AppLogoutView
from app.views.recipe import RecipeListView, RecipeByIngredientListView, RecipeDetailView, RecipeCreateView, \
    RecipeUpdateView, RecipeDeleteView

urlpatterns = []
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("recipe/list", RecipeListView.as_view(), name="recipe_list"),
    path(
        "recipe/by-ingredient/<str:ingredient>",
        RecipeByIngredientListView.as_view(),
        name="recipe_by_ingredient_list",
    ),
    path(
        "recipe/detail<int:pk>",
        RecipeDetailView.as_view(),
        name="recipe_detail",
    ),
    path("recipe/create", RecipeCreateView.as_view(), name="recipe_create"),
    path(
        "recipe/update<int:pk>",
        RecipeUpdateView.as_view(),
        name="recipe_update",
    ),
    path(
        "recipe/delete<int:pk>",
        RecipeDeleteView.as_view(),
        name="recipe_delete",
    ),
    path("login", AppLoginView.as_view(), name="login"),
    path("logout", AppLogoutView.as_view(), name="logout"),
)
