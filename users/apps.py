from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    #signal to create profile when user created
    def ready(self):
        import users.signals
