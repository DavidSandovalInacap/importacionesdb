# aqui se importan las funciones y clases necesarias
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

# aqui estoy definiendo las URL's y asignando las vistas 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_importacion',views.lista_importacion, name='lista_importacion'),
    path('importaciones', views.importaciones, name='importaciones'),
    path('importaciones/crear_importacion', views.crear, name='crear_importacion'),
    path('importaciones/boleta/<int:id>', views.boleta, name='boleta'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # esta es la configuración para servir archivos multimedia durante el desarrollo