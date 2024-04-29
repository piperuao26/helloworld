from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo

class TodoList(generics.ListAPIView):
# ListAPIView requires two mandatory attributes, serializer_class and
# queryset.
# We specify TodoSerializer which we have earlier implemented
    serializer_class = ToDoSerializer

def get_queryset(self):
    user = self.request.user
    return ToDo.objects.filter(user=user).order_by('-created')

