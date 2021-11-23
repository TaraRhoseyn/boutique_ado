from django.db import models

# the 'models.Model' below is making sure our model can do everything the base model from Django can (see import above too)
class Item(models.Model):
    # Django will create ID automatically
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name