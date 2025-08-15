from django.contrib import admin
from . models import Customer


class CustomerAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','phone','email','city','date','image')


admin.site.register(Customer, CustomerAdmin)
