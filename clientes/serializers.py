from clientes.models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome só aceita caracteres alfabéticos")
        return nome
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos.")
        return rg
    
    def validate_tel(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular deve ter o DD e o 9 antes do número, mais que 11 dígitos")
        return celular
