from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product

BANNED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара',
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену товара',
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['checkbox'].widget.attrs.update({
            'class': 'form-label',
        })

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_name(self):

        name = self.cleaned_data.get('name')

        for word in name.split():
            if word.lower() in BANNED_WORDS:
                self.add_error('name', f'Название не может содержать слово "{word}".')
            return name

    def clean_description(self):

        description = self.cleaned_data.get('description')

        for word in description.split():
            if word.lower() in BANNED_WORDS:
                self.add_error('description', f'Описание не может содержать слово "{word}".')
            return description

    def clean_price(self):

        price = self.cleaned_data.get('price')

        if float(price) < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_checkbox(self):

        checkbox = self.cleaned_data.get('checkbox')

        if checkbox == False:
            raise ValidationError('Это обязательное поле для заполнения')
        return checkbox

    def clean_image(self):

        image = self.cleaned_data.get('image')
        image_size = image.size
        image_name = image.name
        max_size = 5 * 1024 * 1024

        if image_size > max_size:
            raise ValidationError('Размер файла не должен превышать 5МБ')

        elif not (image_name.endswith('png') or image_name.endswith('jpg')):
            raise ValidationError('Формат файла должен быть PNG или JPEG')

        return image


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-label'
            field.widget.attrs['class'] = 'form-control'
