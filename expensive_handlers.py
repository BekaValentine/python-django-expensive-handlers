from django.db import models
from django.conf.urls import url
from django.urls import path


class MyModel(models.Model):
  pass

def cheap_handler():
  pass

def expensive_handler_save():
  MyModel().save()

def expensive_handler_delete():
  MyModel().delete()

def expensive_handler_update():
  MyModel().update()

def expensive_handler_create():
  MyModel.objects.create()

def expensive_handler_create_indirect():
  helper()

def helper():
  MyModel.objects.create()

patterns = [
  url("cheap_handler", cheap_handler),
  url("expensive_handler_save", expensive_handler_save),
  path("expensive_handler_delete", expensive_handler_delete)
]
