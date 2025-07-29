# **Gmail Client**

## **Overview**

This repository provides a modular, testable Gmail client implemented in Python using interface-based design. It offers a clean abstraction for interacting with Gmail via the Gmail API or a dummy backend and is built with best practices like CI/CD, type-checking, and unit testing in mind.

## **Features**

1. **📬 Send & Receive Emails:** Easily send messages and fetch inbox content.
2. **🧩 Protocol-Based Interface:** Designed for extensibility via Protocol interfaces.
3. **🧪 Dummy Client:** A mock implementation for testing without live credentials.
4. **📎 Attachment Handling:** Read and decode email attachments.
5. **✅ CI/CD Integration:** CircleCI pipeline with linting, type-checking, and test coverage.
6. **🧼 Strict Type Safety:** mypy enforced across the codebase.

## ** Project Structure**

```
.
├── gmail_client/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── interface.py
│   │   ├── gmail_client.py
│   │   ├── gmail_message.py
│   │   ├── gmail_attachment.py
│   │   ├── factories.py
│   └── tests/
│       ├── test_dummy_client.py
│       ├── test_gmail_client.py
├── tests/
│   ├── test_integration.py
│   └── test_end_to_end.py
│   └── test_end_to_end.py
└── test-results/
│   ├── junit.xml                # Pytest JUnit test result file
│   └── result.csv               # Created after running the file in tools folder
├── tools/                       # Utility scripts
│   └── convert_junit_to_csv.py  # Converts test results to CSV
├── credentials.json
├── token.json
├── pyproject.toml
├── uv.lock
├── .circleci/
│   └── config.yml
├── README.md
└── .gitignore

```

## **🚀 Getting Started**

## **🔧 Prerequisites**

- Python 3.10+
- Gmail API credentials

**🔑 Setup OAuth**

1. Go to Google Cloud Console

2. Create or select a project

3. Enable Gmail API

4. Set up OAuth 2.0 credentials (Desktop App) and download credentials.json

5. Place credentials.json in the project root

6. The first run will generate token.json after browser authentication

## **📦 Installation**

```
git clone https://github.com/Jasmeet-011/Open-Source_-Assignment.git
cd python-template-repo
git checkout interface-definition

uv pip install -e .
uv sync --group dev

```

## **🧪 Running Tests**

```
uv run pytest

```

**To run with coverage and generate an HTML report:**

```
uv run pytest --cov=gmail_client --cov=tests --cov-report=html

```

**To convert the JUnit results to CSV:**

```
uv run tools/convert_junit_to_csv.py

```

The output file will be saved at: **test-results/result.csv**

Open htmlcov/index.html in your browser to view detailed coverage

## **🔁 CircleCI Pipeline**

CircleCI is configured to automatically:

- Install dependencies using **uv**

- Set up **PYTHONPATH**

- Run **ruff** for linting

- Run **mypy** for type-checking

- Run **pytest** with coverage and store results

- Upload artifacts like coverage reports and logs

The config file is located at **.circleci/config.yml**.

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

## **Project Scope**

### ✅ Minimum Viable Product (MVP)

- Interface and implementation of Gmail client.
- Gmail client using Protocol
- Support for sending, reading, and deleting messages
- Read attachment content
- Dummy client for isolated testing
- CI pipeline using CircleCI
- Linting and type checking with Ruff and Mypy
- Unit, integration, and e2e tests

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
