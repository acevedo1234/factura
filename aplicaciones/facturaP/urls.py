from . import views
from django.urls import path


urlpatterns = [
    path('', views.index,name='index'),
    path('list_cliente/', views.list_cliente, name='list_cliente'),
    path('list_producto/', views.list_producto, name='list_producto'),
    path('list_factura/', views.list_factura, name='list_factura'),
    
    path('producto/', views.muestraProducto),
     path('indexproducto/', views.producto_,name='producto'),
      path('indexfactura/indexproducto/indexfactura/', views.producto_,name='producto'),
     path('indexfactura/', views.factura_,name='factura'),
     path('indexproducto/indexproducto/indexproducto/indexfactura/', views.factura_,name='factura'),
    path('registrarFactura/', views.registrarFacture),
    path('listarSat/', views.index1,name='index1'),
     path('indexproducto/listarSat1/', views.producto_1,name='producto_1'),
     path('indexfactura/indexfactura/indexfactura/listarSat2/', views.factura_1,name='factura_1'),
     path('crearCliente/', views.crearcliente,name='crearcliente'),
     path('listarclientes/', views.listarCliente,name='listarclientes'),
      path('indexproducto/listarProductos/', views.listarProductos,name='listarProductor'),
      path('listarfacturas/', views.listarFacturas,name='listarFacturas'),
     path('registrarProducto/', views.registrarProducto),
      path('edicionfactura/<id>', views.edicionfactura),
      path('editarFactura/', views.editarFactura),
      path('eliminarfactura/<moneda>', views.eliminarfactura),
   
]
