from django import forms
from django.contrib import admin


from .models import KidsGroup, GeneralInfo, InfoPages

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class InfoPagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoPages
        fields = '__all__'


admin.site.register(KidsGroup)
admin.site.register(GeneralInfo)


@admin.register(InfoPages)
class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = InfoPagesAdminForm

