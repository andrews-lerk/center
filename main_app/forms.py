from django import forms


class DateForm(forms.Form):
    ADULT_CHOICES = (
        ('Кол. взрослых: не выбрано', 'Кол. взрослых: не выбрано'),
        ("1", 1),
        ("2", 2),
    )
    check_in_out = forms.CharField(label='Дата заезда', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': '1',
        'autocomplete': 'off',
        'placeholder': 'Дата заезда - Дата выезда',
        'readonly': True,
    }))
    adult = forms.ChoiceField(choices=ADULT_CHOICES, required=True, widget=forms.Select(attrs={
        'class': 'cs-select cs-skin-elastic',
        'autocomplete': 'off',
    }))

    def clean(self):
        cleaned_data = super().clean()
        check_in_out = cleaned_data.get('check_in_out')
        adult = cleaned_data.get('adult')
        if check_in_out is None or ' - ' not in check_in_out:
            msg = "Введите дату заезда и выезда полностью"
            self.add_error('check_in_out', msg)
        if adult == 'Кол. взрослых: не выбрано':
            msg = "Введите количество взрослых"
            self.add_error('adult', msg)


class SinglePersonalInfoForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    birth_date = forms.DateField(input_formats=['%d/%m/%Y'], required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'birth',
        'readonly': True,
    }))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'phone'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))

class DuoPersonalInfoForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    first_name2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    last_name2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    birth_date = forms.DateField(input_formats=['%d/%m/%Y'], required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'birth',
        'readonly': True,
    }))
    birth_date2 = forms.DateField(input_formats=['%d/%m/%Y'], required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'birth2',
        'readonly': True,
    }))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    city2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
    }))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'id': 'phone'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))
