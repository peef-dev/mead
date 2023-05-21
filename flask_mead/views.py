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


class Menu:
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

    def __init__(self, categories=None, element_id=None):
        self.categories = categories or []
        self.items = []
        self.element_id = element_id

    def add_category(self, category):
        self.categories.append(category)

    def __iter__(self):
        return iter(self.items)

    def build(self):
        for category in self.categories:
            menu_item = {
                "name": category.name,
                "icon": category.icon,
                "items_menu": [
                    {
                        "name": menu.name,
                        "link": menu.link,
                        "icon": menu.icon,
                    }
                    for menu in category
                ],
            }
            self.items.append(menu_item)
        return self.items


class MenuCategory:
    def __init__(self, name, menu_items, icon=None, css_class=None, element_id=None):
        self.name = name
        self.icon = icon
        self.css_class = css_class
        self.menu_items = menu_items
        self.element_id = element_id

    def __iter__(self):
        return iter(self.menu_items)

    def add_item(self, item):
        self.menu_items.append(item)


class MenuItem:
    def __init__(self, name, link, icon=None, css_class=None, element_id=None):
        self.name = name
        self.link = link
        self.icon = icon
        self.css_class = css_class
        self.element_id = element_id

    def __repr__(self):
        rep = f"MenuItem(name={self.name}, link={self.link})"
        return rep
