from django.db import models


# Create your models here.
class Linux(models.Model):
    # unique:如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的
    # IPAddressField：点分十进制表示的IP地址，如10.0.0.1
    # id = models.AutoField(primary_key=True, unique=True)
    linux_ip = models.GenericIPAddressField(protocol='IPv4', unique=True)
    linux_name = models.CharField(max_length=32)
    linux_cpu = models.IntegerField(default=10)
    linux_notes = models.CharField(max_length=258)

    # 修改表名
    class Meta:
        db_table = "Linux"
