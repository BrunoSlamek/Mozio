from django.contrib.gis.db import models as gis_models
from django.db import models


class BaseModel(models.Model):
    """
    Abstract base class that provides self-updating 'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Provider(BaseModel):
    """
    Represents a transportation service provider, including their contact information,
    language, and preferred currency.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)

    class Meta:
        db_table = 'provider'
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        ordering = ['name']
        db_table_comment = "Stores data about providers, including contact details, language, and currency preferences."

    def __str__(self):
        return f"{self.name} ({self.email})"


class ServiceArea(BaseModel, gis_models.Model):
    """
    Represents the service areas that providers serve. Each service area has a name, price,
    and geographical boundaries (geojson). The area is linked to a provider.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    geojson = gis_models.PolygonField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='service_areas')

    class Meta:
        db_table = 'service_area'
        verbose_name = "Service Area"
        verbose_name_plural = "Service Areas"
        ordering = ['name', 'price']
        db_table_comment = "Stores service area polygons and pricing information linked to providers."

    def __str__(self):
        return f"{self.name} - {self.provider.name}"
