from django.db import models


# 轮播图表
class Banner(models.Model):
    banner_id = models.AutoField(verbose_name='ID', primary_key=True)
    image = models.CharField(verbose_name=u'轮播图', null=False, max_length=128)
    detail_url = models.CharField(verbose_name=u'访问地址', max_length=255, null=False)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'banner'
        verbose_name = u'轮播图管理'
        # 无复数设置
        verbose_name_plural = verbose_name


# 明星基本信 息表
class StarBasicInfo(models.Model):
    star_id = models.AutoField(verbose_name='ID', primary_key=True)
    star_name = models.CharField(verbose_name=u'姓名', max_length=64, null=False, unique=True)
    star_sex = models.CharField(verbose_name=u'性别', max_length=32, null=True, blank=True)
    star_birth = models.DateField(verbose_name=u'出生日期', null=True, blank=True)
    star_weight = models.IntegerField(verbose_name=u'体重', null=True, blank=True)
    star_height = models.IntegerField(verbose_name=u'身高', null=True, blank=True)
    star_career = models.CharField(verbose_name=u'职业', max_length=128, null=True, blank=True)
    star_nationality = models.CharField(verbose_name=u'国籍', max_length=128, null=True, blank=True)
    star_constellation = models.CharField(verbose_name=u'星座', max_length=128, null=True, blank=True)
    star_graduated_school = models.CharField(verbose_name=u'毕业院校', max_length=128, null=True, blank=True)
    star_economic_company = models.CharField(verbose_name=u'经济公司', max_length=128, null=True, blank=True)
    star_representative = models.CharField(verbose_name=u'主要作品', max_length=128, null=True, blank=True)
    star_major_achievements = models.CharField(verbose_name=u'主要成就', max_length=128, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'star_basic_info'
        verbose_name = u'明星信息管理'
        # 无复数设置
        verbose_name_plural = verbose_name


# 图片表
class StarImage(models.Model):
    image_id = models.AutoField(verbose_name='ID', primary_key=True)
    image_name = models.CharField(verbose_name='图片名称', max_length=128, null=False)
    image_type = models.IntegerField(verbose_name=u'图片类型', null=False)
    image_location = models.CharField(verbose_name=u'存储位置', max_length=255, null=False)
    star = models.ForeignKey('StarBasicInfo', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'star_image'
        verbose_name = u'明星图片管理'
        # 无复数设置
        verbose_name_plural = verbose_name


# 用户上传图片表
class UploadImage(models.Model):
    image_id = models.AutoField(verbose_name='ID', primary_key=True)
    image_name = models.CharField(verbose_name='图片名称', max_length=128, null=False)
    image_charset = models.CharField(verbose_name='图片编码', max_length=64, null=True)
    image_size = models.IntegerField(verbose_name="图片大小", null=True)
    image_location = models.CharField(verbose_name=u'存储位置', max_length=255, null=False)
    is_handle = models.BooleanField(verbose_name=u'状态')
    create_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'upload_image'
        verbose_name = u'上传图片管理'
        # 无复数设置
        verbose_name_plural = verbose_name


# 明星描述表
class StarDesc(models.Model):
    desc_id = models.AutoField(verbose_name='ID', primary_key=True)
    desc = models.TextField(verbose_name='明星简介', null=True, blank=True)
    create_time = models.DateField(verbose_name=u'添加时间', auto_now_add=True)
    star = models.OneToOneField("StarBasicInfo", on_delete=models.DO_NOTHING)
    is_delete = models.BooleanField(verbose_name=u'状态', default=False)

    class Meta:
        db_table = 'star_desc'
        verbose_name = u'明星简介管理'
        # 无复数设置
        verbose_name_plural = verbose_name
