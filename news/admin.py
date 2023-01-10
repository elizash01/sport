from django.contrib import admin

# Register your models here.

from .models import News, Comments

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'forecast', 'create_at', 'updated_at', )

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'username', 'create_at', 'updated_at', )
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)    