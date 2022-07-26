class MissingAttributeException(AttributeError):
    def __init__(self, missing_attribute: str, *args: object) -> None:
        super().__init__(*args)
        self.missing_value = missing_attribute

    def __str__(self) -> str:
        return f"Missing required attribute: {self.missing_value}"