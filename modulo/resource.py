from import_export import resources  
from .models import Trabajo


class TrabajoResource(resources.ModelResource):  
   class Meta:  
     model = Trabajo