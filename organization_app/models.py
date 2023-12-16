from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Organization(models.Model):
    title = models.CharField(
        'Название',
        max_length=100,
    )

    def __str__(self):
        return self.title


class Department(MPTTModel):
    title = models.CharField(
        'Название',
        max_length=100,
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Подразделение',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    organization = models.ForeignKey(
        'Organization',
        verbose_name='Организация',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='departments',
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
    )
    department = models.ManyToManyField(
        'Department',
        verbose_name='Подразделение',
        blank=True,
        null=True,
        related_name='roles',
    )

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100,
    )
    department = models.ForeignKey(
        'Department',
        verbose_name='Подразделение',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='units',
    )
    role = models.ManyToManyField(
        'Role',
        verbose_name='Роль',
        blank=True,
        null=True,
        related_name='units',
    )

    def __str__(self):
        return self.name
