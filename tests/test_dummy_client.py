from gmail_client.interface import Client, Message, Attachment
from typing import Iterator, Optional


class DummyMessage(Message):
    def __init__(self):
        self._id = "1"
        self._from = "sender@example.com"
        self._to = "receiver@example.com"
        self._subject = "Test Subject"
        self._body = "Test body"
        self._date = "2023-01-01"

    @property
    def id(self) -> str: return self._id
    @property
    def from_(self) -> str: return self._from
    @property
    def to(self) -> str: return self._to
    @property
    def subject(self) -> str: return self._subject
    @property
    def body(self) -> str: return self._body
    @property
    def date(self) -> str: return self._date


class DummyClient(Client):
    def get_messages(self) -> Iterator[Message]:
        yield DummyMessage()

    def get_message(self, message_id: str) -> Optional[Message]:
        return DummyMessage() if message_id == "1" else None

    def send_message(
        self, to: str, subject: str, body: str, attachments: Optional[list[Attachment]] = None
    ) -> bool:
        return True

    def delete_message(self, message_id: str) -> bool:
        return message_id == "1"


def test_send_email():
    client = DummyClient()
    assert client.send_message("a@b.com", "Hi", "Hello") is True


def test_read_email():
    client = DummyClient()
    msg = client.get_message("1")
    assert msg is not None
    assert msg.subject == "Test Subject"


def test_delete_email_success():
    client = DummyClient()
    assert client.delete_message("1") is True


def test_delete_email_failure():
    client = DummyClient()
    assert client.delete_message("999") is False
