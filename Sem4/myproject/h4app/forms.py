from django.forms import ModelForm, Textarea

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'quantity',
            'img',
        ]
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': f'Описание товара..'})
        }
        labels = {
            'title': 'Наименование',
            'description': '',
            'price': 'Цена',
            'quantity': 'Количество',
            'img': 'Изображение',
        }