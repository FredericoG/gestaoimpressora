from django import forms
from .models import Equipamento, Item, Contador, Troca


class ItemModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.descricao} ({obj.serial})"

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        # Adicionar atributos de dados
        if self.queryset is not None:
            attrs['data-serials'] = ','.join([obj.serial for obj in self.queryset])
            attrs['data-tipos'] = ','.join([obj.tipo for obj in self.queryset])
        return attrs


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['maquina', 'serial', 'tipoeqipopcoes', 'paginaminuto', 'opcaoturno', 'capacidade']
        widgets = {
            'maquina': forms.TextInput(attrs={'placeholder': 'Máquina', 'maxlength': 100, 'required': True}),
            'serial': forms.TextInput(attrs={'placeholder': 'Serial', 'maxlength': 100, 'required': True}),
            'tipoeqipopcoes': forms.Select(),
            'paginaminuto': forms.NumberInput(attrs={'required': True}),
            'opcaoturno': forms.Select(),
            'capacidade': forms.NumberInput(attrs={'required': True}),
        }


class ContadorForm(forms.ModelForm):
    equipamento = forms.ModelChoiceField(queryset=Equipamento.objects.all(), required=True)
    
    class Meta:
        model = Contador
        fields = ['equipamento', 'contador', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['codigo', 'tipo', 'descricao', 'custo', 'durabilidade']
        widgets = {
            'descricao': forms.TextInput(attrs={'required': True}),
        }


class TrocaForm(forms.ModelForm):
    item = ItemModelChoiceField(
        queryset=Item.objects.all(),
        required=True,
        empty_label="Selecione um item",
    )
    
    class Meta:
        model = Troca
        fields = ['equipamento', 'item', 'quantidade', 'contador', 'data_troca']
        widgets = {
            'data_troca': forms.DateInput(attrs={'type': 'date'}),
        }