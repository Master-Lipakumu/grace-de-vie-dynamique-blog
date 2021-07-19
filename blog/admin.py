from django.contrib import admin
from .models import Auteur, Pub, Contacte, Demande, Videos, Ncontacte
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Videos, MyModelAdmin)

admin.site.register(Auteur)
admin.site.register(Pub)
admin.site.register(Ncontacte)
admin.site.register(Contacte)
admin.site.register(Demande)