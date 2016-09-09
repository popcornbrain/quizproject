from django.db import models

class Quiz(models.Model):
		quiz_number=models.PositiveIntegerField()
		name=models.CharField(max_lenght=100)
		description=models.TextField()

class Question(models.Model):
		question=models.TextField()
		answer1=models.CharField(max_lenght=100)
		answer2=models.CharField(max_lenght=100)
		answer3=models.CharField(max_lenght=100)
		quiz=models.ForeignKey(Quiz, related_name="questions")

