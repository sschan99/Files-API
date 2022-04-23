from django.db import models
from os import mkdir

class File(models.Model):
    file = models.FileField(upload_to="upload/", blank=True)
    name = models.CharField(max_length=100, blank=True)
    is_folder = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    size = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_folder:
            path = 'upload/' + self.name
            mkdir(path)
        else:
            self.name = self.file.name
            self.size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name