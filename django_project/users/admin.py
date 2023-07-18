from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = ('id', 'username', 'first_name', 'last_name',)
    ordering = ('username', )
    list_filter = ('date_joined', 'id',)
    readonly_fields = ('username', )
    search_fields = ('username', 'first_name', 'last_name',)
    list_per_page = 10
    list_display_links = ('id', 'username')
