from django.contrib import admin
from demo import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')

class AutherAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'name', 'email', 'headshot', 'last_accessed')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'phone', 'weixin'
    )
    search_fields = (
        'user', 'phone', 'weixin'
    )
    list_filter = (
        'user', 'phone', 'weixin'
    )

class ListAdmin(admin.ModelAdmin):
    list_display = (
        'list_name', 'ip', 'os', 'cpu', 'mem', 'total_hard_disk',
        'guest_status', 'app_name', 'app_role', 'vc',
    )
    list_filter = ('os', 'tools_status', 'guest_status', 'vc', 'esxi_host')

    search_fields = (
        'hostname', 'ip', 'os', 'os_version', 'cpu', 'mem', 'total_hard_disk',
        'tools_status', 'guest_status', 'vc', 'list_name', 'instance_uuid',
        'app_name'
    )

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'serves_hot_dogs', 'serves_pizza')

admin.site.register(models.Author, AutherAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Place, PlaceAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.List, ListAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
