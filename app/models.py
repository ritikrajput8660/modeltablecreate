from django.db import models

# Create your models here.

class cricket(models.Model):
    cricketteam = models.CharField(max_length=30,primary_key=True)
    def __str__(self) -> str:
        return self.cricketteam
    
class teamplayer(models.Model):
    team_name = models.ForeignKey(cricket,on_delete=models.CASCADE)
    playername = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.playername

# class Topic(models.Model):
#     topid_name = models.CharField(max_length=10,primary_key=True)
#     def __str__(self) :
#         return self.topid_name
    
# class Sport(models.Model):
#     topid_name = models.ForeignKey(Topic,on_delete= models.CASCADE)
#     s_name = models.CharField(max_length=20)
#     def __str__(self) :
#         return self.s_name

# class PlayerName(models.Model):
#     S_name = models.ForeignKey(Sport,on_delete = models.CASCADE)
#     name = models.CharField(max_length=30)
#     def __str__(self) :
#         return self.name
