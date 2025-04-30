from django.db import models
from django.contrib.auth.models import User




class WebApp(models.Model):
    name = models.CharField(max_length=100)
    tar_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    port = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class AppAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(WebApp, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.app.name}"
