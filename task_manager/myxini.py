from django.contrib.auth.mixins import UserPassesTestMixin



class PermissionCheckMixin(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user == self.get_object()