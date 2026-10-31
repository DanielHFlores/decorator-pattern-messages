# Message Decorators — Starter

## Your task
1. Keep `PlainMessage` unchanged.
2. Introduce a Decorator that is still a `Message` and wraps another `Message`.
3. Implement `UrgentDecorator`.
4. Implement `TimestampDecorator`.
5. Stack both around one message.
6. Add/update one focused test.
7. Explain whether order matters and one complexity cost.

Use a deterministic timestamp approach so tests remain stable.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.

## Design Explanation

The Decorator Pattern allows additional functionality to be added to messages without modifying the original PlainMessage class.

MessageDecorator implements the Message interface and wraps another Message object. UrgentDecorator and TimestampDecorator extend this base decorator to add their respective functionalities.

Both decorators can be stacked around the same message.

## Decorator Order

The order of decorators matters because each decorator modifies the result returned by the wrapped message.

For example:

- TimestampDecorator(UrgentDecorator(message)) adds the timestamp before the urgent label.
- UrgentDecorator(TimestampDecorator(message)) adds the urgent label before the timestamp.

Both combinations are valid, but they produce different outputs.

## Complexity Cost

Each decorator introduces an additional object and a layer of delegation. As more decorators are stacked, the wrapper chain can become harder to understand, debug, and maintain.