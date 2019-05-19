import xadmin
from xadmin import views
from apps.main.models import Banner, StarImage, StarBasicInfo, UploadImage, StarDesc


# 配置样式
class BaseStyleSettings:
    # 开启主题修改
    enable_themes = True
    # 使用bootstrap样式
    use_bootswatch = True


# 将xadmin默认样式替换成自己的类
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


# 配置后台名称和下方名称
class GlobalSettings:
    site_title = "星鉴识图网后台管理平台"
    site_footer = "星鉴识图，鉴你所见"


# 将xadmin默认样式替换成自己的类
xadmin.site.register(views.CommAdminView, GlobalSettings)


# 轮播图管理
class BannerAdmin:
    # 默认情况下显示object对象
    list_display = ["banner_id",
                    "image",
                    "detail_url",
                    "create_time",
                    "is_delete"
                    ]
    search_fields = ["image"]
    list_per_page = 5


# 将xadmin默认样式替换成自己的类
xadmin.site.register(Banner, BannerAdmin)


# 明星信息管理
class StarBasicInfoAdmin:
    # 默认情况下显示object对象
    list_display = ["star_id",
                    "star_name",
                    "star_sex",
                    "star_birth",
                    "star_weight",
                    "star_height",
                    "star_career",
                    "star_nationality",
                    "star_constellation",
                    "star_graduated_school",
                    "star_economic_company",
                    "star_representative",
                    "star_major_achievements",
                    "create_time",
                    "is_delete",
                    ]

    search_fields = ["star_name"]

    list_per_page = 5


# 将xadmin默认样式替换成自己的类
xadmin.site.register(StarBasicInfo, StarBasicInfoAdmin)


# 明星图片管理
class StarImageAdmin:
    # 默认情况下显示object对象
    list_display = ["image_id",
                    "image_name",
                    "image_type",
                    "image_location",
                    "star",
                    "create_time",
                    "is_delete"
                    ]
    search_fields = ["image_name"]
    list_per_page = 5


# 将xadmin默认样式替换成自己的类
xadmin.site.register(StarImage, StarImageAdmin)


# 上传图片管理
class UploadImageAdmin:
    # 默认情况下显示object对象
    list_display = ["image_id",
                    "image_name",
                    "image_charset",
                    "image_size",
                    "image_location",
                    "is_handle",
                    "create_time",
                    "is_delete"
                    ]
    search_fields = ["image_name"]

    list_per_page = 5


# 将xadmin默认样式替换成自己的类
xadmin.site.register(UploadImage, UploadImageAdmin)


# 明星简介管理
class StarDescAdmin:
    # 默认情况下显示object对象
    list_display = ["desc_id",
                    "desc",
                    "create_time",
                    "star",
                    "is_delete"
                    ]
    search_fields = ["desc"]
    list_per_page = 5


# 将xadmin默认样式替换成自己的类
xadmin.site.register(StarDesc, StarDescAdmin)
