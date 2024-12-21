from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, Article
from .serializers import PersonSerializer, ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [BasicAuthentication]  # Запрос логина и пароля
    permission_classes = [IsAuthenticated]          # Только для авторизованных пользователей





class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ApiRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "articles": "http://127.0.0.1:8000/api/articles/",
            "register": "http://127.0.0.1:8000/api/register/"
        })










