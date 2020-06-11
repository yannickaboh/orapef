from django.db import models
from django.contrib.auth.models import Group, User 
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import *
from django.utils import timezone

# Create your models here.

class Profile(models.Model):

	ONLINE = 'En ligne'
	OFFLINE = 'Hors ligne'

	CONNECTED = [
        (ONLINE, 'En ligne'),
        (OFFLINE, 'Hors ligne'),
    ]


	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/avatar.jpg', verbose_name='Avatar')
	address = models.CharField(max_length=250, blank=True, verbose_name='Adresse')
	phone = models.CharField(max_length=250, blank=True, verbose_name='Téléphone')
	description = models.TextField(blank=True, verbose_name='Description')
	nationalite = models.CharField(max_length=250, blank=True, verbose_name='Nationalité')
	district = models.CharField(max_length=250, blank=True, verbose_name='Quartier')
	ville = models.CharField(max_length=250, blank=True, verbose_name='Ville')
	pays = models.CharField(max_length=250, blank=True, verbose_name='Pays')
	activite = models.CharField(max_length=250, blank=True, verbose_name='Activité')
	code = models.CharField(max_length=250, verbose_name='code de Réinitialisation', blank=True)
	statusAbonnement  = models.IntegerField(verbose_name='statut Abonnement', blank=True, default=0)
	connected = models.CharField(max_length=250, choices=CONNECTED, default=OFFLINE, verbose_name='En ligne ?')


	longitude = models.CharField(max_length=100, blank=True, default=0.0)
	latitude = models.CharField(max_length=100, blank=True, default=0.0)


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Profile'
		ordering = ('user',)
		verbose_name = 'profile'
		verbose_name_plural = 'profiles'

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TypeFormation(models.Model):
	image = models.ImageField(upload_to='types_formation', blank=True, verbose_name='Image')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'TypeFormation'
		ordering = ('-created',)
		verbose_name = 'Type de Formation'
		verbose_name_plural = 'Types de Formation'

	def __str__(self):
		return self.libelle


class TypeMetier(models.Model):
	image = models.ImageField(upload_to='types_metier', blank=True, verbose_name='Image')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'TypeMetier'
		ordering = ('-created',)
		verbose_name = 'Type de Métier'
		verbose_name_plural = 'Types de Métier'

	def __str__(self):
		return self.libelle


class TypeDiplome(models.Model):
	image = models.ImageField(upload_to='types_diplome', blank=True, verbose_name='Image')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'TypeDiplome'
		ordering = ('-created',)
		verbose_name = 'Type de Diplôme'
		verbose_name_plural = 'Types de Diplôme'

	def __str__(self):
		return self.libelle


class TypeEcole(models.Model):
	image = models.ImageField(upload_to='types_ecole', blank=True, verbose_name='Image')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'TypeEcole'
		ordering = ('-created',)
		verbose_name = 'Type d\'Ecole'
		verbose_name_plural = 'Types d\'Ecole'

	def __str__(self):
		return self.libelle


class TypeEvenement(models.Model):
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'TypeEvenement'
		ordering = ('-created',)
		verbose_name = 'Type d\'Evenement'
		verbose_name_plural = 'Types d\'Evenement'

	def __str__(self):
		return self.libelle


class Ecole(models.Model):
	type_ecole = models.ForeignKey(TypeEcole, on_delete=models.CASCADE, verbose_name="Type Ecole")
	logo = models.ImageField(upload_to='ecoles', blank=True, verbose_name='Image')
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	abbreviation = models.CharField(max_length=250, blank=True, verbose_name='Abbréviation')
	date_creation = models.CharField(max_length=250, blank=True, verbose_name='Date de Création')
	responsable_actuel = models.CharField(max_length=250, blank=True, verbose_name='Responsable Actuel')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	fax = models.CharField(max_length=250, blank=True, verbose_name='FAX')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	website = models.CharField(max_length=250, blank=True, verbose_name='Site Web')
	description = models.TextField(blank=True, verbose_name='Description')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Ecole'
		ordering = ('-created',)
		verbose_name = 'Ecole'
		verbose_name_plural = 'Ecoles'

	def __str__(self):
		return self.titre


