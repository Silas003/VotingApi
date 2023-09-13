from rest_framework.permissions import BasePermission
from datetime import datetime,timedelta


class TimeLimitPermission(BasePermission):
    def has_permission(self, request, view):
        expires = datetime.now() + timedelta(seconds=60)
        return datetime.now() < expires