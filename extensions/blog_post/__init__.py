from flask import jsonify, request
from flask_jwt_extended import jwt_required


class BlogExtension:
    def __init__(self, app=None):
        self.app = app
        self.service = BlogService()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.register_routes(app)

    def register_routes(self, app):
        app.add_url_rule('/posts', 'get_posts', self.get_posts, methods=['GET'])
        app.add_url_rule('/posts', 'create_post',
                         jwt_required(self.create_post), methods=['POST'])
        app.add_url_rule('/posts/<int:post_id>', 'get_post', self.get_post,
                         methods=['GET'])
        app.add_url_rule('/posts/<int:post_id>', 'update_post',
                         jwt_required(self.update_post), methods=['PUT'])
        app.add_url_rule('/posts/<int:post_id>', 'delete_post',
                         jwt_required(self.delete_post), methods=['DELETE'])

    def get_posts(self):
        posts = self.service.get_all_posts()
        return jsonify(posts)

    def create_post(self):
        data = request.get_json()
        post = self.service.create_post(data)
        return jsonify(post)
