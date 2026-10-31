from messages.plain_message import PlainMessage
from messages.urgent_decorator import UrgentDecorator
from messages.timestamp_decorator import TimestampDecorator


def test_decorators_can_be_stacked_in_different_orders():
    message = PlainMessage("Deploy complete")
    timestamp = "2026-10-30 20:00"

    first = TimestampDecorator(
        UrgentDecorator(message), timestamp
    )

    second = UrgentDecorator(
        TimestampDecorator(message, timestamp)
    )

    assert first.render() == "[2026-10-30 20:00] [URGENT] Deploy complete"
    assert second.render() == "[URGENT] [2026-10-30 20:00] Deploy complete"