from rest_framework import viewsets
from core.models import AlunoTemDisciplina
from core.serializers import AlunoTemDisciplinaSerializer


class AlunoTemDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = AlunoTemDisciplina.objects.all()
    serializer_class = AlunoTemDisciplinaSerializer