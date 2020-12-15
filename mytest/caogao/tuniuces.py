import json
from urllib import parse
import requests

proxies = {
    'http': 'http://127.0.0.1:1909',
    'https': 'http://127.0.0.1:1909'
}
# result = {'c1': c1_title,
#           'c2': c2_title,
#           'c3': c3_title,
#           'search_type': search_type,
#           'catId': classification_id,
#           'cc': tagId,
#           'url': openUrl}
destination_city = {'c1': '欧粥',
                    'c2': None,
                    'c3': '丽江',
                    'search_type': '2',
                    'catId': '923',
                    'cc': '3312',
                    'url': "tuniuapp://page?iosPageName=TNSearchResultViewController&androidPageName=com.tuniu.app.ui.search.global.GlobalSearchResultActivity¶meters=%7B%22keyword%22%3A%22%E4%B8%BD%E6%B1%9F%22%2C%22search_type%22%3A2%2C%22classification_id%22%3A923%2C%22product_type%22%3A0%2C%22play_route_type_id%22%3A%5B%22%22%5D%7D",
                    }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
}
origin_city = {'city': '北京', 'cc': '200', 'catId': '0'}

url = "https://api.tuniu.com/batch/search/list?c=%7B%22v%22%3A%2210.6.0%22%2C%22ct%22%3A20%2C%22dt%22%3A1%2C%22ov%22%3A20%2C%22p%22%3A10716%2C%22cc%22%3A" + origin_city.get(
    "cc") + "%7D"
search_type = destination_city.get("search_type")
catId = destination_city.get("catId")
c3 = destination_city.get("c3")
cc = destination_city.get("cc")


