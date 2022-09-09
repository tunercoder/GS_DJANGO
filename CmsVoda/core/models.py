from django.db import models

class Human(models.Model):
    
    msisdn = models.IntegerField()
    requestdatetime = models.DateTimeField()
    smstext = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.msisdn} {self.requestdatetime} {self.smstext}'



class TblSmsq(models.Model):
    smsq_int_id = models.BigAutoField(primary_key=True)
    smsq_int_msisdn = models.BigIntegerField()
    smsq_int_dnis = models.PositiveBigIntegerField()
    smsq_int_clipid = models.PositiveIntegerField()
    smsq_int_categoryid = models.PositiveIntegerField()
    smsq_str_channel = models.CharField(max_length=15)
    smsq_str_smstext = models.CharField(max_length=500)
    smsq_str_callid = models.CharField(max_length=50)
    smsq_str_smssender = models.CharField(max_length=250)
    smsq_dtm_request_time = models.DateTimeField()
    smsq_dtm_processat = models.DateTimeField()
    smsq_str_appname = models.CharField(max_length=50)
    smsq_int_priorityflag = models.IntegerField(blank=True, null=True)
    smsq_int_chkdndflag = models.IntegerField(blank=True, null=True)
    smsq_int_qflag = models.IntegerField(blank=True, null=True)
    smsq_str_circlecode = models.CharField(max_length=6)
    smsq_int_srvid = models.PositiveIntegerField()
    smsq_str_subscribertype = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tbl_smsq'
