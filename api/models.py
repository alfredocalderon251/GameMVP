from django.db import models
from tastypie.resources import ModelResource,fields, ALL
from tastypie.authorization import Authorization
from app.models import cart



# Create your models here.

#class CartCount(ModelResource):
#    class Meta:
#        queryset=cart.objects.all().count()
#        resource_name="CartCount"
#        allowed_methods=['get']
#        authorization=Authorization()
#        def get_object_list(self, request):
#            cartcount= cart.objects.all().filter(user=request.user).count()
#            return cartcount