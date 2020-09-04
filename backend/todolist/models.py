from django.db import models

# Create your models here.
class Priority(models.Model):
    p_type = models.CharField('우선순위', max_length=50)

    def __str__(self):
        return self.p_type
    

class Todo(models.Model):
    content = models.CharField('todo-item', max_length=255)
    created = models.DateTimeField('생성시간', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True, auto_now_add=False)
    is_completed = models.BooleanField('완료여부', default=False)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todos')
    class Meta:

        ordering = ['created']
