from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<str:id>", views.listing, name="listing"),
    path("watchlist/", views.watch_list, name="watch_list"),
    path("closebid/<str:id>", views.closebid, name="closebid"),
    path("categories/", views.categories, name="categories"),
    path("category/<str:category>", views.detail_category, name="detail_category"),
    path("winning_list", views.winning_list, name="winning_list"),
]