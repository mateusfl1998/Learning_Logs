from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text