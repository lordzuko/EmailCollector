from __future__ import unicode_literals

from django.db import models

class Join(models.Model):
    ref_id = models.CharField(max_length=120,default='none',unique=True)
    refered_by = models.ForeignKey("self", related_name='referer', null=True,blank=True)
    email = models.EmailField()
    ip_address = models.CharField(max_length=15,default='none')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.email

    class Meta:
        unique_together = ('email','ref_id')
