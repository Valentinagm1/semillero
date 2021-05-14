from wtforms import Form
from wtforms import StringField, TextField, SelectField, IntegerField
from wtforms import validators
from wtforms.fields.html5 import EmailField


class Datos(Form):
    nombre_dante = StringField('Nombre',
    [
        validators.length(min=3, max=10, message='ingrese un nombre valido'),
        validators.Required(message='este dato es necesario')
    ])
    apellido_dante = StringField('Apellido',
    [
        validators.length(min=3, max=15, message='ingrese un apellido valido'),
        validators.Required(message='este dato es necesario')
    ])
    identidad_dante = StringField('Número de identidad',
    [
        validators.length(min=6, max=15, message='ingrese un número de identidad valido'),
        validators.Required(message='este dato es necesario')
    ])
    correo_dante = EmailField('Correo electrónico')

    genero_dante = SelectField(u'Genero', choices=[('m', 'Masculino'), ('f', 'Femenino')])

    #APODERADO
    nombre_rado = StringField('Nombre',
    [
        validators.length(min=3, max=10, message='ingrese un nombre valido'),
        validators.Required(message='este dato es necesario')
    ])
    apellido_rado = StringField('Apellido',
    [
        validators.length(min=3, max=15, message='ingrese un apellido valido'),
        validators.Required(message='este dato es necesario')
    ])
    identidad_rado = StringField('Número de identidad',
    [
        validators.length(min=6, max=15, message='ingrese un número de identidad valido'),
        validators.Required(message='este dato es necesario')
    ])
    correo_rado = EmailField('Correo electrónico')
    carnet = StringField('Carnet')
    genero_rado = SelectField(u'Genero', choices=[('m', 'Masculino'), ('f', 'Femenino')])

    #Eemadn
    nombre_contra= StringField('Nombre',
    [
        validators.length(min=3, max=10, message='ingrese un nombre valido'),
        validators.Required(message='este dato es necesario')
    ])
    apellido_contra = StringField('Apellido',
    [
        validators.length(min=3, max=15, message='ingrese un apellido valido'),
        validators.Required(message='este dato es necesario')
    ])
    identidad_contra = StringField('Número de identidad',
    [
        validators.length(min=6, max=15, message='ingrese un número de identidad valido'),
        validators.Required(message='este dato es necesario')
    ])
    correo_contra = EmailField('Correo electrónico')

    genero_contra = SelectField(u'Genero', choices=[('m', 'Masculino'), ('f', 'Femenino')])