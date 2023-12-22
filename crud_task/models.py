from django.db import models

# Create your models here.
class tasktable(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    completed=models.BooleanField()
    
    def __str__(self):
        return self.title