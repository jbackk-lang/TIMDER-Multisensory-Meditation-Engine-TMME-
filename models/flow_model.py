class FlowModel:
    """
    Metamodel strumienia TIMDER-FLOW.
    """

    def __init__(self, name: str = "Geometric Meditation 01"):
        self.name = name

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "version": "0.1",
        }
