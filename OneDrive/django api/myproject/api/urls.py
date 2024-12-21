from django.urls import path
from .views import ApiRootView, PersonListCreateView, ArticleListCreateView

urlpatterns = [
    path('login/', ApiRootView.as_view(), name='api-root'),
    path('register/', PersonListCreateView.as_view(), name='register'),
    path('articles/', ArticleListCreateView.as_view(), name='articles'),
]








