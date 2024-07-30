# Generated by Django 3.0 on 2024-07-24 12:20
from django.db import migrations

def migrate_profile_data(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile(
            id=old_profile.id,
            favorite_city=old_profile.favorite_city,
            user=User.objects.get(id=old_profile.user.id)
        )
        new_profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profile_data),
    ]
