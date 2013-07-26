# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'directory_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'directory', ['Page'])

        # Adding model 'Image'
        db.create_table(u'directory_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Page'])),
        ))
        db.send_create_signal(u'directory', ['Image'])

        # Adding model 'Sponsor'
        db.create_table(u'directory_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'directory', ['Sponsor'])

        # Adding model 'Text'
        db.create_table(u'directory_text', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Page'])),
        ))
        db.send_create_signal(u'directory', ['Text'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'directory_page')

        # Deleting model 'Image'
        db.delete_table(u'directory_image')

        # Deleting model 'Sponsor'
        db.delete_table(u'directory_sponsor')

        # Deleting model 'Text'
        db.delete_table(u'directory_text')


    models = {
        u'directory.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['directory.Page']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'directory.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'directory.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'directory.text': {
            'Meta': {'object_name': 'Text'},
            'entry': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['directory.Page']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['directory']