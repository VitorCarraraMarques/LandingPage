from landingPage.models import *

class Project(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField()
    id = models.UUIDField(primary_key=True)

    def __str__(self):
        return self.name