from django.urls import path

from modulo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('registro/', views.UserCreation, name='registro'),    
    path('trabajo-list/', views.trabajoList, name='trabajo-list'), 
    path('trabajo-list-granformato/', views.trabajoListGranformato, name='trabajo-list-granformato'), 
    path('trabajo-list-corte/', views.trabajoListCorte, name='trabajo-list-corte'),  
    path('trabajo-list-impresiones/', views.trabajoListImpresiones, name='trabajo-list-impresiones'), 
    path('trabajo-list-publicidad/', views.trabajoListPublicidad, name='trabajo-list-publicidad'), 
    path('trabajo-create/', views.trabajoCreate, name='trabajo-create'),
    path('trabajo-update/<int:id>', views.trabajoUpdate, name='trabajo-update'),
    path('trabajo-detail/<int:id>', views.trabajo_detail, name='trabajo-detail'),
    path('producto-list/', views.ProductoList, name='producto-list'), 
    path('producto-create/', views.productoCreate, name='producto-create'),
    path('pdf-trabajos/', views.ListTrabajosPdf.as_view(), name='pdf-trabajos'),
    path('pdf-trabajosGF/', views.ListTrabajosGFPdf.as_view(), name='pdf-trabajosGF'),
    path('pdf-trabajosCorte/', views.ListTrabajosCortePdf.as_view(), name='pdf-trabajosCorte'),
    path('pdf-trabajosImp/', views.ListTrabajosImpPdf.as_view(), name='pdf-trabajosImp'),
    path('pdf-trabajosP/', views.ListTrabajosPPdf.as_view(), name='pdf-trabajosP'),
    path('producto-update/<int:id>', views.productoUpdate, name='producto-update'),
    path('producto-detail/<int:id>', views.producto_detail, name='producto-detail'),
    path('pdf-productos/', views.ListProductosPdf.as_view(), name='pdf-productos'),
    path('import', views.importar , name='import'),
    path('reporte_excel_trabajos/', views.reporteTrabajoExcel.as_view() , name='reporte_excel_trabajos'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
