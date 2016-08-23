from django.contrib import admin
from demo import models
# Register your models here.

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

admin.site.register(models.List, ListAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
