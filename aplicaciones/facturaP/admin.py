from django.contrib import admin

from .models import empresa,cliente,address,taxes,producto,local_taxes,item,factura
# Register your models here.
admin.site.register(empresa)
admin.site.register(cliente)
admin.site.register(address)
admin.site.register(producto)
admin.site.register(taxes)
admin.site.register(local_taxes)
admin.site.register(factura)
admin.site.register(item)




