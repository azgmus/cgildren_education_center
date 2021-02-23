from django.contrib import admin
from .models import Article
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(label="содержание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'





@admin.register(Article)
class InfoPagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    form = ArticleAdminForm

