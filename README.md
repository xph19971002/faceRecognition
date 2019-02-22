                                                 星鉴人脸识别项目开发说明及参考


----------------------------------------------------------项目开发文档----------------------------------------------------------

1.环境
    python 版本 3.6.0以上3.7.0以下
    django 版本 1.11.12

    创建项目运行环境，github上不上传，手动创建运行环境方法（windows）：
        cmd下：
            1.pip install virtualenv
            下载慢可加源：（pip install virtualenv -i http://pypi.douban.com/simple/）
            2.virtualenv  查看是否安装成功
            3.virtualenv [虚拟环境根目录名称] --python=python3
            4.激活  进入创建好的环境变量根目录scripts中去，cmd中输入activate.bat运行    （windows）
    
    数据库 mysql （连接远程数据库服务器命令：mysql -u[账号] -p[密码] -P[端口号] -h[IP地址]）
        name： frdb
        host：
        port：3306
        username：   root
        password：   root


2.数据库表命名说明

    数据库迁移命令:python manage.py makemigrations [app名称]
    数据库同步命令:python manage.py migrate [app名称]

--------------------------------------------------------------------------------------------------------
                                             数据类型参照表
--------------------------------------------------------------------------------------------------------
                                    models                                            mysql/oracle
    
    自增类型                       AutoField                                           auto_increment       （一把用于id）
    整数           IntegerField/TinyintField/BigIntegerField                             int/number
    单精度浮点                    FloatField/                                              float
    高精度浮点                    DecimalField   必须设置max_digit和decimal_places         decimal         （一般用于金钱）
    
                                                                                          char
    字符                           CharField     必须设置max_length
                                                                                          varchar/varchar2
    
    文本域                        TextField                                               text
    日期                          DateField                                               date
    时间                        DateTimeField                                           datetime/timestamp
    布尔类型                    booleanField                                                bool            （一般用于假删除）
---------------------------------------------------------------------------------------------------------
                                             字段约束参照表
---------------------------------------------------------------------------------------------------------
    主键约束       primary_key = True
    唯一约束       unique = True | False
    最大长度       max_length =
    默认值         default = 0 | True | False
    空值约束       null = True | False
    索引字段       db_index = True
    
                    DateTimeField(auto_now=True | auto_now_add=True)    auto_now每次更新数据库重新赋予时间
    时间约束                                                            auto_now_add 永远为第一次创建的时间
                    DateField
    
    外键约束

---------------------------------------------------------------------------------------------------------
3.第三方库资源说明
    已安装：框架版本控制：  django=1.11.12
            数据库模型相关：pymysql、 Pillow  （用于模型层ImageField）
            会话
            缓存
            后台

    环境导出命令: pip freeze > requirements.txt
    批量环境安装：pip install requirements.txt

4.项目文件夹说明

    4.1 模块功能apps
        所有功能模块集合
        创建app命令: python manage.py startapp [app名称]


    4.2 静态资源文件夹static,建议不同模块创建不同static文件夹
        所有的css，js 资源初步建议直接调用网上cdn
    
    4.3 模板建议一个功能模块一个templates文件夹

5.后台账户

    创建超级管理员
    run manage.py tools:  createsuperuser


---------------------------------------------------------------------------------------------------------
                                            开发问题汇总表
---------------------------------------------------------------------------------------------------------
1.运行报错:
cv2.error: OpenCV(3.4.1) D:\Build\OpenCV\opencv-3.4.1\modules\highgui\src\window.cpp:364:
error: (-215) size.width>0 && size.height>0 in function cv::imshow

原因：
根据提示，判断出是imshow方法没有读取到像素的问题，验证后发现，imread返回值为None，所以应该是图片路径问题，
修改为绝对路径后，依然报错，在开源社区stack overflow找到了解决方法，原因竟是我的路径中存在空格，而opencv
读取路径时碰到空格无法解析，所以就无法读取正确路径。

解决方法：
修改路径（绝对路径）中没有空格存在。

[stack overflow 原文](https://stackoverflow.com/questions/27953069/opencv-error-215size-width0-size-height0-in-function-imshow)


2.Opencv 中文乱码问题

