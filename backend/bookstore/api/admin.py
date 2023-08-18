from django.contrib import admin
from api.models import BookStoreModel
# Register your models here.
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author','edition','publication_date','last_published')
admin.site.register(BookStoreModel,BookStoreModelAdmin)