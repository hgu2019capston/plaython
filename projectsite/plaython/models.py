from django.db import models

class Applicant(models.Model):
    TYPE_PERMISSIONS = (
            (1, ("disapproval")),
            (2, ("approval"))
            )
    contents = "학부 교육용 서버는 학생과 교원이 교육과 연구를 위한 목적으로 사용되어야 하며, 그 이외의 목적으로 인한 사용은 제한됩니다. 학부 서버는 여러 학생과 교수가 공동으로 사용하는 장비로,  각 사용자는 서버 관리자의 운영에 적극 협조해야 합니다. 다른 사용자의 사용을 방해하는 행위나 다른 사용자의 보안을 해치는 행위, 지속적인 오사용으로 서버 운영에 방해가 있는 경우, 혹은 2개월 이상 사용이 없을 경우 예고 없이 계정과 계정에 속한 파일이 삭제 될 수 있습니다."

    name = models.CharField(max_length=100)
    student_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=100)
    usage = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    permission = models.IntegerField(choices=TYPE_PERMISSIONS, default=1)
    password = models.CharField(max_length=100)
    apply_time = models.DateTimeField(auto_now_add=True)
    agreement = models.TextField(max_length=300, default=contents)
    I_agree = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.name

    def generate(self):
        return self.save()

