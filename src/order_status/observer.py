from typing import Protocol


class Observer(Protocol):
    def update(self, order_id: str, status: str) -> None:
        ...
