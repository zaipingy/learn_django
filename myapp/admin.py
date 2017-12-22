from django.contrib import admin

# Register your models here.
from myapp.models import Event, Guest


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']    # 在admin管理后台展示更多字段
    search_fields = ['name']                                            # 在admin后台增加搜索栏
    list_filter = ['status']                                            # 在admin后台增加过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)