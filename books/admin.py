from django.contrib import admin
from . models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author' ,'translator', 'price' , 'cover']



# admin.site.register(Book , BookAdmin)