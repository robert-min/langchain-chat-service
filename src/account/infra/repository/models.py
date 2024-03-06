from django.db import models


class UserAccount(models.Model):
    seq = models.AutoField(primary_key=True)
    id = models.CharField(max_length=500, null=False)
    password = models.BinaryField(null=False)
    status = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = "user_account"
