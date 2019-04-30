from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AppUsers)
admin.site.register(EncodedData)
admin.site.register(ScanData)