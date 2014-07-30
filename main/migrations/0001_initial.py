# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'main_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('recipient_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('recipient_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('good', self.gf('django.db.models.fields.TextField')(null=True)),
            ('bad', self.gf('django.db.models.fields.TextField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'main_post')


    models = {
        u'main.post': {
            'Meta': {'object_name': 'Post'},
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'bad': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'good': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'recipient_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['main']