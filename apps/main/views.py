from django.http import HttpResponse
from django.shortcuts import render
from apps.main.models import Banner, StarBasicInfo


def index(request):
    banners = Banner.objects.all()

    man_stars = StarBasicInfo.objects.filter(star_sex="男")[0:4]

    for man_star in man_stars:
        image_list = man_star.image_set.filter(image_type=1)
        man_star.image = image_list[0]

    woman_stars = StarBasicInfo.objects.filter(star_sex="女")[0:4]

    for woman_star in woman_stars:
        image_list = woman_star.image_set.filter(image_type=1)
        woman_star.image = image_list[0]

    return render(request, "index.html", context={
        "banners": banners,
        "man_stars": man_stars,
        "woman_stars": woman_stars,
    })
