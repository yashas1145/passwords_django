from django.db import models

# Create your models here.

class password(models.Model):
    url = models.URLField()
    password = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'Passwords'
        
    def __str__(self):
        return 'URL: {} Password: {}'.format(self.url, self.password)
    