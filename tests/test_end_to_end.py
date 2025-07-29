# tests/test_end_to_end.py

import pytest
from gmail_client.src.gmail_client import GmailClient
from gmail_client.src.interface import Message

@pytest.fixture(scope="module")
def gmail_client() -> GmailClient:
    return GmailClient()

def test_full_email_flow(gmail_client: GmailClient) -> None:
    subject = "E2E Flow Test"
    body = "This message tests the full E2E flow."

    # Send the message
    sent = gmail_client.send_message(
        to="your_email@gmail.com",  # Replace with your email
        subject=subject,
        body=body,
        attachments=None,
    )
    assert sent is True

    # Fetch message
    messages = list(gmail_client.get_messages())
    assert len(messages) > 0
    message = next((m for m in messages if subject in m.subject), None)
    assert message is not None

    # Mark as read
    read_result = gmail_client.mark_as_read(message.id)
    assert read_result is True

    # Delete the message
    deleted = gmail_client.delete_message(message.id)
    assert deleted is True
