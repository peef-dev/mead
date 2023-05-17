import uuid

from werkzeug.security import generate_password_hash

from application.models import Role, User


class RoleService:
    def __init__(self, session):
        self.session = session

    def get_all_roles(self):
        return self.session.query(Role).all()

    def get_role_by_id(self, role_id):
        return Role.query.get(role_id)

    def create_role(self, name, description):
        role = Role()
        role.name = name
        role.description = description
        self.session.add(role)
        self.session.commit()
        return role

    def create_first_roles(self):
        first_roles = [("admin", "Administrator"), ("user", "User")]
        for role in first_roles:
            self.create_role(name=role[0], description=role[1])


class UserService:
    def __init__(self, session):
        self.session = session

    def get_id(self):
        return User.id

    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def generate_identifier(self):
        return str(uuid.uuid4())

    def create_user(self, name, email, password, role_id):
        user = User()
        user.name = name
        user.password = generate_password_hash(password)
        user.email = email
        user.role_id = role_id
        self.session.add(user)
        self.session.flush()
        identifier = self.generate_identifier()
        id = user.id
        user.identifier = f"{identifier}-{id}"
        self.session.commit()
        return user.id

    def update_user(self, user_id, email=None, password=None, role_id=None):
        user = self.get_user_by_id(user_id)
        if not user:
            return None

        if email:
            user.email = email
        if password:
            user.password = generate_password_hash(password)
        if role_id:
            user.role_id = role_id

        self.session.commit()
        return user.id

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if not user:
            return False

        self.session.delete(user)
        self.session.commit()
        return True

    def get_user_role(self, name):
        return self.session.query(Role).filter_by(name=name).first()

    def get_user_by_email(self, email):
        return self.session.query(User).filter_by(email=email).first()

    def user_email_exist(self, email):
        """check if an email exist or not."""
        user_email_count = User.query.filter(User.email == email).count()
        return False if user_email_count == 0 else True
