from django.contrib import admin
from .models import *



# ------------------ [SEÇÃO CURSO] -------------------------- #
class CourseAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'icon', 'description']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Course, CourseAdmin)



# ------------------ [SEÇÃO CORPO DOCENTE] -------------------------- #
class ProfessorAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'position', 'image']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ['name']}

admin.site.register(Professor, ProfessorAdmin)


# ------------------ [SEÇÃO DISCIPLINA] -------------------------- #
class DisciplineAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'icon', 'description']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Discipline, DisciplineAdmin)


# ------------------ [SEÇÃO TCC] -------------------------- #
class TemplateAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'file']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Template, TemplateAdmin)



# ------------------ [SEÇÃO TCC] -------------------------- #
class LinkAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'link']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Link, LinkAdmin)


# ------------------ [PÁGINA DISCIPLINA] -------------------------- #

class InfosAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'content']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Infos, InfosAdmin)


class ReferenceAdmin(admin.ModelAdmin):

	list_display = ['title', 'slug', 'file']
	search_fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Reference, ReferenceAdmin)