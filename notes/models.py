from django.db import models

class Note(models.Model):
    class SubjectType(models.TextChoices):
        Python = 'Python'
        terminal = 'Terminal'
        django_the_great = 'Django'

    subject = models.CharField(max_length=40, choices = SubjectType.choices)
    explanation = models.TextField()
    rate_understanding = models.PositiveIntegerField()
    revised_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Subject: {self.subject}'





    
    
    
