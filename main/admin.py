from django.contrib import admin
from .models import Banner,Project,Role,Employee,EmployeeAttribute

# Register your models here.
admin.site.register(Role)



class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_display=('title','image_tag','starttime','active')
admin.site.register(Project,ProjectAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','title','project','role','is_featured')
    list_editable=('is_featured',)
admin.site.register(Employee,EmployeeAdmin)

# Product Attribute
class EmployeeAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','employee')
    list_editable=('employee',)
admin.site.register(EmployeeAttribute,EmployeeAttributeAdmin)