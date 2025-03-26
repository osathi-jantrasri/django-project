from rest_framework import permissions, viewsets
from .models import Member
from .serializers import MemberSerializer
from rest_framework.permissions import AllowAny

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

