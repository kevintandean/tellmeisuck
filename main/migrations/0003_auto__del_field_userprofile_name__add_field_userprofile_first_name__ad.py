# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.name'
        db.delete_column(u'main_userprofile', 'name')

        # Adding field 'UserProfile.first_name'
        db.add_column(u'main_userprofile', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20),
                      keep_default=False)

        # Adding field 'UserProfile.last_name'
        db.add_column(u'main_userprofile', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20),
                      keep_default=False)

        # Adding field 'UserProfile.created'
        db.add_column(u'main_userprofile', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.new'
        db.add_column(u'main_userprofile', 'new',
                      self.gf('django.db.models.fields.CharField')(default='ture', max_length=6),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UserProfile.name'
        db.add_column(u'main_userprofile', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Deleting field 'UserProfile.first_name'
        db.delete_column(u'main_userprofile', 'first_name')

        # Deleting field 'UserProfile.last_name'
        db.delete_column(u'main_userprofile', 'last_name')

        # Deleting field 'UserProfile.created'
        db.delete_column(u'main_userprofile', 'created')

        # Deleting field 'UserProfile.new'
        db.delete_column(u'main_userprofile', 'new')


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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'new': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['main']