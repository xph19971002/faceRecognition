from django.db import models


class Test(models.Model):
    t_id = models.AutoField(primary_key=True, default=1)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = "test"