class Entreprise(models.Model):
	logo = models.ImageField(upload_to='ecoles', blank=True, verbose_name='Image')
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	abbreviation = models.CharField(max_length=250, blank=True, verbose_name='Abbréviation')
	date_creation = models.CharField(max_length=250, blank=True, verbose_name='Date de Création')
	responsable_actuel = models.CharField(max_length=250, blank=True, verbose_name='Responsable Actuel')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	fax = models.CharField(max_length=250, blank=True, verbose_name='FAX')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	website = models.CharField(max_length=250, blank=True, verbose_name='Site Web')
	description = models.TextField(blank=True, verbose_name='Description')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Entreprise'
		ordering = ('-created',)
		verbose_name = 'Entreprise'
		verbose_name_plural = 'Entreprises'

	def __str__(self):
		return self.titre


class Incubateur(models.Model):
	logo = models.ImageField(upload_to='ecoles', blank=True, verbose_name='Image')
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	abbreviation = models.CharField(max_length=250, blank=True, verbose_name='Abbréviation')
	date_creation = models.CharField(max_length=250, blank=True, verbose_name='Date de Création')
	responsable_actuel = models.CharField(max_length=250, blank=True, verbose_name='Responsable Actuel')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	fax = models.CharField(max_length=250, blank=True, verbose_name='FAX')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	website = models.CharField(max_length=250, blank=True, verbose_name='Site Web')
	description = models.TextField(blank=True, verbose_name='Description')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Incubateur'
		ordering = ('-created',)
		verbose_name = 'Incubateur'
		verbose_name_plural = 'Incubateurs'

	def __str__(self):
		return self.titre


class Stage(models.Model):
	entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, verbose_name="Entreprise")
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	description = models.TextField(blank=True, verbose_name='Description')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Stage'
		ordering = ('-created',)
		verbose_name = 'Stage'
		verbose_name_plural = 'Stages'

	def __str__(self):
		return self.titre


class Emploi(models.Model):
	entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, verbose_name="Entreprise")
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	description = models.TextField(blank=True, verbose_name='Description')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Emploi'
		ordering = ('-created',)
		verbose_name = 'Emploi'
		verbose_name_plural = 'Emplois'

	def __str__(self):
		return self.titre


class Metier(models.Model):
	type_metier = models.ForeignKey(TypeMetier, on_delete=models.CASCADE, verbose_name="Type de Métier")
	image = models.ImageField(upload_to='metiers', blank=True, verbose_name='Image')
	niveau = models.CharField(max_length=250, blank=True, verbose_name='Niveau')
	prerequis = models.CharField(max_length=250, blank=True, verbose_name='Pré-requis')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')
	description = models.TextField(blank=True, verbose_name='Description')
	debouches = models.TextField(blank=True, verbose_name='Débouchés')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Metier'
		ordering = ('-created',)
		verbose_name = 'Metier'
		verbose_name_plural = 'Metiers'

	def __str__(self):
		return self.libelle


class Diplome(models.Model):
	type_diplome = models.ForeignKey(TypeDiplome, on_delete=models.CASCADE, verbose_name="Type de Diplôme")
	image = models.ImageField(upload_to='diplomes', blank=True, verbose_name='Image')
	niveau = models.CharField(max_length=250, blank=True, verbose_name='Niveau')
	prerequis = models.CharField(max_length=250, blank=True, verbose_name='Pré-requis')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')
	description = models.TextField(blank=True, verbose_name='Description')
	debouches = models.TextField(blank=True, verbose_name='Débouchés')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Diplome'
		ordering = ('-created',)
		verbose_name = 'Diplôme'
		verbose_name_plural = 'Diplômes'

	def __str__(self):
		return self.libelle


class Formation(models.Model):
	type_formation = models.ForeignKey(TypeFormation, on_delete=models.CASCADE, verbose_name="Type de Formation")
	image = models.ImageField(upload_to='formations', blank=True, verbose_name='Image')
	niveau = models.CharField(max_length=250, blank=True, verbose_name='Niveau')
	prerequis = models.CharField(max_length=250, blank=True, verbose_name='Pré-requis')
	libelle = models.CharField(max_length=250, blank=True, verbose_name='Libellé')
	description = models.TextField(blank=True, verbose_name='Description')
	debouches = models.TextField(blank=True, verbose_name='Débouchés')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Formation'
		ordering = ('-created',)
		verbose_name = 'Formation'
		verbose_name_plural = 'Formations'

	def __str__(self):
		return self.libelle


