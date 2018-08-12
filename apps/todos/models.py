from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
        db_table = 'todos'
        ordering = ['name']