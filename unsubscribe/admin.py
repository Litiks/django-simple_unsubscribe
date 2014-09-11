from django.contrib import admin
from unsubscribe.models import *

class UnsubscribeDetailAdmin(admin.ModelAdmin):
    list_display = ('email', 'unsub_date')
    search_fields = ('email',)

admin.site.register(UnsubscribeDetail, UnsubscribeDetailAdmin)
