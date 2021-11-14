from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self,username, email, password=None):
		if not email:
			raise ValueError("Veuillez saisir une adresse email")

		if not username:
			raise ValueError("Veuillez saisir un Pseudo")

		user = self.model(
			email = self.normalize_email(email),
			username = username

			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		user = self.create_user(
			email = self.normalize_email(email),
			username = username,
			password=password
			)

		user.is_active = True
		user.is_admin  = True
		user.is_staff  = True
		user.is_superadmin = True

		user.save(using=self._db)
		return user



class Account(AbstractBaseUser):
	lastname = models.CharField(max_length=50, blank=True, verbose_name='Nom')
	firstname = models.CharField(max_length=50, blank=True, verbose_name='Prénom')
	username  = models.CharField(max_length=50, unique=True, verbose_name='Pseudo')
	email     = models.EmailField(max_length=255, unique=True, verbose_name='Email')
	phone     = models.CharField(max_length=25, blank=True, verbose_name="Téléphone")
	city      = models.CharField(max_length=50, verbose_name="Ville")

	date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date inscription")
	last_login  = models.DateTimeField(auto_now=True, verbose_name="Dernière connexion")
	is_admin    = models.BooleanField(default=False, verbose_name="Admin")
	is_staff     = models.BooleanField(default=False, verbose_name="Staff")
	is_active    = models.BooleanField(default=False, verbose_name="Actif")
	is_superadmin = models.BooleanField(default=False, verbose_name="Super Admin")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	class Meta:
		verbose_name = 'Compte'
		verbose_name_plural = 'Comptes'

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, add_label):
		return True