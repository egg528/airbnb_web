from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # 생성할 때 자동으로 시간 추가
    created = models.DateTimeField(auto_now_add=True)
    # 저장할 때 자동으로 시간 추가
    updated = models.DateTimeField(auto_now=True)

    # 해당 클래스는 데이터 베이스에 저장되지 않고 상속받은 타 모델만 저장되도록
    class Meta:
        abstract = True
