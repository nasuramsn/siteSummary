from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('summary_app1/', include('summary_app1.urls')),
    url(r'^admin/', admin.site.urls),
]
