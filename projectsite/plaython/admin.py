from django.contrib import admin
from .models import Applicant
from django.contrib import messages
from .serverUser import *
#from django.utils.safestring import mark_safe

class ApplicantAdmin(admin.ModelAdmin):

    list_per_page = 10
    list_display = ('name', 'student_number', 'username', 'permission', 'apply_time')
    list_editable = ('permission',)
    list_filter = ('permission',)

    actions = ['setPermission', 'deleteUser']

    def setPermission(self, request, queryset):
        for applicant in queryset:
            adduser(applicant.username, applicant.password)
            Applicant.objects.filter(username=applicant.username).update(permission=2)

        messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))

    setPermission.short_description = "선택된 계정 생성하기"
    


    def deleteUser(self, request, queryset):
        for applicant in queryset:
            deluser(applicant.username)
            Applicant.objects.filter(username=applicant.username).delete()

        messages.success(request, '{0}명의 회원을 삭제했습니다.'.format(len(queryset)))

    deleteUser.short_description = "선택된 계정 삭제하기"
    
    def save_model(self, request, obj, form, change):
        if(obj.permission == 2):
            adduser(obj.username, obj.password)
        obj.save()

    def delete_model(self, request, obj):
        deluser(obj.username)
        obj.delete()

admin.site.disable_action('delete_selected')
admin.site.register(Applicant, ApplicantAdmin)
