from django.contrib import admin
from .models import *
from .models.doctor import ServiceDocs

# Register your models here.
admin.site.register(User)
admin.site.register(Position)
admin.site.register(Price)
admin.site.register(Professions)
admin.site.register(DocTime)
admin.site.register(Service)
admin.site.register(ServiceDocs)


