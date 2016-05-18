from django.contrib import admin

from .models import Scroll

class ScrollAdmin(admin.ModelAdmin):
	list_display = ('scrollID', 'scrollMessage')

admin.site.register(Scroll, ScrollAdmin)