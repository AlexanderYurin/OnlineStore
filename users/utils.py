from django.http import HttpRequest


def get_session_key(request: HttpRequest) -> str:
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key
