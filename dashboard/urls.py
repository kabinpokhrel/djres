from django.conf.urls import url
from .views import dashboard_index, dashboard_client
from .views import GeneratePDF, pdf_test

urlpatterns = [
    url(r'^$', dashboard_index, name='dashboard-index'),
    url(r'^client/(?P<slug>[\w-]+)/$', dashboard_client, name='dashboard-client'),
    url(r'^pdf/$', GeneratePDF.as_view(), name='generate-pdf'),
    url(r'^pdf-test/$', pdf_test, name='pdf-test')
]
