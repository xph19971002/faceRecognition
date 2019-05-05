import datetime

from django.http import HttpResponse
from django.shortcuts import render

from apps.main.models import StarBasicInfo, StarDesc


def result(request):
    return render(request, "search_results.html")



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
