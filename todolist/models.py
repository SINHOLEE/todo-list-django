from .utils import PriorityTypes
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField('todo-item', max_length=255)
    created = models.DateTimeField('생성시간', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('수정시간', auto_now=True, auto_now_add=False)
    is_completed = models.BooleanField('완료여부', default=False)
    priority = models.IntegerField(choices=PriorityTypes.choices())

    def get_priority_type_label(self):
        return PriorityTypes(self.priority).name.title()
    class Meta:

        ordering = ['created']
