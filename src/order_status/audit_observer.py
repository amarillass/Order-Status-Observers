class AuditObserver:
    def __init__(self):
        self.entries = []

    def update(self, order_id: str, status: str) -> None:
        self.entries.append((order_id, status))
