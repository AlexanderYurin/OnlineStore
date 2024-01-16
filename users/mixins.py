from django.contrib import messages
from django.urls import reverse


class MessagesMixin:
    success_url: str
    messages: str

    def get_success_url(self):

        messages.success(self.request, f"{self.request.user}, {self.messages}!"
                         if self.request.user.id else f"{self.messages}!")
        return reverse(self.success_url)
