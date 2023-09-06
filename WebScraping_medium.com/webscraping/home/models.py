from django.db import models

class Search_History(models.Model):
    Blog_Tag = models.CharField(max_length=120)
    Blog_Title = models.TextField()
    Blog_Author = models.CharField(max_length=120)
    Publishing_Date = models.CharField(max_length=120)
    Estimated_Reading_Time = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.Blog_Tag
