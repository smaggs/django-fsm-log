# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StateLog.reason'
        db.alter_column(u'django_fsm_log_statelog', 'reason', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

    def backwards(self, orm):

        # Changing field 'StateLog.reason'
        db.alter_column(u'django_fsm_log_statelog', 'reason', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        "%s.%s" % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_fsm_log.statelog': {
            'Meta': {'object_name': 'StateLog'},
            'by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s.%s']" % (User._meta.app_label, User._meta.object_name), 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'transition': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_fsm_log']
