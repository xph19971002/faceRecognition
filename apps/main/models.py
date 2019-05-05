from django.db import models


# 轮播图表
class Banner(models.Model):
    banner_id = models.AutoField(verbose_name='ID', primary_key=True)
    image = models.CharField(verbose_name=u'轮播图', max_length=128, null=False)
    detail_url = models.CharField(verbose_name=u'访问地址', max_length=255, null=False)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'banner'
        # verbose_name = u'轮播图'
        # verbose_name_plural = verbose_name


# 图片表
class Image(models.Model):
    image_id = models.AutoField(verbose_name='ID', primary_key=True)
    image_name = models.CharField(verbose_name='图片名称', max_length=128, null=False)
    image_type = models.IntegerField(verbose_name=u'图片类型', null=False)
    image_location = models.CharField(verbose_name=u'存储位置', max_length=255, null=False)
    star = models.ForeignKey('StarBasicInfo', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'image'


# 用户上传图片表
class UploadImage(models.Model):
    image_id = models.AutoField(verbose_name='ID', primary_key=True)
    image_name = models.CharField(verbose_name='图片名称', max_length=128, null=False)
    image_location = models.CharField(verbose_name=u'存储位置', max_length=255, null=False)
    is_handle = models.BooleanField(verbose_name=u'状态')
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'upload_image'


# 明星基本信 息表
class StarBasicInfo(models.Model):
    star_id = models.AutoField(verbose_name='ID', primary_key=True)
    star_name = models.CharField(verbose_name=u'姓名', max_length=64, null=False, unique=True)
    star_sex = models.CharField(verbose_name=u'性别', max_length=32, null=True)
    star_birth = models.DateField(verbose_name=u'出生日期', default=False, null=True)
    star_weight = models.IntegerField(verbose_name=u'体重', default=False, null=True)
    star_height = models.IntegerField(verbose_name=u'身高', default=False, null=True)
    star_career = models.CharField(verbose_name=u'职业', max_length=128, null=True)
    star_nationality = models.CharField(verbose_name=u'国籍', max_length=128, null=True)
    star_constellation = models.CharField(verbose_name=u'星座', max_length=128, null=True)
    star_graduated_school = models.CharField(verbose_name=u'毕业院校', max_length=128, null=True)
    star_economic_company = models.CharField(verbose_name=u'经济公司', max_length=128, null=True)
    star_representative = models.CharField(verbose_name=u'主要作品', max_length=128, null=True)
    star_major_achievements = models.CharField(verbose_name=u'主要成就', max_length=128, null=False)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'star_basic_info'


# 明星描述表
class StarDesc(models.Model):
    desc_id = models.AutoField(verbose_name='ID', primary_key=True)
    desc = models.TextField(verbose_name='明星简介', null=True)
    create_time = models.DateField(verbose_name=u'添加时间', auto_now_add=True)
    star = models.OneToOneField("StarBasicInfo", on_delete=models.DO_NOTHING)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'star_desc'
