from django.db import models

class ReadingText(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=200)
    english_text = models.TextField(blank=True, null=True)
    urdu_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} ({self.date})"
