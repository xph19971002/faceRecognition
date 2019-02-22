from django.db import models


class Test(models.Model):
    t_id = models.AutoField(primary_key=True, default=1)
    username = models.CharField(max_length=64, null=False)
    password = models.CharField(max_length=64, null=False)
    is_delete = models.BooleanField(default=False, null=False)
    price = models.DecimalField(max_digits=7,decimal_places=2)

    class Meta:
        db_table = "test"
