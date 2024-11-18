from django.contrib import admin

# Register your models here.
from .models import Contact 

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email','phone','message')
  list_display_links = ('name', 'email')
  list_filter = ('contact_date',)
  search_fields = ('name', 'email', 'phone')
  list_editable = ('phone',)
  list_per_page = 25
  ordering = ('-contact_date',)
  date_hierarchy = 'contact_date'

admin.site.register(Contact,ContactAdmin)