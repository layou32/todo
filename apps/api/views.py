from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from apps.todos.models import Todo

# Create your views here.
class TodosViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()