from rest_framework import routers
from .views import *
from django.urls import path


router = routers.SimpleRouter()
router.register(r'userdata/(?P<user_name>[\w ]+)/(?P<pass>[\w ]+)', UserViewSet)
router.register(r'registerdata', UserViewSet)
router.register(r'encodedata', EncodeViewSet)
router.register(r'scandata', ScanViewSet)
urlpatterns = router.urls

urlpatterns += [
        path('studentauth/', studentLogin),
]
