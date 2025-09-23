from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User




UniqData = UniqueValidator(queryset=User.objects.all())


    


