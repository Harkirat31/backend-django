from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    # display product category in admin niterface with name field
    def __str__(self) -> str:
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("SWEDISH_CROWN"))
        YEN = ("JPN", _("YEN"))
        AMERICAN_DOLLAR = ("USD", _("AMERICAN_DOLLAR"))

    name = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    subtitle = models.CharField(max_length=512)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, blank=True, null=True)
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )

    variation_product_ids = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True),
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.subtitle} -{self.maker}"
