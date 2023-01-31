from clientes.models import Cliente
from rest_framework import serializers
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Este número de CPF não é válido"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "O nome só aceita caracteres alfabéticos"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos."})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O celular deve seguir este modelo XX XXXXX-XXXX"})
        
        return data
