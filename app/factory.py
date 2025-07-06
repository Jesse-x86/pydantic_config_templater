from .formatters import *

_factory: dict[str, type[BaseFormatter]] = {
    "json": JsonFormatter,
    "yaml": YamlFormatter,
}

class FormatterFactory:
    @staticmethod
    def get_formatter(file_format: str) -> BaseFormatter:
        if file_format is None:
            raise ValueError("Either custom_formatter or file_format must be provided.")
        if file_format not in _factory:
            raise ValueError(f"Unsupported file format: {file_format}.")
        return _factory[file_format]()

    @staticmethod
    def register_formatter(file_format: str, formatter: type[BaseFormatter]):
        if not file_format:
            raise ValueError("file_format must be provided.")
        if not issubclass(formatter, BaseFormatter):
            raise ValueError("formatter must be a subclass of BaseFormatter.")
        _factory[file_format] = formatter

    @staticmethod
    def has_formatter(file_format: str) -> bool:
        return file_format in _factory