from django.db import models



class Aspirant(models.Model):
    first_name=models.CharField(null=False,max_length=20)
    second_name=models.CharField(null=False,max_length=20)
    program_of_study=models.CharField(max_length=50,null=False)
    image=models.ImageField(upload_to='')
    def __str__(self):
        return f'{self.first_name} {self.second_name}'
    


class Vote(models.Model):
    name=models.ForeignKey(Aspirant,on_delete=models.CASCADE)
    votes=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
   