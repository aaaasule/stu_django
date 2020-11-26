from django.db import models


# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128, null=False)
    password = models.CharField(max_length=128, null=False)
    registertime = models.DateTimeField(auto_now_add=True)
    sex = models.IntegerField()

    def __str__(self):  # 返回对象信息
        return self.username + ":" + str(self.uid) + ":" + str(self.sex)

    class Meta:
        db_table = "user"
