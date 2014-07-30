# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'main_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'main', ['UserProfile'])

        # Deleting field 'Post.recipient_id'
        db.delete_column(u'main_post', 'recipient_id')

        # Deleting field 'Post.author_id'
        db.delete_column(u'main_post', 'author_id')

        # Deleting field 'Post.recipient_name'
        db.delete_column(u'main_post', 'recipient_name')

        # Deleting field 'Post.author_name'
        db.delete_column(u'main_post', 'author_name')

        # Adding field 'Post.author'
        db.add_column(u'main_post', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='post', to=orm['main.UserProfile']),
                      keep_default=False)

        # Adding field 'Post.recipient'
        db.add_column(u'main_post', 'recipient',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='something', to=orm['main.UserProfile']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'main_userprofile')

        # Adding field 'Post.recipient_id'
        db.add_column(u'main_post', 'recipient_id',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Post.author_id'
        db.add_column(u'main_post', 'author_id',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Post.recipient_name'
        db.add_column(u'main_post', 'recipient_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Post.author_name'
        db.add_column(u'main_post', 'author_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'Post.author'
        db.delete_column(u'main_post', 'author_id')

        # Deleting field 'Post.recipient'
        db.delete_column(u'main_post', 'recipient_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['main']