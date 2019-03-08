from django.db import models

class Applicant(models.Model):
    TYPE_PERMISSIONS = (
            (1, ("disapproval")),
            (2, ("approval"))
            )
    name = models.CharField(max_length=100)
    student_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    agreement = models.BooleanField(default=False, blank=False)
    permission = models.IntegerField(choices=TYPE_PERMISSIONS, default=1)
    password = models.CharField(max_length=100)
    apply_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def generate(self):
        return self.save()

