from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def handle_add(request):
    User.objects.bulk_create([User(username="jdd", password="123456"), User(username="hzl", password="123456"),
                              User(username="yudi", password="123456")])

    return HttpResponse("add Success")


def handle_curd(request):
    # user = User.objects.get(pk=1)
    # username = user.username

    #  查询结果集 QuerySet
    # data = User.objects.all()
    # print(data)

    # 获取一条
    # data = data.first()
    # print("data")

    # filter 过滤结果集
    # result_data = data.filter(uid__lt=20)  # uid < 20
    # result_data = result_data.filter(uid__gt=10)  # uid > 10
    #
    # print(result_data)

    #  按username 升序排列
    # data = User.objects.order_by('username')
    # for user in data:
    #     print(user.username)

    # 限制结果集
    # data = User.objects.order_by('username')[:2]
    # data = User.objects.order_by('-uid')[4:9]
    # for user in data:
    #     print(user.username, user.uid)

    # 指定字段
    # data = User.objects.all().values('username')
    # for user in data:  # user 是字典类型
    #     print(user)

    #  去重
    # data = User.objects.all().values('password').distinct()[:10]
    # data = User.objects.values('password').distinct()[:10]
    # print(data)
    # for user in data:
    #     print(user)
    #
    # #  反序
    # data = User.objects.order_by("uid").reverse()
    # print(data)

    return HttpResponse("curd Success")


def handle_query(request):
    #  非过滤器方法
    #  get只能返回一条记录
    # user = User.objects.get(pk=1)
    # print(user.username, user.password)

    # first 返回一个模型对象
    # user = User.objects.first()
    # print(user)

    # last 最后一条记录
    # user = User.objects.last()
    # print(user)

    # 返回最近增加记录
    # user = User.objects.latest()
    # print(user)

    # 结果集中记录数
    # num = User.objects.filter(uid__lt=10).count()
    # print(num)

    # 判断结果集是否存在
    flag = User.objects.filter(uid__gt=22).exists()
    print(flag)
    return HttpResponse("Query")


# 查询条件的写法
def handle_filter(request):
    # 关系运算
    """
    >=  uid__gte=1
    >   uid__gt=1
    <=  uid__lte=1
    <   uid__lt=1
    ==  uid=1
    !=
    """
    #  filter 多个条件 逻辑 与
    # data = User.objects.filter(uid__gt=5, uid__lt=10)

    # in 集合运算
    # data = User.objects.filter(uid__in=[1, 2, 3, 4, 5, 6])

    # 模糊查询
    # data = User.objects.filter(username__contains="ji")
    # print(data[0].username)

    # is null  判空
    # data = User.objects.filter(sex__isnull=True)

    # 字符串操作
    # data = User.objects.filter(username__startswith="ji")
    # data = User.objects.filter(username__endswith="ye")

    # regex 正则匹配
    # data = User.objects.filter(username__regex=r"^y")

    # 日期查询
    data = User.objects.filter(registertime__year=2020)

    print(data)

    return HttpResponse("Filter")


def handle_group(request):
    from django.db.models import Max, Avg, Sum, Count
    #  统计函数用法
    # 获取最大值
    # user = User.objects.aggregate(Max('uid'))

    # 分组   根据values中的值分组; annotate 统计字段; select sex,count(uid) from user group by sex;
    # data = User.objects.values('sex').annotate(Count('uid'))  # QuerySet  查询结果集
    # data = data.filter(uid__gt=7)  # 再次过滤 select sex,count(uid) from user group by sex having uid > 7;

    #  Q 对象  构造 逻辑或、逻辑非; 和F 对象
    # data = User.objects.filter(Q(uid=1) | Q(sex=1))  # 或
    # data = User.objects.filter(~Q(uid__gt=7))  # 非 逻辑取反  gt 大于  uid 小于等于7   不能处理null

    # F对象：把sex 看成USer的一个列名
    data = User.objects.filter(uid=F('sex'))
    # <QuerySet [<User: james:7:7>, <User: neymar:10:10>, <User: xdd:13:13>]>

    print(data)
    return HttpResponse("Group")


def handle_sql(request):
    #  原生SQL
    # user = User.objects.raw("select * from USER ")
    # print(user)

    # 防止sql注入  拼接符使用 %s  不用 format
    user = User.objects.raw("select * from USER where username=%s ", ['jiye' or 'yuran'])
    print(list(user), type(user))  # [<User: jiye:1:None>] <class 'django.db.models.query.RawQuerySet'>

    return HttpResponse("SQL")
