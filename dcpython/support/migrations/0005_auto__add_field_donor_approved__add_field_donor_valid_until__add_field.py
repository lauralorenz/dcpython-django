# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Donor.approved'
        db.add_column(u'support_donor', 'approved',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Donor.valid_until'
        db.add_column(u'support_donor', 'valid_until',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donation.valid_until'
        db.add_column(u'support_donation', 'valid_until',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Donation.level'
        db.add_column(u'support_donation', 'level',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Donor.approved'
        db.delete_column(u'support_donor', 'approved')

        # Deleting field 'Donor.valid_until'
        db.delete_column(u'support_donor', 'valid_until')

        # Deleting field 'Donation.valid_until'
        db.delete_column(u'support_donation', 'valid_until')

        # Deleting field 'Donation.level'
        db.delete_column(u'support_donation', 'level')


    models = {
        u'support.donation': {
            'Meta': {'object_name': 'Donation'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'donation': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['support.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'valid_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'support.donor': {
            'Meta': {'object_name': 'Donor'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'public_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'public_slogan': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'public_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'valid_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['support']