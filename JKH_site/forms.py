from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Product, Category


class NewUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            "input type":"text",
            "class":"form-control",
            "placeholder":"Введите свой логин"})
    )

    email = forms.CharField(
        label='email',
        widget=forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"Введите адрес электронной почты"})
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            "input type":"text",
            "class":"form-control",
            "placeholder":"Введите пароль"})
    )

    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={
            "input type":"text",
            "class":"form-control",
            "placeholder":"Введите пароль еще раз"})
    )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            "input type":"text",
            "class":"form-control",
            "placeholder":"Введите своё имя",})
    )

    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            "input type":"text",
            "class":"form-control",
            "placeholder":"Введите свою фамилию"})
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
    )
    password = forms.CharField(
        max_length=30,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control"}))

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    company_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    address = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    phone_number = forms.CharField(
        max_length=25,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['company_name', 'company_info', 'photo', 'address', 'phone_number']


class ProductAddingForm(forms.ModelForm):
    product_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    product_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    product_category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите значение")
    product_price = forms.DecimalField(
        max_digits=20,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['product_image', 'product_category', 'product_name', 'product_info', 'product_price',]
