from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import empresa,cliente,producto,factura,address,taxes,local_taxes,item

# Create your views here.

def index(request):
   return render(request,"index.html")
def index1(request):
   return render(request,"index1.html")
def producto_(request):
   return render(request,"producto.html")
def factura_(request):
   return render(request,"factura.html")
def producto_1(request):
   return render(request,"producto1.html")
def factura_1(request):
   return render(request,"factura1.html")


def list_factura(_request):
    fact=list(factura.objects.values('type','cliente__legal_name','cliente__email','cliente__tax_id','cliente__tax_system','cliente__address__zip','cliente__tax_system','item__quantity','item__producto__description','item__producto__product_key','item__producto__price','payment_form','folio_number','series'))
    for datac in fact:
     dict_fact=dict()
     dict_fact['type']=datac['type']
     dict_customer=dict()
     dict_customer['legal_name']=datac['cliente__legal_name']
     dict_customer['email']=datac['cliente__email']
     dict_customer['tax_id']=datac['cliente__tax_id']
     dict_customer['tax_system']=datac['cliente__tax_system']
     dic_address=dict() 
     dic_address['zip']=datac['cliente__address__zip']
     dict_customer['address']=dic_address
     dict_fact['customer']=dict_customer
     dict_item=dict()
     dict_item['quantity']=datac['item__quantity']
     dict_product=dict()
     dict_product['description']=datac['item__producto__description']
     dict_product['product_key']=datac['item__producto__product_key']
     dict_product['price']=datac['item__producto__price']
     dict_item['product']=dict_product
     item=list()
     item.append(dict_item)
     dict_fact['items']=item
     dict_fact['payment_form']=datac['payment_form'] 
     dict_fact['folio_number']=datac['folio_number']
     dict_fact['series']=datac['series'] 


       
    return JsonResponse(dict_fact)
 

def list_producto(_request):
    pr=list(producto.objects.values('description','product_key','price','tax_included','taxability','taxes__type','taxes__rate','unit_key','unit_name','sku'))
    list_pr=list()
    for datab in pr:
       dict_product=dict()
       dict_product['description']=datab['description']
       dict_product['product_key']=datab['product_key']
       dict_product['price']=datab['price']
       dict_product['tax_included']=datab['tax_included']
       dict_product['taxability']=datab['taxability']
       dict_taxe=dict()
    
       dict_taxe['type']=datab['taxes__type']
       dict_taxe['rate']=datab['taxes__rate']
       tax=list()
       tax.append(dict_taxe)
       dict_product['taxes']=tax
       ltaxes=list()
       dict_product['local_taxes']=ltaxes 
       dict_product['unit_key']=datab['unit_key']
       dict_product['unit_name']=datab['unit_name']
       dict_product['sku']=datab['sku']

     
       list_pr.append(dict_product)
    data = {'productos':dict_product}
   
    return JsonResponse(dict_product)

def list_cliente(_request):
    programmers = list(cliente.objects.values('id','legal_name','tax_id','tax_system','email','phone','address__street','address__exterior','address__interior','address__neighborhood','address__city','address__municipality','address__zip','address__state'))
    
    list_programmers=list()
    
    for datap in programmers:
       idcliente=datap['id']
       dic_programmers=dict()
       dic_programmers['legal_name']=datap['legal_name']
       dic_programmers['tax_id']=datap['tax_id']
       dic_programmers['tax_system']=datap['tax_system']
       dic_programmers['email']=datap['email']
       dic_programmers['phone']=datap['phone']
       dic_address=dict()
       dic_address['street']=datap['address__street']
       dic_address['exterior']=datap['address__exterior']
       dic_address['interior']=datap['address__interior']
       dic_address['neighborhood']=datap['address__neighborhood']
       dic_address['city']=datap['address__city']
       dic_address['municipality']=datap['address__municipality']
       dic_address['zip']=datap['address__zip']
       dic_address['state']=datap['address__state']

       dic_programmers['address']=dic_address
       list_programmers.append(dic_programmers)
    data = {'clientes':dic_programmers}
    #import pdb; pdb.set_trace()
    #cliente.objects.filter(id=idcliente).update(is_create=True)
    # .filter(is_create=False)
    return JsonResponse(dic_programmers)

def hola(request):
    facturaslistado=empresa.objects.all()
    return render(request,"gestionFactura.html",{"facturas":facturaslistado})

def listarCliente(request):
     clientelist=cliente.objects.all()
     return render(request,"listarClientes.html",{"Clientes":clientelist})
def listarProductos(request):
     produclist=producto.objects.all()
     return render(request,"listarProductos.html",{"productos": produclist})
def listarFacturas(request):
     faclist=factura.objects.all()
     return render(request,"listarFacturas.html",{"facturas": faclist})



def muestraProducto(request):
    facturaslist=empresa.objects.all()
    return render(request,"gestionProduto.html",{"Productos":facturaslist})

def crearcliente(request):
  return render(request,"creacionCliente.html")
 
def registrarFacture(request):
  legal_name = request.POST['txtid']
  numero = request.POST['num']
  fechaCotizacion = request.POST['txtfechacotizacion']
  fechaPedido = request.POST['txtfechapedido']
  tipoVenta = request.POST['tipoventa']
  moneda = request.POST['moneda']
  nombreVendedor = request.POST['nombreVendedor']

  factura = empresa.objects.create(
     legal_name =legal_name, numero=numero, fechaCotizacion=fechaCotizacion,fechaPedido=fechaPedido,tipoVenta=tipoVenta,moneda=moneda,nombreVendedor=nombreVendedor)
  return redirect('/')

def registrarProducto(request):
  legal_name = request.POST['txtid']
  numero = request.POST['num']
  fechaCotizacion = request.POST['txtfechacotizacion']
  fechaPedido = request.POST['txtfechapedido']
  tipoVenta = request.POST['tipoventa']
  moneda = request.POST['moneda']
  nombreVendedor = request.POST['nombreVendedor']

  factura = empresa.objects.create(
        legal_name=legal_name, numero=numero, fechaCotizacion=fechaCotizacion,fechaPedido=fechaPedido,tipoVenta=tipoVenta,moneda=moneda,nombreVendedor=nombreVendedor)
  return redirect('/producto/')


def edicionfactura(request, legal_name):
    factura = empresa.objects.get(legal_name=legal_name)
    return render(request, "edicionfactura.html", {"empresa": factura})

def editarFactura(request):
    legal_name = request.POST['txtid']
    numero = request.POST['num']
    fechaCotizacion = request.POST['txtfechacotizacion']
    fechaPedido = request.POST['txtfechapedido']
    tipoVenta = request.POST['tipoventa']
    moneda = request.POST['moneda']
    nombreVendedor = request.POST['nombreVendedor']
    factura = empresa.objects.get(legal_name=legal_name)
    factura.legal_name=legal_name
    factura.numero=numero
    factura.fechaCotizacion=fechaCotizacion
    factura.fechaPedido=fechaPedido
    factura.tipoVenta=tipoVenta
    factura.moneda=moneda
    factura.nombreVendedor=nombreVendedor
    factura.save()
    return redirect('/')

def eliminarfactura(request,moneda):
    fact=empresa.objects.get(moneda=moneda)
    fact.delete()
    return redirect('/')


