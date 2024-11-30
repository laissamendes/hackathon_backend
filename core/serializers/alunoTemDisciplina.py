from rest_framework import serializers

from core.models import AlunoTemDisciplina


class AlunoTemDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoTemDisciplina
        fields = "__all__"