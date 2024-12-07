from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Category(models.Model):
    parent = models.ForeignKey(to="self", verbose_name=_("parent"), on_delete=models.CASCADE, 
                               related_name="categories", null=True, blank=True)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), blank=True)
    is_active = models.BooleanField(_("is active"), default=True)
    avatar = models.ImageField(_("avatar"), blank=True, upload_to="categories/file/")
    created_time = models.DateTimeField(_("created time"), auto_now_add=True)
    updated_time = models.DateTimeField(_("updated time"), auto_now=True)

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


# class Product(models.Model):
#     pass


# class ProductFile(models.Model):
#     pass