from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re
from utils.validadorCpf import valida_cpf 

# Create your models here.
class Perfil(models.Model):

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, help_text='Digite apenas números')
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.usuario} {self.usuario.email}'

    def clean(self):

        error_msg = {}

        if not valida_cpf(self.cpf):
            error_msg['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_msg['cep'] = 'Informe um CEP válido com 8 digitos'

        if error_msg:
            raise ValidationError(
                error_msg
            )



        