class Evenement(models.Model):
	type_event = models.ForeignKey(TypeEvenement, on_delete=models.CASCADE, verbose_name="Type d\'Evenement")
	image = models.ImageField(upload_to='metiers', blank=True, verbose_name='Image')
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	description = models.TextField(blank=True, verbose_name='Description')
	nbre_places = models.IntegerField(blank=True, verbose_name='Nombre de Places')
	prix_simple = models.IntegerField(blank=True, verbose_name='Prix Simple')
	prix_vip = models.IntegerField(blank=True, verbose_name='Prix VIP')
	lieu = models.CharField(max_length=250, blank=True, verbose_name='Lieu')
	horaire = models.CharField(max_length=250, blank=True, verbose_name='Timing')
	phone1 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 1')
	phone2 = models.CharField(max_length=250, blank=True, verbose_name='Téléphone 2')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	website = models.CharField(max_length=250, blank=True, verbose_name='Site Web')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Evenement'
		ordering = ('-created',)
		verbose_name = 'Evenement'
		verbose_name_plural = 'Evenements'

	def __str__(self):
		return self.titre


class Departement(models.Model):
	ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE, verbose_name="Ecole ou Université")
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	description = models.TextField(blank=True, verbose_name='Description')
	responsable_actuel = models.CharField(max_length=250, blank=True, verbose_name='Responsable Actuel')
	phone = models.CharField(max_length=250, blank=True, verbose_name='Téléphone')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Departement'
		ordering = ('-created',)
		verbose_name = 'Departement'
		verbose_name_plural = 'Departements'

	def __str__(self):
		return self.titre


class Filiere(models.Model):
	departement = models.ForeignKey(Departement, blank=True, on_delete=models.CASCADE, verbose_name="Département")
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	description = models.TextField(blank=True, verbose_name='Description')
	prerequis = models.CharField(max_length=250, blank=True, verbose_name='Pré-requis')
	debouches = models.CharField(max_length=250, blank=True, verbose_name='Débouchés')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Filiere'
		ordering = ('-created',)
		verbose_name = 'Filiere'
		verbose_name_plural = 'Filieres'

	def __str__(self):
		return self.titre


class Matiere(models.Model):
	filiere = models.ForeignKey(Filiere, blank=True, on_delete=models.CASCADE, verbose_name="Filière")
	titre = models.CharField(max_length=250, blank=True, verbose_name='Titre')
	niveau = models.CharField(max_length=250, blank=True, verbose_name='Niveau')
	description = models.TextField(blank=True, verbose_name='Description')
	prerequis = models.CharField(max_length=250, blank=True, verbose_name='Pré-requis')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Matiere'
		ordering = ('-created',)
		verbose_name = 'Matiere'
		verbose_name_plural = 'Matieres'

	def __str__(self):
		return self.titre


class Conseiller(models.Model):
	name = models.CharField(max_length=250, blank=True, verbose_name='Noms & Prénoms')
	fonction = models.CharField(max_length=250, blank=True, verbose_name='Fonction')
	facebook = models.CharField(max_length=250, blank=True, verbose_name='Facebook')
	twitter = models.CharField(max_length=250, blank=True, verbose_name='Twitter')
	instagram = models.CharField(max_length=250, blank=True, verbose_name='Instagram')
	linkedin = models.CharField(max_length=250, blank=True, verbose_name='LinkedIn')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Conseiller'
		ordering = ('-created',)
		verbose_name = 'Conseiller'
		verbose_name_plural = 'Conseillers'

	def __str__(self):
		return self.name


class Message(models.Model):
	name = models.CharField(max_length=250, blank=True, verbose_name='Noms & Prénoms')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	phone = models.CharField(max_length=250, blank=True, verbose_name='Téléphone')
	objet = models.CharField(max_length=250, blank=True, verbose_name='Objet')
	message = models.TextField(max_length=250, blank=True, verbose_name='Message')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'Message'
		ordering = ('-created',)
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'

	def __str__(self):
		return self.name


class RendezVous(models.Model):
	name = models.CharField(max_length=250, blank=True, verbose_name='Noms & Prénoms')
	email = models.EmailField(max_length=250, blank=True, verbose_name='Email')
	phone = models.CharField(max_length=250, blank=True, verbose_name='Téléphone')
	message = models.TextField(max_length=250, blank=True, verbose_name='Message')


	visibilite = models.IntegerField(verbose_name='Visibilité', default=1)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
	updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
	deleted = models.DateTimeField(auto_now=True, verbose_name='Date de Suppression')
	added_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_added_by')
	updated_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_updated_by')
	deleted_by = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE, related_name='%(class)s_deleted_by')

	class Meta:
		db_table = 'RendezVous'
		ordering = ('-created',)
		verbose_name = 'RendezVous'
		verbose_name_plural = 'Nos RendezVous'

	def __str__(self):
		return self.name