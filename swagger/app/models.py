from django.db import models

class Emissions(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    date_created = models.DateField(null=False)
    accounting_period = models.CharField(null=False, max_length=8)
    scope1 = models.IntegerField(null=True)
    scope2 = models.IntegerField(null=True)
    scope3 = models.IntegerField(null=True)


# from app.models import Emissions
# from app.serializers import EmissionSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# ### create data values
# emission = Emissions(date_created="2023-05-10", accounting_period="fiscal", scope1=33)
# emission.save()
# emission = Emissions(date_created="2023-12-15", accounting_period="calendar", scope1=29, scope2=44, scope3=54)
# emission.save()

# ### serialize instance 
# serializer = EmissionSerializer(emission)
# serializer.data

# ### render json
# content = JSONRenderer().render(serializer.data)
# content
