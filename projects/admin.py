from django.contrib import admin
from .models import Projects, Tag, ProgrammingLang, Developer, Technology

class PostAdmin(admin.ModelAdmin):
    list_filter = ("developed_by", "date", "tags", "languages", "employer")
    list_display = ("title", "developed_by", "employer", "start_date", "end_date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Projects, PostAdmin)
admin.site.register(Developer)
admin.site.register(Tag)
admin.site.register(ProgrammingLang)
admin.site.register(Technology)
