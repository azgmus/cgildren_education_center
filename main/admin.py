from django import forms
from django.contrib import admin


from .models import KidsGroup, GeneralInfo, InfoPages

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class InfoPagesAdminForm(forms.ModelForm):
    schedule = forms.CharField(label="содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoPages
        fields = '__all__'

class InfoPagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="текст страницы", widget=CKEditorUploadingWidget())

    class Meta:
        model = InfoPages
        fields = '__all__'


class KidsGroupForm(forms.ModelForm):
    schedule = forms.CharField(label="расписание", widget=CKEditorUploadingWidget())

    class Meta:
        model = KidsGroup
        fields = '__all__'


@admin.register(KidsGroup)
class KidsGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = KidsGroupForm


admin.site.register(GeneralInfo)
@admin.register(InfoPages)
class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    form = InfoPagesAdminForm

