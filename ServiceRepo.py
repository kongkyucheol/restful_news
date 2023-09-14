from flask import jsonify

from source.FeedNewsSource import FeedNewsSource
from source.OpenNewsSource import OpenNewsSource


class ServiceRepo:
    serviceList = []
    serviceSource = OpenNewsSource()
    mkFeedList = []
    mkFeedSource = FeedNewsSource("https://www.hankyung.com/feed/all-news")
    mkFeedFinacneList = []
    mkFeedFinanceSource = FeedNewsSource("https://www.hankyung.com/feed/finance")


    def getNewsJson(self, maxCount, keyList):
        result = []
        for service in self.serviceList:
            serviceJson = {'http': service.httpUri,
                           'thumbnail': service.thumbnailUri,
                           'title': service.title,
                           'description': service.description,
                           'datetime': service.datetime,
                           'fromSource': service.fromSource}
            result.append(serviceJson)
        return jsonify(result)

    def getMKAll(self, count):
        result = []
        for service in self.mkFeedList:
            serviceJson = {'http': service.httpUri,
                           'thumbnail': service.thumbnailUri,
                           'title': service.title,
                           'description': service.description,
                           'datetime': service.datetime,
                           'fromSource': service.fromSource}
            result.append(serviceJson)
        return jsonify(result)

    def getMKFinance(self, count):
        result = []
        for service in self.mkFeedFinacneList:
            serviceJson = {'http': service.httpUri,
                           'thumbnail': service.thumbnailUri,
                           'title': service.title,
                           'description': service.description,
                           'datetime': service.datetime,
                           'fromSource': service.fromSource}
            result.append(serviceJson)
        return jsonify(result)

    def getNews(self, url):
        result = []
        feedNewsList = FeedNewsSource(url).request()
        for service in feedNewsList:
            serviceJson = {'http': service.httpUri,
                           'thumbnail': service.thumbnailUri,
                           'title': service.title,
                           'description': service.description,
                           'datetime': service.datetime,
                           'fromSource': service.fromSource}
            result.append(serviceJson)
        return jsonify(result)

    def ready(self):
        print("ready")
        self.update()

    def update(self):
        print("update")
        self.serviceList = self.serviceSource.request()
        self.mkFeedList = self.mkFeedSource.request()
        self.mkFeedFinacneList = self.mkFeedFinanceSource.request()
