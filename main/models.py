from django.db import models

# Create your models here.


class HelpInstruction(models.Model):
    title = models.CharField(max_length=255, null=True)
    instruction = models.TextField(max_length=1255,  blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title
