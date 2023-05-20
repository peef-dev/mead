from flask import render_template
from flask.views import View


class BaseView(View):
    def __init__(self, template=None, model=None):
        if template is not None:
            self.template = template
        if model is not None:
            self.model = model


class FormView(BaseView):
    methods = ["GET", "POST"]

    def __init__(self, template, model):
        super().__init__(template, model)


class DetailView(BaseView):
    
    def __init__(self, template, model=None):
        super().__init__(template, model=None)

class ActionView(BaseView):

    def __init__(self, redirect_url, template=None):
        super().__init__(template=None, model=None)
        self.redirect_url = redirect_url
        self.template = template


class MenuItem:
    def __init__(self):
        """
        menus = [
            {
                name: 'Produits',
                icon: 'fa-star',
                items: [
                    {
                        'name': 'Peintures',
                        'link': 'www.menu.penture',
                        'icon': 'fa-star',
                    },
                    {
                        'name': 'Ordinateurs',
                        'link': 'www.menu.ordi',
                        'icon': 'fa-star'
                    }
                ]
            },
            {
                name: 'Produits',
                icon: 'fa-star',
                items: [
                    {
                        'name': 'Peintures',
                        'link': 'www.menu.penture',
                        'icon': 'fa-star',
                    },
                    {
                        'name': 'Ordinateurs',
                        'link': 'www.menu.ordi',
                        'icon': 'fa-star'
                    }
                ]
            },
        ]
        """
        menu_items = []