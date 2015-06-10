# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_id', models.IntegerField(db_index=True)),
                ('object_id', models.IntegerField(db_index=True)),
                ('alias', models.CharField(max_length=255, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('object_type', models.ForeignKey(related_name='related_relatedobject', to='contenttypes.ContentType')),
                ('parent_type', models.ForeignKey(related_name='child_relatedobject', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
    ]
