import datetime
import os
import face_recognition
from django.http import HttpResponse
from django.shortcuts import render
from apps.main.models import UploadImage, StarImage, StarBasicInfo, StarDesc
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def result(request):
    if request.method == "GET":
        return render(request, "search_results.html")
    if request.method == "POST":
        # 接收用户上传图片
        files = request.FILES.getlist("upload-img")
        # 判断上传文件数量
        if len(files) == 0:
            return HttpResponse(u"请选择一个文件!")
        elif len(files) == 1:
            # 允许上传的图片类型
            all_type = [".jpg"]
            # 判断上传文件的大小 自定义上传文件大小限制10M
            max_size = 10485760
            # 获取文件
            file = files[0]
            # 获取文件名
            file_name = file.name
            # 获取文件大小
            file_size = file.size
            # 获取文件编码
            file_charset = file.charset
            # 获取文件后缀
            upload_origin_ext = os.path.splitext(file_name)

            # 自定义允许上传的文件类型
            # 判断文件上传类型
            if upload_origin_ext[1] not in all_type:
                return HttpResponse(f"服务器暂不允许上传{upload_origin_ext[1]}类型的文件")

            # 判断文件大小是否合适
            if file_size > max_size:
                return HttpResponse(u"上传文件大小不能超过10M")
            else:
                # 上传图片静态保存路径
                static_url = u"G:/11.GitHubRepositories/faceRecognition/static/img"
                # 图片重命名
                img_name = "IMG_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
                # 图片保存最终的位置及名称
                unknown_img_name = static_url + '/upload_img/' + img_name
                # 保存到本地
                with open(unknown_img_name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                # 保存进数据库
                upload_image_info = UploadImage(
                    image_name=img_name,
                    image_location="G:/11.GitHubRepositories/faceRecognition/static/img/upload_img/",
                    image_size=file_size,
                    image_charset=file_charset,
                    is_handle=1,
                    create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    is_delete=False,
                )
                upload_image_info.save()

            models_faces_path1 = "G:/11.GitHubRepositories/faceRecognition/static/img/type_2/men"
            models_faces_path2 = "G:/11.GitHubRepositories/faceRecognition/static/img/type_2/women"

            face_dict = {}

            # 循环遍历路径下的人脸  获取人脸名称和人脸数据

            # print(os.listdir(models_faces_path))

            for file in os.listdir(models_faces_path1):
                # 加载图片
                load_img = face_recognition.load_image_file(models_faces_path1 + "/" + file)

                # 获取人脸数据
                face_encode = face_recognition.face_encodings(load_img)[0]

                # 截取图片名（这里应该把images文件中的图片名命名为为人物名）
                file_name = file[:(len(file) - 4)]

                face_dict[f'{file_name}'] = face_encode
                face_dict.update()

            for file in os.listdir(models_faces_path2):
                # 加载图片
                load_img = face_recognition.load_image_file(models_faces_path2 + "/" + file)

                # 获取人脸数据
                face_encode = face_recognition.face_encodings(load_img)[0]

                # 截取图片名（这里应该把images文件中的图片名命名为为人物名）
                file_name = file[:(len(file) - 4)]

                face_dict[f'{file_name}'] = face_encode
                face_dict.update()

            unknown_image = UploadImage.objects.get(image_name=img_name)
            unknown_image = face_recognition.load_image_file(unknown_image.image_location + img_name)

            try:
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                for i in face_dict:
                    results = face_recognition.compare_faces([face_dict[i]], unknown_encoding, tolerance=0.4)
                    if str(results[0]) == "True":
                        star_info = StarBasicInfo.objects.get(star_name=i)
                        star_desc = star_info.stardesc.desc
                        image = StarImage.objects.filter(image_name=i).filter(image_type=2)
                        image_location = image[0].image_location
                        return render(request, "search_results.html", {"star_info": star_info,
                                                                       "star_desc": star_desc,
                                                                       "image_loaction": image_location,
                                                                       })
                return render(request, "404.html")
            except IndexError as e:
                return HttpResponse("上传图片有误！")


def add(request):
    star_basic_info = StarBasicInfo(
        star_name="杨坤3号",
        star_sex="男",
        star_birth=datetime.date(1997, 10, 10),
        star_weight=80,
        star_height=197,
        star_career="演员",
        star_nationality="中国",
        star_constellation="人马座",
        star_graduated_school="黄河科技学院",
        star_economic_company="星鉴有限公司",
        star_representative="《死了都要爱》",
        star_major_achievements="中国内地最佳男歌手",
        create_time=datetime.datetime.strptime('2018-11-16 18:20:20', '%Y-%m-%d %H:%M:%S'),
        is_delete=False,
    )
    star_basic_info.save()

    star_desc = StarDesc(
        desc="杨坤，1972年12月18日生于内蒙古自治区包头市，中国内地流行乐男歌手、影视演员、音乐制作人。1994年，为电视剧《陌生的海岸》演唱主题曲《陌生海岸》，从而正式进入演艺圈。1997年，杨坤录制完成个人原创专辑《无所谓》，但却被唱片公司反复退回。1999年，为范琳琳、耿宁、刘俊等歌手创作了《往日难追》、《想念你》等歌曲。2002年，推出首张个人音乐专辑《无所谓》 。2003年，获得“第十届中国歌曲排行榜颁奖典礼”年度最受欢迎新人奖  。2004年，获得“第11届东方风云榜颁奖典礼”最受欢迎男歌手奖 。2004年，参加中央电视台春节联欢晚会，并演唱歌曲《天下父母心》 ；同年，出演个人首部电影《十三月》 。2005年，推出第三张个人音乐专辑《2008》。2007年，推出第四张个人音乐专辑《牧马人》 。2009年，推出第五张个人音乐专辑《杨坤》。2010年，推出第六张个人音乐专辑《DISCO》；同年，获得“第八届东南劲爆音乐榜颁奖礼”内地最佳男歌手奖 。2011年，主演剧情电影《密室2之不可靠岸》。2012年，推出第七张个人音乐专辑《真的很在乎》；同年，担任浙江卫视歌唱选秀节目《中国好声音》的导师。2013年，参加中央电视台春节联欢晚会 。2014年，推出第八张个人音乐专辑《今夜二十岁》。2016年，担任东方卫视原创音乐挑战节目《天籁之战》的导师。2017年，推出第9张个人音乐专辑《孤独颂》。2019年，作为首发阵容参加湖南卫视音乐竞技节目《歌手2019》，最终取得了总决赛4强的成绩。",
        create_time=datetime.datetime.strptime('2018-11-16 18:20:20', '%Y-%m-%d %H:%M:%S'),
        is_delete=False,
        star_id=star_basic_info.star_id
    )
    star_desc.save()
    return HttpResponse("添加数据")
