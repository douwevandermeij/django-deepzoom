# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeepZoom'
        db.create_table(u'deepzoom_deepzoom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('associated_image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('deepzoom_image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('deepzoom_path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('deepzoom_xml', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'deepzoom', ['DeepZoom'])

        # Adding model 'TestImage'
        db.create_table(u'deepzoom_testimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploaded_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('create_deepzoom', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deepzoom_already_created', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'deepzoom', ['TestImage'])


    def backwards(self, orm):
        # Deleting model 'DeepZoom'
        db.delete_table(u'deepzoom_deepzoom')

        # Deleting model 'TestImage'
        db.delete_table(u'deepzoom_testimage')


    models = {
        u'deepzoom.deepzoom': {
            'Meta': {'object_name': 'DeepZoom'},
            'associated_image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deepzoom_image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'deepzoom_path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'deepzoom_xml': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'deepzoom.testimage': {
            'Meta': {'ordering': "['name']", 'object_name': 'TestImage'},
            'create_deepzoom': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deepzoom_already_created': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploaded_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['deepzoom']