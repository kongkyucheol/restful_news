from ServiceSource import ServiceSource, ServiceData
import requests
import feedparser
import xml.etree.ElementTree as elemTree


class FeedNewsSource(ServiceSource):

    def __init__(self, url):
        self.url = url

    def request(self):
        response = requests.get(self.url)
        parsedData = elemTree.fromstring(response.text)
        # print(response.text)
        entries = parsedData.find('./channel').findall('./item')
        source = parsedData.find('./channel').find('./title').text
        serviceDatas = []
        print(len(entries))
        for p in entries:
            serviceData = ServiceData()
            serviceData.title = p.find('./title').text
            serviceData.fromSource = source
            serviceData.httpUri = p.find('./link').text
            image = p.find('./image')
            if image is not None:
                serviceData.thumbnailUri = image.text
            else:
                continue
            serviceData.datetime = p.find('./pubDate').text
            serviceData.description = serviceData.title
            serviceDatas.append(serviceData)
        return serviceDatas
