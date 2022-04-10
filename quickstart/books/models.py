from datetime import datetime
from django.db import models

class Book(models.Model):
    full_title = models.TextField()
    title = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    return_date = models.DateField(null=True)

    def check_availability(self):
        if self.return_date is not None and self.return_date > datetime.now():
            return f"Book not available. Check again after {self.return_date}"
        if not self.is_available:
            return "Book not available" 
        return "Available"