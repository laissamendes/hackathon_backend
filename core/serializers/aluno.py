from rest_framework import serializers
from core.models import Aluno
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(
        required=False,
        read_only=True
    )
    
class AlunoListRetrieveSerializer(ModelSerializer):
    foto = ImageSerializer(required=False)