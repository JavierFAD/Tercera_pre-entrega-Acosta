from django.db import models

class Lider(models.Model):
    nombre      = models.CharField(max_length=50,blank=True,null=True)
    apellido    = models.CharField(max_length=50)
    legajo      = models.IntegerField()
    sector      = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.apellido +', '+ self.nombre + ' | ' + str(self.legajo)
    

class Operario(models.Model):
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    legajo      = models.IntegerField()
    lider       = models.CharField(max_length=50, null=False, blank=False)
    funcion     = models.TextField()
    descripcion = models.TextField(default='descripción adicional')
    
    def __str__(self) -> str:
        return self.apellido + ', ' + self.nombre+ ' | ' + str(self.legajo) + ' | ' + self.lider
    
class Herramienta(models.Model):
    nombre      = models.CharField(max_length=50)
    rastreo     = models.IntegerField()
    calibracion = models.DateField()
    operario    = models.CharField(max_length=40)
    descripcion  = models.TextField()
    
    def __str__(self) -> str:
        return self.nombre + ' | ' + str(self.rastreo) + ' | ' + self.operario + ' --> calibración: ' + str(self.calibracion)
    
class Consumible(models.Model):
    nombre      = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    cantidad      = models.IntegerField()
    unidad      = models.CharField(max_length=10, default='c/u')
    
    def __str__(self) -> str:
        return self.nombre + ' -----> ' + str(self.cantidad) + self.unidad 
    
