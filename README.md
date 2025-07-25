# **Gmail Client**

## **Overview**

The Gmail Client is a modular Python component that provides a well-typed, interface-driven implementation for interacting with Gmail. Designed with reusability, testability, and clarity in mind, it enables users to fetch, send, and manage email messages via the Gmail API or a dummy backend.

## **Features**

1. **Send and receive messages:** Compose and send emails using Gmail or mock data.
2. **Message retrieval:** Access inbox messages and individual messages by ID.
3. **Attachment handling:** Read and decode file attachments from emails.
4. **Mock support:** Use a DummyClient for testing without real Gmail credentials.

## **API Reference**

### **GmailClient Class**

**Initialization**

```python
from gmail_client import get_gmail_client
client = get_gmail_client("credentials.json", "token.json")
```

1. **send_message(to: str, subject: str, body: str, attachments: Optional[list[Attachment]]) -> bool**

- Sends an email with optional attachments.

Args:

- `to` (str): Recipient email address.

- `subject` (str): Subject of the message.

- `body` (str): Message body content.

- `attachments` (list, optional): List of file attachments.

Returns:

- `bool` – Success status.

2. **get_messages() -> Iterator[Message]**

- Retrieves inbox messages.

  Returns:

  - `Iterator[Message]`: Generator of message objects.

3. **get_message(message_id: str) -> Optional[Message]**

- Retrieves a specific message by ID.

  Args:

  - `message_id` (str): Gmail message ID.

  Returns:

  - `Optional[Message]`: The corresponding message or None.

4. **delete_message(message_id: str) -> bool**

- Trashes an email by ID.

  Args:

  - `message_id` (str): Gmail message ID.

  Returns:

  - `bool`: Success status.

5. **mark_as_read(message_id: str) -> bool**

- Removes the "UNREAD" label from a message.

  Args:

  - `message_id (str)`: Gmail message ID.

  Returns:

  - `bool`: Success status.

## **Setup & Installation**

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Jasmeet-011/Open-Source_-Assignment.git
cd python-template-repo
git checkout interface-definition
```

### 2️⃣ Install Dependencies

```sh
uv pip install -e .
```

### 3️⃣ Run Tests

```sh
uv run pytest
```

## **Project Scope**

### ✅ Minimum Viable Product (MVP)

- Interface and implementation of Gmail client.
- Support for sending, reading, and deleting messages
- Read attachment content
- Fully tested using a DummyClient
- CI pipeline using CircleCI
- Linting and type checking with Ruff and Mypy

### ❌ Out of Scope

- OAuth setup or token refresh UX
- Real-time email polling
- Rich HTML message composition or threading

## **Contributing**

- Fork the repo.
- Create a new branch: `git checkout -b feature-name`
- Commit changes: `git commit -m "Add feature"`
- Push and create a PR.

## **License**

This project is licensed under the MIT License.
