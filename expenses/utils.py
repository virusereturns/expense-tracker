from django.utils import timezone


def get_local_today():
    """
    Returns today's date adjusted to the server's local timezone (TIME_ZONE setting).
    """
    return timezone.localtime(timezone.now()).date()
