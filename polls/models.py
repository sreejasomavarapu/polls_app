from django.db import models

# Create your models here.

class Question(models.Model):
    question_title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_title=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_title


