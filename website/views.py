from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.models import Group, User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.forms import ModelForm
import re
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import urllib
from decimal import Decimal
from django.template import loader
from django import template
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
import urllib.request
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required

from datetime import datetime, date
import datetime
from datetime import timedelta
from datetime import datetime
from datetime import *

from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.views.defaults import page_not_found

# Create your views here.

######################################################################################
#																					 #
#                               MANAGE ORAPEF SITE                                   #
#																					 #
######################################################################################


# Acceuil
def index(request):
	return render(request, 'website/index.html', {})

# Contact
def contact(request):
	return render(request, 'website/contact.html', {})

# Services
def services(request):
	return render(request, 'website/services.html', {})

# Comment ça marche ?
def commentcamarche(request):
	return render(request, 'website/commentcamarche.html', {})



######################################################################################
#																					 #
#                               MANAGE ORAPEF SITE                                   #
#																					 #
######################################################################################


# Nos formations
def formations(request):
	return render(request, 'website/formations.html', {})

# Nos metiers
def metiers(request):
	return render(request, 'website/metiers.html', {})

# Nos diplomes
def diplomes(request):
	return render(request, 'website/diplomes.html', {})

# Nos ecoles
def ecoles(request):
	return render(request, 'website/ecoles.html', {})

# Nos stages
def stages(request):
	return render(request, 'website/stages.html', {})

# Nos incubateurs
def incubateurs(request):
	return render(request, 'website/incubateurs.html', {})

# Nos universites
def universites(request):
	return render(request, 'website/universites.html', {})

# Nos evenements
def evenements(request):
	return render(request, 'website/evenements.html', {})


######################################################################################
#																					 #
#                               MANAGE ORAPEF SITE                                   #
#																					 #
######################################################################################