def tuniu_search_list():
    data = {
        "keyword": str(c3),
        "page": 1,
        "limit": 1,
        # "poiId": str(cc),
        "searchType": str(search_type),
        "productType": 0,
        "catId": str(catId)
    }
    # {"catId":923,"customMode":0,"displayType":0,"gpPlan":"没有GP率","height":0,"isDirectSearch":false,"isShowDot":false,"keyword":"丽江","lastKey":"","lat":"39.932636","limit":15,"lng":"116.458904","locateCityCode":200,"maxHour":0,"maxPrice":-1,"minHour":0,"minPrice":0,"originalKeyword":"丽江","page":1,"poiId":0,"policyJsonStr":"{\"45\":\"无转化率\",\"50\":\"无签约率\",\"53\":\"无销量指数\",\"57\":\"无GP转化因子\",\"61\":\"无满意度\"}","productType":1,"recommendPlan":"通用","searchType":2,"tabId":0,"tact":"861322030527903","tagName":"","title":"","useSpecialType":0,"width":0}
    data = {
        "catId": 923,
        "keyword": "丽江",
        "limit": 300,
        "locateCityCode": 200,
        "page": 1,
        "searchType": 2,
        "productType": 1,
        "poiId": '3312'
    }

    # data = {
    #     "catId": 923,
    #     # "customMode": 0,
    #     # "displayType": 0,
    #     # "gpPlan": "没有GP率",
    #     # "height": 0,
    #     # "isDirectSearch": False,
    #     # "isShowDot": False,
    #     "keyword": "丽江",
    #     # "lastKey": "",
    #     # "lat": "39.932636",
    #     "limit": 100,
    #     # "lng": "116.458904",
    #     "locateCityCode": 200,
    #     # "maxHour": 0,
    #     # "maxPrice": -1,
    #     # "minHour": 0,
    #     # "minPrice": 0,
    #     # "originalKeyword": "丽江",
    #     "page": 1,
    #     # "poiId": 0,
    #     # "policyJsonStr": "{\"45\":\"无转化率\",\"50\":\"无签约率\",\"53\":\"无销量指数\",\"57\":\"无GP转化因子\",\"61\":\"无满意度\"}",
    #     "productType": 1,
    #     # "recommendPlan": "通用",
    #     "searchType": 2,
    #     # "tabId": 0,
    #     # "tact": "861322030527903",
    #     # "tagName": "",
    #     # "title": "",
    #     # "useSpecialType": 0,
    #     # "width": 0
    # }

    # url = 'https://api.tuniu.com/batch/search/list?c={"cc":619,"ct":20,"dt":1,"ov":20,"p":10716,"v":"10.34.0"}'
    url = 'https://api.tuniu.com/batch/search/list?c={"cc":619,"ct":20,"dt":1,"ov":20,"p":10716,"v":"10.34.0"}'
    # {"catId":923,"customMode":0,"displayType":0,"gpPlan":"没有GP率","height":0,"isDirectSearch":true,"isShowDot":false,"keyword":"丽江","lastKey":"","lat":"39.932636","limit":15,"lng":"116.458904","locateCityCode":200,"maxHour":0,"maxPrice":-1,"minHour":0,"minPrice":0,"originalKeyword":"丽江","page":1,"poiId":0,"policyJsonStr":"{\"46\":\"无转化率\",\"49\":\"无签约率\",\"54\":\"无销量指数\",\"58\":\"无GP转化因子\",\"62\":\"无满意度\"}","productType":0,"recommendPlan":"通用","searchKey":[{"fieldKey":"play_route_type_id","fieldName":"play_route_type_id","searchIds":[""]}],"searchType":2,"tabId":0,"tact":"861322030527903","tagName":"","title":"","useSpecialType":0,"width":0}
    res = requests.post(url=url,
                        json=data,
                        headers=headers,
                        verify=False,
                        # proxies=proxies,
                        timeout=10)
    res_json = res.json()
    print(res_json)

    # openUrl = "tuniuapp://page?iosPageName=TNSearchResultViewController&androidPageName=com.tuniu.app.ui.search.global.GlobalSearchResultActivity¶meters=%7B%22keyword%22%3A%22%E4%B8%B9%E9%BA%A6%22%2C%22search_type%22%3A2%2C%22classification_id%22%3A858%2C%22product_type%22%3A0%2C%22play_route_type_id%22%3A%5B%22%22%5D%7D"
    # openUrl="tuniuapp://page?iosPageName=TNSearchResultViewController&androidPageName=com.tuniu.app.ui.search.global.GlobalSearchResultActivity¶meters=%7B%22keyword%22%3A%22%E4%B8%BD%E6%B1%9F%22%2C%22search_type%22%3A2%2C%22classification_id%22%3A923%2C%22product_type%22%3A0%2C%22play_route_type_id%22%3A%5B%22%22%5D%7D"
    # values = json.loads(parse.unquote(openUrl).split('=')[-1])
    # print(values)
    # 'totalCount': 721, 'pageCount': 49
    # {'productType': 240, 'order': 16, 'productTypeName': '专业顾问', 'productCount': 179, 'pageCount': 1, 'selected': False}


def tuniu_product_list():
    cate = {
        # 'productType': "240",
        'productType': "96",
        'productTypeName': '专业顾问',
        'productCount': 179,
    }
    url = 'https://api.tuniu.com/batch/search/list?c={"v":"10.34.0","ct":20,"dt":1,"ov":20,"p":10716,"cc":' + origin_city.get(
        "cc") + '}'
    search_type = destination_city.get("search_type")
    cc = origin_city.get("cc")
    if search_type == 3:
        poiId = destination_city.get("cc"),
        catId = 0
    else:
        poiId = 0
        catId = destination_city.get("catId")
    data = {
        "keyword": str(destination_city.get("c3")),
        "page": 1,
        "searchKey": [{"fieldName": "depart_cities", "searchIds": [str(cc)]}],
        "poiId": str(poiId),
        "productType": str(cate.get("productType")),
        "limit": 200,
        "searchType": str(search_type),
        "catId": str(catId)
    }
    print('eachCityCat', data)
    res = requests.post(url=url,
                        json=data,
                        headers=headers,
                        verify=False,
                        # proxies=TuniuTravelProduct.proxies,
                        timeout=10)
    res_json = res.json()
    print(res_json)


if __name__ == '__main__':
    # tuniu_product_list()
    productTypeName = '专业顾问'
    if productTypeName not in {'机票', '酒店', '产品推荐', '专业顾问'}:
        print(1)

