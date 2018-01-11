from django.shortcuts import render
from myDjango.models import Info
# 引入分页
from django.core.paginator import Paginator
# Create your views here.
def data_gen(area):
    pipeline=[
        {'$match':{'area':{'$regex':area}}},
        {'$group':{'_id':'$brand','counts':{'$sum':1}}},
        {'$sort':{'counts':1}}
    ]
    for i in Info._get_collection().aggregate(pipeline):
        # data={
        #     'name':i['_id'],
        #     'data':[i['counts']],
        #     'type':'colum'
        # }
        # yield data
        yield [i['_id'],i['counts']]
series_sh=[i for i in data_gen("上海")]
series_bj=[i for i in data_gen("北京")]
series_gz= [i for i in data_gen("广州")]

area_sh=[]
area_bj=[]
area_ah=[]
area_hl=[]
area_js=[]
area_gx=[]
area_fj=[]
area_tj=[]
area_gd=[]
area_zj=[]
def dq_data():
    content = Info._get_collection().find({"area": {'$regex': '北京'}})
    for i in content:
        area_bj.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '上海'}})
    for i in content:
        area_sh.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '江苏'}})
    for i in content:
        area_js.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '河南'}})
    for i in content:
        area_hl.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '广西'}})
    for i in content:
        area_gx.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '福建'}})
    for i in content:
        area_fj.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '天津'}})
    for i in content:
        area_tj.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '广东'}})
    for i in content:
        area_gd.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '浙江'}})
    for i in content:
        area_zj.append(i['area'])
    content = Info._get_collection().find({"area": {'$regex': '安徽'}})
    for i in content:
        area_ah.append(i['area'])

bd_bm=[]
bd_ad=[]
bd_bt=[]
bd_xfl=[]
bd_dz=[]
bd_ft=[]
bd_stn=[]
bd_lbjn=[]
bd_bc=[]
bd_ft=[]
def bd_data():
    content = Info._get_collection().find({"brand": {'$regex': '宝马'}})
    for i in content:
        bd_bm.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '奥迪'}})
    for i in content:
        bd_ad.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '本田'}})
    for i in content:
        bd_bt.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '雪佛兰'}})
    for i in content:
        bd_xfl.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '大众'}})
    for i in content:
        bd_dz.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '丰田'}})
    for i in content:
        area_fj.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '桑塔纳'}})
    for i in content:
        bd_stn.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '兰博基尼'}})
    for i in content:
        bd_lbjn.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '奔驰'}})
    for i in content:
        bd_bc.append(i['brand'])
    content = Info._get_collection().find({"brand": {'$regex': '福特'}})
    for i in content:
        bd_ft.append(i['brand'])

def index(requests):
    info=Info.objects[:1]
    limit=20
    paginator=Paginator(info,limit)
    # 得到页码
    page=requests.GET.get('page',1)
    loaded=paginator.page(page)
    context={
        'Info':loaded
    }
    return render(requests,'index.html',context)

def chart(requests):
    context={
        'chart_sh':series_sh,

        'chart_gz':series_gz
    }
    return render(requests,'chart.html',context)

def bj_chart(requests):
    context={
        'chart_bj': series_bj
    }
    return render(requests,'bj.html',context)

def gz_chart(requests):
    context={
        'chart_gz': series_gz
    }
    return render(requests,'gz.html',context)

def chart_dq(requests):
    dq_data()
    series=[['上海',len(area_sh)],['北京',len(area_bj)],['安徽',len(area_ah)],['江苏',len(area_js)],['福建',len(area_fj)],['天津',len(area_tj)],['广东',len(area_gd)],['浙江',len(area_zj)]]
    # series=[['123',123],['234',234],['345',345]]
    context={
        'chart_data':series
    }
    return render(requests,'chart_diqu.html',context)

def chart_pp(requests):
    bd_data()
    series=[['宝马',len(bd_bm)],['奥迪',len(bd_ad)],['本田',len(bd_bt)],['雪佛兰',len(bd_xfl)],['大众',len(bd_dz)],['丰田',len(bd_ft)],['桑塔纳',len(bd_stn)],['兰博基尼',len(bd_lbjn)],['奔驰',len(bd_bc)],['福特',len(bd_ft)]]
    context={
        'char_bd':series
    }
    return render(requests,'chart_bd.html',context)