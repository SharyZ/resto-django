from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password):
        user = self.model(first_name=first_name,
                          last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(first_name=first_name, last_name=last_name,
                                username=username, email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
