from django.db import models
from django.contrib.auth.models import User

# Questions Model
class Question(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=255,null=True,blank=True)
    body        = models.TextField(null=True,blank=True)
    likes       = models.ManyToManyField(User, related_name='liked_questions', blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name_plural = 'Questions'
        ordering            = ['-created_at']
        indexes             = [models.Index(name='questions',fields=['user','title'])]

# Answer Model
class Answer(models.Model):
    question    = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    body        = models.TextField(null=True,blank=True)
    likes       = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Answer by {self.user.username}'

    class Meta:
        verbose_name_plural = 'Answers'
        ordering            = ['-created_at']
        indexes             = [models.Index(name='answers', fields=['question', 'user'])]
