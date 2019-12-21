from django.db import models
from faicon.fields import FAIconField
from ckeditor.fields import RichTextField


# ------------------ [BANNER DA SEÇÃO INICIAL] Foto e Texto -------------------------- #

class Banner(models.Model):
    name = models.CharField('Identificador', max_length=100)
    slug = models.SlugField('Atalho')
    text = models.TextField('Mensagem do Banner', blank=False)
    image = models.ImageField(upload_to='banner/images', verbose_name='Foto do Banner', null=False, blank=False)
    prepopulated_fields = {'slug':['name']}
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Banner'
        verbose_name_plural = '#01: Banners'
        ordering = ['name']
        

# ------------------ [SEÇÃO CURSO] Cards de Informações -------------------------- #

class Course(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    icon = models.ImageField(upload_to='course/images', verbose_name='Ícone', null=False, blank=False)
    description = models.TextField('Descrição', max_length=200, blank=False)
    prepopulated_fields = {'slug':['name']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Informação do Curso'
        verbose_name_plural = '#02: Informações do Curso'
        ordering = ['title']
        
        
        
# ------------------ [SEÇÃO CORPO DOCENTE] Infos dos Professores -------------------------- #

class Professor(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    position = models.TextField('Cargo', blank=False)
    image = models.ImageField(upload_to='professor/images', verbose_name='Foto do(a) Professor(a)', null=False, blank=False)
    prepopulated_fields = {'slug':['name']}
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Corpo Docente'
        verbose_name_plural = '#03: Docentes'
        ordering = ['name']

        
# ------------------ [SEÇÃO DISCIPLINAS] Infos das Disciplinas -------------------------- #

class Discipline(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    icon = models.ImageField(upload_to='discipline/images', verbose_name='Ícone', null=False, blank=False)
    description = models.TextField('Descrição', max_length=200, blank=False)
    prepopulated_fields = {'slug':['name']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Informação da Disciplina'
        verbose_name_plural = '#04: Informações da Disciplina'
        ordering = ['title']
        


# ------------------ [SEÇÃO TCC] Template TCC  -------------------------- #

class Template(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    file = models.FileField(upload_to='tcc/files', verbose_name='Arquivo', null=False, blank=False)    
    prepopulated_fields = {'slug':['title']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Template'
        verbose_name_plural = '#05: Templates'
        ordering = ['title']

        
# ------------------ [SEÇÃO TCC] Links para o TCC -------------------------- #

class Link(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    link = models.CharField('Link', max_length=500, null=True)   
    prepopulated_fields = {'slug':['title']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Link'
        verbose_name_plural = '#06: Links'
        ordering = ['title']

        

# ------------------ [SEÇÃO CONTATO] Infos de Contato -------------------------- #

class Contact(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    local = models.CharField('Setor - Bloco - Sala', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    phone = models.CharField('Telefone', max_length=100)
    prepopulated_fields = {'slug':['title']}
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Contato'
        verbose_name_plural = '#07: Contatos'
        ordering = ['title']

        
# ------------------ [PÁGINA DISCIPLINA] Detalhes Disciplina -------------------------- #

class Infos(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    content = RichTextField('Descrição da Disciplina', null=True, blank=True)
    prepopulated_fields = {'slug':['title']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Descrição'
        verbose_name_plural = '#08: Descrição da Disciplina'
        ordering = ['title']

        
        
# ------------------ [PÁGINA DISCIPLINA] Referências da Disciplina -------------------------- #

class Reference(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Atalho')
    file = models.FileField(upload_to='discipline/files', verbose_name='Arquivo', null=False, blank=False)    
    prepopulated_fields = {'slug':['title']}
    
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name = 'Referência'
        verbose_name_plural = '#09: Referências'
        ordering = ['title']
