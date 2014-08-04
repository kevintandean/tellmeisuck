# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.email'
        db.add_column(u'main_userprofile', 'email',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.email'
        db.delete_column(u'main_userprofile', 'email')


    models = {
        u'main.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post'", 'to': u"orm['main.UserProfile']"}),
            'bad': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'good': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'something'", 'to': u"orm['main.UserProfile']"})
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'new': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['main']