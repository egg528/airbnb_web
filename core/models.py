from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # 해당 클래스는 데이터 베이스에 저장되지 않고 상속받은 타 모델만 저장되도록
    class Meta:
        abstract = True
