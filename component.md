# Gmail Client Component

## Concept of a Component

In software architecture, a **component** is a modular, encapsulated, and reusable unit that performs a specific set of related tasks. It exposes a clear interface, is loosely coupled, and is designed to be independently tested or replaced.

In this repository, the Gmail Client is one such component. It encapsulates all logic related to interacting with Gmail—sending messages, retrieving inbox data, managing attachments, and more. Its design promotes modularity, testability, and flexibility through clear interfaces and dependency injection.

---

### Directory Structure

```
gmail_client/
│ ├── src/
│ │ ├── init.py # Public API & exports
│ │ ├── interface.py # Protocols for Client, Message, and Attachment
│ │ ├── gmail_client.py # GmailClient implementation
│ │ ├── gmail_message.py # GmailMessage implementation of Message
│ │ ├── gmail_attachment.py # GmailAttachment implementation
│ │ └── factories.py # Factory to construct the correct Client
│
│ └── tests/
│ ├── test_dummy_client.py # Unit tests using DummyClient
│ └── test_gmail_client.py # Unit tests for GmailClient
│
tests/
│ ├── test_integration.py # Integration tests for GmailClient behavior
│ └── test_end_to_end.py # E2E pipeline for full email flow
```

---

## GmailClient Component

### Purpose

The `GmailClient` implements the `Client` protocol to interact with Gmail via the official Gmail API. It supports:

- Sending messages with optional attachments
- Fetching inbox messages
- Accessing individual messages
- Marking messages as read
- Deleting messages

It is designed to be swappable with a mock implementation (`DummyClient`) for testing purposes.

---

## Methods and Inputs/Outputs

- **send_message(to: str, subject: str, body: str, attachments: Optional[list[Attachment]]) → bool**  
  Sends an email via Gmail API.  
  **Input:** Recipient email, subject, body, optional attachments  
  **Output:** Success flag

- **get_messages() → Iterator[Message]**  
  Fetches inbox messages.  
  **Output:** Generator of Message objects

- **get_message(message_id: str) → Optional[Message]**  
  Fetches a single message by ID.  
  **Input:** Gmail message ID  
  **Output:** Message or None

- **delete_message(message_id: str) → bool**  
  Moves the message to trash.  
  **Input:** Gmail message ID  
  **Output:** Success flag

- **mark_as_read(message_id: str) → bool**  
  Removes the `UNREAD` label from the message.  
  **Input:** Gmail message ID  
  **Output:** Success flag

---

## Example Usage

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

# List recent messages
for message in client.get_messages():
    print(message.subject)

# Mark a message as read
client.mark_as_read("123456")

# Delete a message
client.delete_message("123456")
```

---

## Component Interaction and Testing

This component adheres to the **Client** protocol defined in **interface.py**. It is constructed via a factory (**get_gmail_client**) to allow clean separation of logic and runtime flexibility.

For testing, a **DummyClient** is provided that mimics Gmail behavior without making real API calls. This allows for safe and repeatable unit tests. Tests are structured as:

- Unit tests (inside **gmail_client/tests/**) for each method using DummyClient and GmailClient

- Integration and E2E tests (**inside tests/**) to verify full real-world Gmail interactions

## Best Practices Followed

- 🧩 **Protocol-Based Interfaces:** Clean, swappable implementations using Python Protocol

- 🔌 **Dependency Injection:** Construct clients via factories for modularity

- 🧪 **Full Test Coverage:** Unit + Integration + E2E testing with pytest

- 📦 **Modular Design:** Separated logic for message, attachment, and client

- ✅ **CI Integration:** Automated lint, type-check, and test steps via CircleCI

- 🧼 **Type Safety:** mypy checks enforced across all logic and tests
