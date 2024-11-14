from django.contrib import admin

# Register your models here.
from .models import Listing

#To show extra fields for the listing admin
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id','title','is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor','is_published', 'list_date')
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode')
  list_editable = ('is_published', 'price')
  list_per_page = 25
  ordering = ('-list_date',)
  date_hierarchy = 'list_date'
admin.site.register(Listing, ListingAdmin)