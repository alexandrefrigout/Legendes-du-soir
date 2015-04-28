from django.db import models

class Ibook(models.Model):
		LANGUAGE = (
			('FR', 'Francais'),
			('ES', 'Espagnol'),
			('CH', 'Chinois'),
			('EN', 'Anglais'),
		)
		TYPE = (
			('Conte', 'Conte'),
			('Fable', 'Fable'),
		)

		titre =  models.CharField(max_length=200)
		booktype = models.CharField(max_length=10, choices=TYPE, default='Fable')
		langue = models.CharField(max_length=2, choices=LANGUAGE, default='Francais')
		resume = models.TextField()
		idapple = models.CharField(max_length=250)
