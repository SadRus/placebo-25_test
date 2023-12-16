# Generated by Django 4.2 on 2023-12-16 20:16

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='organization_app.department', verbose_name='Подразделение'),
        ),
        migrations.RemoveField(
            model_name='unit',
            name='role',
        ),
        migrations.AddField(
            model_name='unit',
            name='role',
            field=models.ManyToManyField(blank=True, null=True, related_name='units', to='organization_app.role', verbose_name='Роль'),
        ),
    ]
