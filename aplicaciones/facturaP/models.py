from django.db import models

# Create your models here.

class address(models.Model): 
    street = models.CharField(max_length=50)
    exterior = models.CharField(max_length=50) 
    interior = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50) 
    city = models.CharField(max_length=50) 
    municipality = models.CharField(max_length=50) 
    zip = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    country = models.CharField(max_length=3)

class taxes(models.Model): 
    type=models.CharField(max_length=200)
    rate=models.CharField(max_length=200)
    
class local_taxes(models.Model): 
    type=models.CharField(max_length=200)
    rate=models.CharField(max_length=200)
  
class cliente(models.Model):
   legal_name = models.CharField(max_length=50)
   tax_id = models.CharField(max_length=50)
   tax_system = models.CharField(max_length=3)
   email = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   #address = models.CharField(max_length=2000)
   address = models.ForeignKey(address,null=True,on_delete=models.CASCADE)
   is_create=models.BooleanField(default=False)


 
class producto(models.Model):
    description=models.CharField(max_length=200)
    product_key=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    tax_included=models.BooleanField(default=False)
    taxability=models.BooleanField(default=False)
    taxes=models.ForeignKey(taxes,null=True,on_delete=models.CASCADE)
    local_taxes=models.ForeignKey(local_taxes,null=True,on_delete=models.CASCADE)
    unit_key=models.CharField(max_length=200)
    unit_name=models.CharField(max_length=200)
    sku=models.CharField(max_length=200)

class item(models.Model):
    quantity=models.CharField(max_length=200)
    producto=models.ForeignKey(producto,null=True,on_delete=models.CASCADE)
class factura(models.Model):
    type = models.CharField(max_length=3)
    cliente=models.ForeignKey(cliente,null=True,on_delete=models.CASCADE)
    item=models.ForeignKey(item,null=True,on_delete=models.CASCADE)
    payment_form=models.CharField(max_length=200)
    folio_number=models.CharField(max_length=200)
    series=models.CharField(max_length=200)

   
class empresa(models.Model):
    legal_name=models.CharField(primary_key=True,max_length=20)
    numero=models.PositiveSmallIntegerField()
    fechaCotizacion=models.CharField(max_length=6)
    fechaPedido=models.CharField(max_length=6)
    tipoVenta=models.CharField(max_length=6)
    moneda=models.CharField(max_length=6)
    nombreVendedor=models.CharField(max_length=60)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.legal_name,self.numero, self.fechaCotizacion,self.fechaPedido,self.tipoVenta,self.moneda,self.nombreVendedor)
    
   