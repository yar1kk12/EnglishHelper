from django.db import models

# Create your models here.
class PhrasalVerbs(models.Model):
    def __str__(self):
        return self.phrasal_verb

    phrasal_verb = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    example = models.CharField(max_length=140, null=True)




