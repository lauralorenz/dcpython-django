# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Donor.balanced_uri'
        db.delete_column(u'support_donor', 'balanced_uri')


        # Changing field 'Donor.name'
        db.alter_column(u'support_donor', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Adding field 'Donation.transaction_id'
        db.add_column(u'support_donation', 'transaction_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Donor.balanced_uri'
        raise RuntimeError("Cannot reverse this migration. 'Donor.balanced_uri' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Donor.balanced_uri'
        db.add_column(u'support_donor', 'balanced_uri',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Donor.name'
        raise RuntimeError("Cannot reverse this migration. 'Donor.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Donor.name'
        db.alter_column(u'support_donor', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'Donation.transaction_id'
        db.delete_column(u'support_donation', 'transaction_id')


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
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['support']