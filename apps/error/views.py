import datetime
import os
import face_recognition
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.main.models import UploadImage, StarBasicInfo, StarImage


@csrf_exempt
def error(request):
    if request.method == "GET":
        return render(request, "404.html")
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
            except IndexError:
                return HttpResponse("上传图片有误！")
