from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import Group

admin_group = Group.objects.get(name='admin')
freelancer_group = Group.objects.get(name="freelancers")
contratante = Group.objects.get(name="contractors")





