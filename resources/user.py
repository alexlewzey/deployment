from flask_restful import reqparse, Resource

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username required')
    parser.add_argument('password', type=str, required=True, help='password required')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'this user already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user created'}, 201
