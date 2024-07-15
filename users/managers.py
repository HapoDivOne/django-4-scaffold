from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(
            self,
            username: str,
            password: str,
        ):
            user = self.model(
                username=username, password=password,
            )
            user.password = make_password(password)
            user.save(using=self._db)
            return user

    def create_user(
        self,
        username: str,
        password: str,
    ):
        return self._create_user(username, password)
