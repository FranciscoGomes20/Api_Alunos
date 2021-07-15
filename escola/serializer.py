from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg']
