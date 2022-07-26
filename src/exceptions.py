from typing import Optional


class MissingAttributeException(AttributeError):
    def __init__(self, missing_attribute: str, message: Optional[str],
                 *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.missing_value = missing_attribute

    def __str__(self) -> str:
        message = f"Missing required attribute: {self.missing_value}"
        if self.message:
            message += f"\n{self.message}"
        return message