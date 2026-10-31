from .message import Message


class MessageDecorator(Message):
    def __init__(self, message: Message):
        self._message = message

    def render(self) -> str:
        return self._message.render()