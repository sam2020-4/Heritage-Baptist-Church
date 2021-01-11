from django.contrib import admin
from .models import Team, Sermon, Children, Youth, Event

# Register your models here.
admin.site.register(Team)
admin.site.register(Sermon)
admin.site.register(Children)
admin.site.register(Youth)
admin.site.register(Event)
