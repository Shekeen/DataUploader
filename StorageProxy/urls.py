from django.conf.urls import url

from .views import list_all_data, upload_data, api_list_data, api_upload_data


urlpatterns = [
    url(r'^$', list_all_data),
    url(r'^upload/$', upload_data),

    url(r'^api/list', api_list_data),
    url(r'^api/upload', api_upload_data, name='api-upload'),
]
