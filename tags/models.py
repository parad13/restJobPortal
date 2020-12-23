from django.db import models

# Create your models here.

# TAG_TYPE = (
#     ("1", "PHP"),
#     ("2", "Larvel"),
#     ("3", "Python"),
#     ("4", "Django"),
#     ("5", "Database"),
#     ("12", "Angular"),
# )

class Tag(models.Model):
    # name = models.CharField(choices=TAG_TYPE,max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
