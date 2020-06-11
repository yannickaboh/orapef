from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings

# Models Shop app
from website.models import *
from .models import Profile

# Register your models here.




class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class TypeFormationAdmin(admin.ModelAdmin):
    list_display = ['image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(TypeFormation, TypeFormationAdmin)

class TypeMetierAdmin(admin.ModelAdmin):
    list_display = ['image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(TypeMetier, TypeMetierAdmin)

class TypeDiplomeAdmin(admin.ModelAdmin):
    list_display = ['image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(TypeDiplome, TypeDiplomeAdmin)

class TypeEcoleAdmin(admin.ModelAdmin):
    list_display = ['image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(TypeEcole, TypeEcoleAdmin)

class TypeEvenementAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'created', ]
    list_per_page = 10

admin.site.register(TypeEvenement, TypeEvenementAdmin)

class EcoleAdmin(admin.ModelAdmin):
    list_display = ['logo', 'titre', 'created', ]
    list_per_page = 10

admin.site.register(Ecole, EcoleAdmin)

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ['logo', 'titre', 'created', ]
    list_per_page = 10

admin.site.register(Entreprise, EntrepriseAdmin)

class IncubateurAdmin(admin.ModelAdmin):
    list_display = ['logo', 'titre', 'created', ]
    list_per_page = 10

admin.site.register(Incubateur, IncubateurAdmin)

class StageAdmin(admin.ModelAdmin):
    list_display = ['entreprise', 'titre', 'created', ]
    list_per_page = 10

admin.site.register(Stage, StageAdmin)

class EmploiAdmin(admin.ModelAdmin):
    list_display = ['entreprise', 'titre', 'created', ]
    list_per_page = 10

admin.site.register(Emploi, EmploiAdmin)

class MetierAdmin(admin.ModelAdmin):
    list_display = ['type_metier', 'image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(Metier, MetierAdmin)

class DiplomeAdmin(admin.ModelAdmin):
    list_display = ['type_diplome', 'image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(Diplome, DiplomeAdmin)

class FormationAdmin(admin.ModelAdmin):
    list_display = ['type_formation', 'image', 'libelle', 'created', ]
    list_per_page = 10

admin.site.register(Formation, FormationAdmin)

class EvenementAdmin(admin.ModelAdmin):
    list_display = ['type_event', 'image', 'titre', 'lieu', 'created', ]
    list_per_page = 10

admin.site.register(Evenement, EvenementAdmin)

class DepartementAdmin(admin.ModelAdmin):
    list_display = ['ecole', 'titre', 'responsable_actuel', 'phone', 'created', ]
    list_per_page = 10

admin.site.register(Departement, DepartementAdmin)

class FiliereAdmin(admin.ModelAdmin):
    list_display = ['departement', 'titre', 'prerequis',  'created', ]
    list_per_page = 10

admin.site.register(Filiere, FiliereAdmin)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ['filiere', 'titre', 'niveau',  'created', ]
    list_per_page = 10

admin.site.register(Matiere, MatiereAdmin)

class ConseillerAdmin(admin.ModelAdmin):
    list_display = ['name', 'fonction',  'created', ]
    list_per_page = 10

admin.site.register(Conseiller, ConseillerAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'objet',  'created', ]
    list_per_page = 10

admin.site.register(Message, MessageAdmin)

class RendezVousAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created', ]
    list_per_page = 10

admin.site.register(RendezVous, RendezVousAdmin)