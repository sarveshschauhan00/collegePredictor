from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse



ls = "OPEN,OPEN (PwD),EWS,EWS (PwD),OBC-NCL,OBC-NCL (PwD),SC,SC (PwD),ST,ST (PwD)".split(",")

class RankTable(models.Model):

    gender = models.CharField(max_length=50,
                              choices=(('Gender-Neutral', 'Male'), ('Female-only (including Supernumerary)', 'Female')),
                              blank=False,
                              default='M')
    percentile = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        blank=True,
        null=True,
    )
    catagory = models.CharField(max_length=15,
                                choices=((ele, ele) for ele in ls),
                                default='OPEN'
                                )
    main_catagory_rank = models.IntegerField(blank=True, null=True,
                                        validators=[MinValueValidator(0)],)
    advanced_general_rank = models.IntegerField(blank=True, null=True,
                                        validators=[MinValueValidator(0)],)
    advanced_catagory_rank = models.IntegerField(blank=True, null=True,
                                        validators=[MinValueValidator(0)],)


    def get_absolute_url(self):
        return reverse('home')
