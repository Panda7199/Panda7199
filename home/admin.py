from django.contrib import admin
from home.models import Aboutus, Chef, ContactMessage, Order


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title','email', 'phone',]

class ChefAdmin(admin.ModelAdmin):
    list_display = ['title',]



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'creat_at',)
    list_filter = ['status']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'amount', 'category', 'food', 'address','ip',]
    list_filter = ['status']









admin.site.register(Order, OrderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Aboutus, AboutusAdmin)

