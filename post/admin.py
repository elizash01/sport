from django.contrib import admin

from .models import Legends, Weekly
# Register your models here.
class LegendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'qwer', 'asd', 'create_at', 'updated_at', )

class WeeklyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pochta', 'create_at', 'updated_at', )


admin.site.register(Legends, LegendsAdmin)  
admin.site.register(Weekly, WeeklyAdmin) 