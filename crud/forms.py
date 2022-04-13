from django.forms import ModelForm
from crud.models import Patrimonios

# Create the form class.


class PatrimoniosForm(ModelForm):
    class Meta:
        model = Patrimonios
        fields = ['ETIQUETA', 'RESPONSAVEL', 'CPF_DO_RESPONSAVEL', 'DESCRICAO_DO_EQUIPAMENTO', 'MARCA', 'MODELO',
                  'NUMERO_DE_SERIE', 'NUMERO_DA_NOTA_FISCAL', 'LOCALIZACAO', 'PROJETO', 'ANO_DO_PROJETO', 'EMPRESA_PATROCINADORA']
