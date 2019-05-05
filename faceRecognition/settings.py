import os
import sys

# 获取当前文件的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps添加python扫描的路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 加密
SECRET_KEY = '+ta4n+ec49^2xq8%b!ng(eczl2o%37bj@1kg4+)=3=-i+u6yc!'

# 测试环境
DEBUG = True

ALLOWED_HOSTS = []

# ----------------------------------------------------------------------
#                            app注册配置
# ----------------------------------------------------------------------

SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 第三方功能模块
EXT_APPS = [
    'crispy_forms',  # 必须添加
    'xadmin',  # 必须添加
    'reversion',  # 非必要添加 修改后台样式用
]

# 自定义功能模块
CUSTOM_APPS = [
    'apps.main',
    'apps.result',
]

INSTALLED_APPS = SYS_APPS + CUSTOM_APPS + EXT_APPS

# ----------------------------------------------------------------------
#                            中间件配置
# ----------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由配置文件
ROOT_URLCONF = 'faceRecognition.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 指定模板路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 部署有关文件配置，指向wsgi.py
WSGI_APPLICATION = 'faceRecognition.wsgi.application'

# ----------------------------------------------------------------------
# 数据库配置
# ----------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'faceDB',
        'POST': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
    }
}

# ----------------------------------------------------------------------
#                      自带auth模块用户密码验证配置
# ----------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ----------------------------------------------------------------------
#                             后台配置
# ----------------------------------------------------------------------

# 语言配置
LANGUAGE_CODE = 'zh-hans'

# 时区配置
TIME_ZONE = 'Asia/Shanghai'

# 国际化配置,自动转化多个语言
USE_I18N = True
USE_L10N = True

# 不使使用django的时区,使用系统时区
USE_TZ = False

# ----------------------------------------------------------------------
#                          静态文件访问路径配置
# ----------------------------------------------------------------------

# 根目录静态文件的访问路径
STATIC_URL = '/static/'

# 不同功能模块下静态文件路径配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static'),
    os.path.join(BASE_DIR, 'apps/result/static'),
)

# ----------------------------------------------------------------------
#                              文件上传配置
# ----------------------------------------------------------------------

# 访问多媒体文件的路径
MEDIA_URL = '/media/'
# 上传文件的根路径， 字符类型
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ----------------------------------------------------------------------
#                               缓存的配置
# ----------------------------------------------------------------------

# pip install django-redis
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             # 'PASSWORD':123
#             # 使用线程池管理连接
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     },
#     'session': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         "LOCATION": "redis://192.168.50.16:6379/3",
#         "OPTIONS": {
#             # 'PASSWORD':123
#             # 使用线程池管理连接
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     },
# }


# ----------------------------------------------------------------------
#                             session会话维持配置
# ----------------------------------------------------------------------

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "session"
#
# # session失效的时间 7天
# SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒


# ----------------------------------------------------------------------
#                               邮件配置
# ----------------------------------------------------------------------
# 传递消息时使用的redis 的ip 端口 数据库名
BROKER_URL = 'redis://127.0.0.1:6379/2'

# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'

# 发送邮件端口
EMAIL_PORT = 25

# 用户收到邮件显示的邮箱
DEFAULT_FROM_EMAIL = 'xph19971002@163.com'

# 邮箱账号
EMAIL_HOST_USER = 'xph19971002@163.com'

# 授权码
EMAIL_HOST_PASSWORD = 'xipenghao456'

# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True

# 发送超时时间
# EMAIL_TIMEOUT = 120


# ----------------------------------------------------------------------
#                               日志配置
# ----------------------------------------------------------------------
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }
