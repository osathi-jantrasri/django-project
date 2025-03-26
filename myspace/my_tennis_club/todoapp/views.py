from rest_framework import permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]