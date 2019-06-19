'''
from polls.models import Question, Choice
from django.utils import timezone
import datetime

now = datetime.datetime.now()

q = Question(question_text="", pub_date=timezone.now())
q.save()
q.id

now = timezone.now()
new = timezone.localtime(now)


'''