# Gmail Client Component

## Concept of a Component

In this repository, a component is a modular unit encapsulating specific functionality. Each component is isolated in its own folder with implementation, interface, and data models. All tests reside in a separate tests/ directory to preserve a clean separation between logic and validation.

The Gmail Client component is responsible for sending emails, retrieving inbox messages, managing message deletion and read-status, and handling attachments. It implements a standardized Client interface, enabling integration with Gmail or a mock backend using dependency injection.

---

### Directory Structure

gmail_client/
│ ├── **init**.py # Public exports and interface registration
│ ├── gmail_client.py # GmailClient implementation of the Client interface
│ ├── gmail_message.py # GmailMessage implementation of Message interface
│ ├── gmail_attachment.py # GmailAttachment implementation of Attachment interface
│ └── factories.py # Factory to return get_gmail_client()

mail_client/
│ └── interface.py # Protocols for Client, Message, and Attachment

tests/
│ ├── dummy_client.py # Dummy implementation of Client for safe testing
│ └── test_dummy_client.py # Unit tests for DummyClient

Each component follows a structure where:

- **Implementation files** (gmail_client/\*.py): Gmail-specific logic.

- **Interface file** (mail_client/interface.py): Abstract interfaces for the client, message, and attachment.

- **Test files** (tests/\*.py): Dummy client and test cases using pytest.

---

## GmailClient Component

### Purpose

The GmailClient implements the Client protocol to interact with the Gmail API. It supports sending and reading emails, reading attachments, deleting messages, and marking messages as read. The component is modular, testable, and can be replaced by a DummyClient for offline testing.

### Core Methods and Inputs/Outputs

- **send_message(to: str, subject: str, body: str, attachments: Optional[list[Attachment]]) -> bool**
  Sends an email with optional file attachments.
  **Input:** to, subject, body, optional attachments
  **Output:** bool (success)

- **get_messages() -> Iterator[Message]**
  Retrieves recent inbox messages.
  **Output:** generator of Message objects

- **get_message(message_id: str) -> Optional[Message]**
  Retrieves a message by ID.
  **Input:** message_id
  **Output:** Message or None

- **delete_message(message_id: str) -> bool**
  Deletes a message by moving it to trash.
  **Input:** message_id
  **Output:** bool (success)

- **mark_as_read(message_id: str) -> bool**
  Marks a message as read by removing the "UNREAD" label.
  **Input:** message_id
  **Output:** bool (success)

---

### Example Usage

```python

from gmail_client import get_gmail_client

client = get_gmail_client("credentials.json", "token.json")


# Send an email

client.send_message(
to="recipient@example.com",
subject="Hello from Gmail Client",
body="This is a test email.",
attachments=[]
)

# List messages

for message in client.get_messages():
print(message.subject)

# Mark message as read

client.mark_as_read("123456")

# Delete a message

client.delete_message("123456")

```

---

### Component Interaction and Testing

The Gmail client is accessed via get_gmail_client() and implements the Client protocol defined in mail_client/interface.py. It can be replaced with a DummyClient for testing, enabling safe offline test runs.

Tests are located under the tests/ folder and use pytest. The DummyClient mimics Gmail functionality and adheres to the same interface as the real implementation, ensuring consistent behavior.

### Best Practices Followed

- **Interfaces with Protocols:** Abstract definitions for consistent implementations.

- **Dependency Injection:** GmailClient is created via a factory to enable decoupling and easy substitution.

- **Modularity:** Logical separation between messages, attachments, and core client logic.

- **Testability:** Dummy client enables full unit testing without network calls.

- **CI-Ready:** Designed to be linted (ruff), type-checked (mypy), and tested in CI/CD environments via CircleCI.
