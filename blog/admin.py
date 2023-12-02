from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','editorial','ISBN','edicion')
    list_filter = ('titulo','autor','edicion')
    search_fields = ('titulo','autor','ISBN')
    ordering = ('titulo','ISBN')
      

                    