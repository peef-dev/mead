from flask import render_template
from flask.views import MethodView

# @index_bp.route("/")
# def index():
#     return render_template("index/home.html")


class BaseView(MethodView):
    def __init__(self, template=None):
        if template is not None:
            self.template = template

    def get_template(self):
        return self.template


class IndexView(BaseView):
    def __init__(self, template):
        super().__init__(template)

    def get(self):
        template = self.get_template()
        return render_template(template)
