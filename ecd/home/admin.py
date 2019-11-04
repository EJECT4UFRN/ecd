from django.contrib import admin
from .models import *


# ------------------ [BANNER DA SEÇÃO INICIAL] -------------------------- #
class BannerAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'text', 'image']
	search_fields = ['name', 'slug']

admin.site.register(Banner, BannerAdmin)


# ------------------ [SEÇÃO CURSO] -------------------------- #
class CourseAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'icon', 'description']
	search_fields = ['title', 'slug']

admin.site.register(Course, CourseAdmin)



# ------------------ [SEÇÃO CORPO DOCENTE] -------------------------- #
class ProfessorAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'position', 'image']
	search_fields = ['name', 'slug']

admin.site.register(Professor, ProfessorAdmin)


# ------------------ [SEÇÃO DISCIPLINA] -------------------------- #
class DisciplineAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'icon', 'description']
	search_fields = ['title', 'slug']

admin.site.register(Discipline, DisciplineAdmin)


# ------------------ [SEÇÃO TCC] -------------------------- #
class TemplateAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'file']
	search_fields = ['title', 'slug']

admin.site.register(Template, TemplateAdmin)



# ------------------ [SEÇÃO TCC] -------------------------- #
class LinkAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'link']
	search_fields = ['title', 'slug']

admin.site.register(Link, LinkAdmin)


# ------------------ [SEÇÃO CONTATO] -------------------------- #
class ContactAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'local', 'email', 'phone']
	search_fields = ['title', 'slug']

admin.site.register(Contact, ContactAdmin)



# ------------------ [PÁGINA DISCIPLINA] -------------------------- #

class InfosAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'content']
	search_fields = ['title', 'slug']

admin.site.register(Infos, InfosAdmin)


class ReferenceAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'file']
	search_fields = ['title', 'slug']

admin.site.register(Reference, ReferenceAdmin)