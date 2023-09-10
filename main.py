from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api
from flask import make_response

from AdminRepo import AdminRepo
from ServiceRepo import ServiceRepo

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app)
api = Api(app)  # Flask 객체에 Api 객체 등록


# NEWS
# curl -X POST -H "User-Agent:linux" -H "Content-Type:application/json" -d "{\"max_count\":\"3\"}" 127.0.0.1:5000/api/service/news/request
# curl -X GET "127.0.0.1:5000/api/others"

#ADMIN
# curl -X POST -H "User-Agent:linux" -H "Content-Type:application/json" -d "{\"max_count\":\"3\"}" 127.0.0.1:5000/api/service/news/request
# curl -X GET "127.0.0.1:5000/admin"

serviceRepo = ServiceRepo()
serviceRepo.ready()
adminRepo = AdminRepo()


@api.route('/api/service/news/request')
class NewsServer(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self):
        maxCount = request.json.get("max_count")
        idList = request.json.get("provider_id_list")
        # self.serviceRepo.update()
        return make_response(serviceRepo.getNewsJson(maxCount), 200)

@api.route('/api/others')
class NewsServer(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        return make_response(serviceRepo.getOtherJson(10), 200)
# Admin
@api.route('/admin')
class AdminServer(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def post(self):
        print(request.json)
        adminRepo.post(request.json)
        return make_response(adminRepo.get(), 200)


    def get(self):
        return make_response(adminRepo.get(), 200)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
