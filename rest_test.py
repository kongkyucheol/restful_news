

from flask import Flask, request
from flask_restx import Resource, Api
from requests import get

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

# SITE_NAME = 'https://google.com/'
#
# todos = {}
# count = 1
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def proxy(path):
#   return get(f'{SITE_NAME}{path}').content

#curl -X POST -H "User-Agent:linux" -H "Content-Type:application/json" -d "{\"data\":\"study\"}" 127.0.0.1:5000/todos
@api.route('/todos')
class TodoPost(Resource):
    def post(self):
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {
            'todo_id': idx,
            'data': todos[idx]
        }


@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def delete(self, todo_id):
        del todos[todo_id]
        return {
            "delete": "success"
        }

if __name__ == '__main__':
    app.run(debug=True)