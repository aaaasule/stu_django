from django.db import models


# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=20)
    boyNum = models.IntegerField()
    girlNum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "grades"


class Student(models.Model):
    """
    django 升级到2.0之后， 表与表之间关联的时候，必须要写on_delete参数

    on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
	on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
	on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
	on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
	# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
	on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
	# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
	on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
	on_delete=models.SET,         # 删除关联数据,
	 a. 与之关联的值设置为指定值,设置：models.SET(值)
	 b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)


    多对多没有on_delete参数  所以以上只针对外键和一对一
    """
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField()
    content = models.CharField(max_length=40)
    # 外键   在表中字段为grade_id
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"
