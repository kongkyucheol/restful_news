import requests

from ServiceSource import ServiceSource, ServiceData


class OpenNewsSource(ServiceSource):
    def request(self):
        url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-08-02&sortBy=publishedAt&apiKey"
               "=3a48b12063b0415f9359490b7907ab46")
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
            # print(serviceData.__str__())
            serviceDatas.append(serviceData)
        return serviceDatas
