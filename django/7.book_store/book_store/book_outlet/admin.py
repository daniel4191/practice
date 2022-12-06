from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.
# 이걸 해줌으로 인해서 관리자 페이지에서 관리가 가능하게 되었다.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    # 관리자 페이지에서 add data 할떄, title을 작성하면 slug도 함께 작성되는 기능이다.
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
