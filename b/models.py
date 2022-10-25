from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
# Esta carpeta es para especificar que queremos guardar en la base de datos
class pro(models.Model):
    id = models.AutoField(primary_key=True)
    title = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='port/images')
    url = URLField(blank=True)

# Create your models here.
