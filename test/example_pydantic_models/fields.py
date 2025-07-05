from pydantic import Field

from .base import BaseConfig

class BaseTypesWithFields(BaseConfig):
    """
    Test case: Basic types with Field definition
    """
    integer: int = Field(10, description="An integer")
    string: str = Field("hello", description="A string")
    float: float = Field(3.14, description="A float")
    boolean: bool = Field(True, description="A boolean")