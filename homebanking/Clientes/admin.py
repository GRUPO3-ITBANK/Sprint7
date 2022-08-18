from django.contrib import admin
from .models import Cliente
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Cliente

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = Cliente
#         fields = ('DNI','email','nombre','apellido','fecha_de_nac','tipo_cliente')

#     def clean_password2(self):
#         # Chequeo que las 2 passwords coincidan
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Contraseñas no coinciden")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """Para actualizer cliente. Incluye campos de clientes
#     pero reemplaza el campo de contraseña con contraseña
#     desabilitada
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Cliente
#         fields = ('DNI','email','password','nombre','apellido','fecha_de_nac','tipo_cliente','is_active', 'is_admin')


# class UserAdmin(BaseUserAdmin):
#     # Formularios para agregar y cambiar instancias de usuarios 
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # Campos para ser usados en display User model.
#     list_display = ('DNI','email','nombre','apellido','fecha_de_nac','tipo_cliente', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('DNI', 'password')}),
#         ('Personal info', {'fields': ('email','nombre','apellido','fecha_de_nac','tipo_cliente')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('DNI','email','password','nombre','apellido','fecha_de_nac','tipo_cliente', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('DNI',)
#     ordering = ('DNI',)
#     filter_horizontal = ()


admin.site.register(Cliente)

admin.site.unregister(Group)