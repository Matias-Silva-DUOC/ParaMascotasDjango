from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#modelos 4ta ev
#modelo para cliente (<> a usuario, puede haber un usuario no cliente pero no al revés)
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	#image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

##  CLASE REGIONES

class Region(models.Model):
    id_region   = models.IntegerField(primary_key=True, verbose_name='ID Región')
    nom_region  = models.CharField(max_length=40, verbose_name='Nombre Región')

    def __str__(self):
        return self.nom_region


##  CLASE PRODUCTOS
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombre      = models.CharField(max_length=32, verbose_name='Nombre Producto')
    precio      = models.IntegerField()
    region      = models.ForeignKey(Region, on_delete=models.CASCADE)
	# stock		= models.IntegerField(default=1, verbose_name='Stock Producto')

    def __str__(self):
        return self.nombre

## CLASE USUARIOS
class Usuario(models.Model):

    class roles(models.TextChoices):
        admin   = 'adm', ('Admin')
        usuario = 'usr', ('Usuario')
        socio   = 'usc', ('Socio')
    email_usuario   = models.EmailField(primary_key=True, max_length=32, verbose_name='Email de Usuario')
    nom_usuario     = models.CharField(max_length=24, verbose_name='Nombre de Usuario')
    ape_usuario     = models.CharField(max_length=24, verbose_name='Apellido de Usuario')
    contra_usuario  = models.CharField(max_length=16, verbose_name='Contraseña de Usuario')
    rol_usuario     = models.CharField(max_length=3, choices=roles.choices, verbose_name='Rol de Usuario')
    ## puntos_usuario  = models.IntegerField(verbose_name='Puntos de Usuario')
    ## mascotas        = models.JSONField()
    ## suscripcion     = models.


    def __str__(self):
        return self.email_usuario


##  CLASE HISTORIAL VENTAS