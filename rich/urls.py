from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    url(r'', include('htmlToPDF.urls')),
    url(r'^admin/', admin.site.urls),
]
