from django.db import models

# Create your models here.
class dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ninjas(models.Model):
    dojo = models.ForeignKey(dojos, related_name="ninja", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# def __repr__(self):
        # return f"<users object: {self.first_name}, {self.last_name}, {self.email_address}, {self.age}>"