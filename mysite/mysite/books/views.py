from django.shortcuts import render

from django.db.models import Q
from django.shortcuts import render
from .models import Book

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.mail import send_mail

