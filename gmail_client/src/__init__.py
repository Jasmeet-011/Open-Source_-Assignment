# gmail_client/__init__.py

from .factories import get_gmail_client, create_gmail_attachment
from .gmail_client import GmailClient
from .gmail_message import GmailMessage
from .gmail_attachment import GmailAttachment
from .interface import Client, Message, Attachment

__all__ = [
    "GmailClient",
    "GmailMessage",
    "GmailAttachment",
    "get_gmail_client",
    "create_gmail_attachment",
    "Client",
    "Message",
    "Attachment",
]
