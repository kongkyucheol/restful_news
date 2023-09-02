from flask import jsonify

from source.OpenNewsSource import OpenNewsSource


class ServiceRepo:
    serviceList = []
    serviceSource = OpenNewsSource()

    def getNewsJson(self, count):
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

    def ready(self):
        print("ready")
        self.update()

    def update(self):
        print("update")
        self.serviceList = self.serviceSource.request()
