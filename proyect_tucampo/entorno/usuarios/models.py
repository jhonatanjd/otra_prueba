from pyexpat import model
from django.db import models

class client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=254)  
    class Meta:
        db_table ='cliente'

class producer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=254)   
    class Meta:
        db_table ='productor'

class driver(models.Model):
    VEHICLE_TYPE =( 
        ('Pickup', 'Pickup'),
        ('Luv','Luv'),
        ('Turbo', 'Turbo'),
        ('Camion sencillo','Camion'),
        ('Doble troque', 'Doble troque'),
        ('Cuatro manos','Cuatro manos'),
        ('Minimula', 'Minimula'),
        ('Tractomula 2 troques','Tractomula 2 troques'),
        ('Tractomula 3 troques','Tractomula 3 troques'))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    vehicle_type = models.CharField(max_length=254, null=True, choices=VEHICLE_TYPE)
    city = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    password = models.CharField(max_length=254)

    class Meta:
        db_table ='driver'

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

CIUDADS ={
    ('bogota','bogota'),
    ('medellin','medellin'),
    ('cali','cali'),
    ('boyaca','boyaca'),
    ('cucuta','cucuta'),
    ('leticia','leticia'),
    ('rionegro','rionegro'),
    ('apartado','apartado'),
    ('turbo','turbo'),
    ('caucasia','caucasia'),
    ('arauca','arauca'),
    ('barranquilla','barranquilla'),
    ('sabanalarga','sabanalarga'),
    ('girardot','girardot'),
    ('fusagasuga','fusagasuga'),
    ('zipaquira','zipaquira'),
    ('facatativa','facatativa'),
    ('cartagena','cartagena'),
    ('magangue','magangue'),
    ('el carmen de bolivar','el carmen de bolivar'),
    ('tunja','tunja'),
    
}
ROL ={
    ('eres cliente','eres cliente'),
    ('eres productor','eres productor'),
    ('eres conductor','eres conducto')
    
}    

class registro (models.Model):
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    rol = models.CharField(max_length=254, choices=ROL)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=254)
    cedula = models.CharField(max_length=254)
    direcion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    celular = models.CharField(max_length=254)
    correo = models.CharField(max_length=254)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)

    class Meta:
        db_table ='registro'

    def __str__(self):
        return self.username      

class soporte(models.Model):
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)        

    class Meta:
        db_table ='soporte'


ESTADO ={
    ('Disponible','disponible'),
    ('no disponible','no disponible'),
    ('pendiente','pendiente'), 
}  
PRODUCTS_FRUTAS ={
    ('banano','banano'),
    ('fresa','fresa'),
    ('papaya','papaya'),
    ('manzana','manzana'), 
    ('uvas','uvas'),
    ('mandarina','mandarina')
}
CANTIDAS ={
    ('50 kgs','50 kgs'),
    ('60 kgs','60 kgs'),
    ('70 kgs','70 kgs'),
    ('80 kgs','80 kgs'), 
    ('90 kgs','90 kgs'),
    ('100 kgs','100 kgs')
}
SI_NO ={
    ('NO','NO'),
    ('SI','SI'),
}
class registro_producto(models.Model):
    producto = models.CharField(max_length=254, unique=True)
    cantidad = models.CharField(max_length=254)
    precio_kgs = models.CharField(max_length=254, choices=ROL)
    precio_total = models.CharField(max_length=254)
    ciudad = models.CharField(max_length=254)
    cedula = models.CharField(max_length=254)
    direcion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    celular = models.CharField(max_length=254)
    correo = models.CharField(max_length=254)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)

    class Meta:
        db_table ='registro'

    def __str__(self):
        return self.username
