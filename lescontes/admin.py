from django.contrib import admin
from lescontes.models import Ibook

class IbookAdmin(admin.ModelAdmin):
	list_display = ('titre', 'langue')

admin.site.register(Ibook, IbookAdmin)
