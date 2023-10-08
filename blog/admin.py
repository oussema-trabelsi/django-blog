from django.contrib import admin
from .models import AboutPage,ContactPage,HomePage,Post
# Register your models here.
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)



@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','created_at','status']
    list_filter=['status','created_at','publish','author']
    raw_id_fileds='author'
    prepopulated_fields={'slug':('title',)}
    ordering=['status','publish']