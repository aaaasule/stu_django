from django.contrib import admin
from myapp.models import Grade, Student

# Register your models here.
# 注册
admin.register(Grade)
admin.register(Student)


class StudentLine(admin.StackedInline):
    model = Student
    extra = 2


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentLine]
    list_display = ['pk', 'name', 'boyNum', 'girlNum']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 列表页
    def sex(self):
        if self.sex:
            return "男"
        return '女'

    sex.short_description = '性别'

    list_display = ['pk', 'name', 'age', sex, 'content', 'grade_id', 'isDelete']
    list_filter = ['grade_id']
    search_fields = ['age']
    list_per_page = 6
    actions_on_top = False
    actions_on_bottom = True
    # 添加、修改页

    fieldsets = [
        ('base', {'fields': ['name', 'sex', 'age']}),
        ('more', {'fields': ['contents', 'grade', 'isDelete']})
    ]
