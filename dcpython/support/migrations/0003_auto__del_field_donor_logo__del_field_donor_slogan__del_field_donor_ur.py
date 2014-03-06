# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Donor.logo'
        db.delete_column(u'support_donor', 'logo')

        # Deleting field 'Donor.slogan'
        db.delete_column(u'support_donor', 'slogan')

        # Deleting field 'Donor.url'
        db.delete_column(u'support_donor', 'url')

        # Deleting field 'Donor.contact'
        db.delete_column(u'support_donor', 'contact')

        # Adding field 'Donor.display_name'
        db.add_column(u'support_donor', 'display_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.display_url'
        db.add_column(u'support_donor', 'display_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.display_slogan'
        db.add_column(u'support_donor', 'display_slogan',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.display_logo'
        db.add_column(u'support_donor', 'display_logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Donor.name'
        db.alter_column(u'support_donor', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

    def backwards(self, orm):
        # Adding field 'Donor.logo'
        db.add_column(u'support_donor', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.slogan'
        db.add_column(u'support_donor', 'slogan',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.url'
        db.add_column(u'support_donor', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donor.contact'
        db.add_column(u'support_donor', 'contact',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Donor.display_name'
        db.delete_column(u'support_donor', 'display_name')

        # Deleting field 'Donor.display_url'
        db.delete_column(u'support_donor', 'display_url')

        # Deleting field 'Donor.display_slogan'
        db.delete_column(u'support_donor', 'display_slogan')

        # Deleting field 'Donor.display_logo'
        db.delete_column(u'support_donor', 'display_logo')


        # Changing field 'Donor.name'
        db.alter_column(u'support_donor', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'support.donation': {
            'Meta': {'object_name': 'Donation'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'donation': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['support.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'support.donor': {
            'Meta': {'object_name': 'Donor'},
            'display_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'display_slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'display_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['support']