from django.contrib import admin
from .models import Note


admin.site.register(Note)
# @admin.register(Notes)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'subject', 'explanation', 'rate_understanding']
    
#     fieldsets = (
#         ('selections', {'fields' : ['subject', 'explanation', 'rate_understanding']}),

#     )


    

