
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal_project/', include('django_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
