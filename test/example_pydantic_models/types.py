from .base import BaseConfig

class BaseTypes(BaseConfig):
    """
    Test case: Basic types without Field definition
    """
    integer: int
    string: str
    float: float
    boolean: bool
    dictionary: dict
    list: list

class BaseTypesWithDefaults(BaseConfig):
    """
    Test case: Basic types with Field definition
    """
    integer: int = 10
    string: str = "hello"
    float: float = 3.14
    boolean: bool = True
    dictionary: dict = {"key": "value"}
    list: list = [1, 2, 3]

class BaseTypesWithOptional(BaseConfig):
    """
    Test case: Basic types with Field definition
    """
    integer: int | None = None
    string: str | None = None
    float: float | None = None
    boolean: bool | None = None
    dictionary: dict | None = None
    list: list | None = None

class BaseTypesWithOptionalAndDefaults(BaseConfig):
    """
    Test case: Basic types with Field definition
    """
    integer: int | None = 10
    string: str | None = "hello"
    float: float | None = 3.14
    boolean: bool | None = True
    dictionary: dict | None = {"key": "value"}
    list: list | None = [1, 2, 3]