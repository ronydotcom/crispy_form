from django import forms 
from crispy_app.models import*

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=ProductModel
        fields='__all__'
        exclude=['total_price']

        widgets={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

            