# tests/test_integration.py

import pytest
from gmail_client.src.gmail_client import GmailClient
from gmail_client.src.interface import Message

@pytest.fixture(scope="module")
def gmail_client() -> GmailClient:
    return GmailClient()

def test_send_and_fetch_message(gmail_client: GmailClient) -> None:
    # Send a test message
    success = gmail_client.send_message(
        to="your_email@gmail.com",  # Replace with your email
        subject="Integration Test",
        body="This is a test for send and fetch integration.",
        attachments=None,
    )
    assert success is True

    # Fetch the most recent message
    messages = list(gmail_client.get_messages())
    assert len(messages) > 0
    latest = messages[0]
    assert isinstance(latest, Message)
    assert "Integration Test" in latest.subject or latest.body

def test_send_and_delete_message(gmail_client: GmailClient) -> None:
    success = gmail_client.send_message(
        to="your_email@gmail.com",  # Replace with your email
        subject="Delete Me",
        body="This message should be deleted by the test.",
        attachments=None,
    )
    assert success is True

    messages = list(gmail_client.get_messages())
    msg_to_delete = next((m for m in messages if "Delete Me" in m.subject), None)
    assert msg_to_delete is not None

    delete_result = gmail_client.delete_message(msg_to_delete.id)
    assert delete_result is True
