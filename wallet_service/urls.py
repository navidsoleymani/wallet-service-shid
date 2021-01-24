from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('wallet.urls'), name='wallet'),
    url(r'setting/', include('wsetting.urls'), name='setting'),
]
