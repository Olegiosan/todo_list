from django.contrib import admin
from .models import *

# Register your models here
admin.site.register(Board)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Coments)
admin.site.register(ComentImage)