import pytest
from gmail_client.gmail_client import GmailClient
from gmail_client.interface import Message

@pytest.fixture(scope="module")
def gmail_client() -> GmailClient:
    return GmailClient()

def test_send_email_real(gmail_client: GmailClient) -> None:
    success = gmail_client.send_message(
        to="your_email@gmail.com",  # ← Replace this with your test email
        subject="Test Subject from Pytest",
        body="This is a test message sent by GmailClient tests.",
        attachments=None,
    )
    assert success is True

def test_get_messages(gmail_client: GmailClient) -> None:
    messages = list(gmail_client.get_messages())
    assert isinstance(messages, list)
    if messages:
        assert isinstance(messages[0], Message)

def test_get_single_message(gmail_client: GmailClient) -> None:
    messages = list(gmail_client.get_messages())
    if not messages:
        pytest.skip("No messages in inbox to test retrieval by ID.")
    message = gmail_client.get_message(messages[0].id)
    assert message is not None
    assert message.id == messages[0].id

def test_delete_message(gmail_client: GmailClient) -> None:
    messages = list(gmail_client.get_messages())
    if not messages:
        pytest.skip("No messages to delete.")
    result = gmail_client.delete_message(messages[0].id)
    assert result is True

def test_mark_as_read(gmail_client: GmailClient) -> None:
    messages = list(gmail_client.get_messages())
    if not messages:
        pytest.skip("No messages to mark as read.")
    success = gmail_client.mark_as_read(messages[0].id)
    assert success is True
