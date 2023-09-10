from datetime import datetime, timedelta

import requests
from ServiceSource import ServiceSource, ServiceData


class OpenNewsSource(ServiceSource):
    def request(self):
        yesterday = datetime.today() - timedelta(3)
        url = ("https://newsapi.org/v2/everything?q=tesla&from="+yesterday.strftime("%Y-%m-%d")+"&sortBy=publishedAt&apiKey"
               "=3a48b12063b0415f9359490b7907ab46")
        print(url)
        response = requests.get(url)
        articles = response.json()['articles']
        serviceDatas = []
        for article in articles:
            serviceData = ServiceData()
            serviceData.title = article["title"]
            serviceData.fromSource = "OPEN NEWS"
            serviceData.httpUri = article["url"]
            serviceData.thumbnailUri = article["urlToImage"]
            serviceData.datetime = article["publishedAt"]
            serviceData.description = article["description"]
            serviceDatas.append(serviceData)
        return serviceDatas
