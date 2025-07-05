# Parser
# Use to parse pydantic (config) model to provide templates
# Core of the entire lib
from pydantic import BaseModel

from app.formatters import BaseFormatter
from factory import factory

def parse(model: BaseModel,
          custom_formatter: BaseFormatter = None,
          file_format: str = None,
          with_notes: bool = True) -> str:
    """
    解析一个pydantic模型以提供模板。
    Parse a pydantic model to provide templates.
    :param model: 要解析的pydantic模型。The pydantic model to parse.
    :param custom_formatter: 自定义格式化器，留空以基于file_format从工厂中获取。Custom formatter, leave empty to get from factory based on file_format.
    :param file_format: 当custom_formatter为空时，用于从工厂获取格式化器的文件格式。File format used when custom_formatter is empty to get formatter from factory.
    :param with_notes: 是否包含注释。Whether to include notes.
    :return: 解析后的模板字符串。Parsed template string.
    """

    # --- Initialize Formatter ---
    if custom_formatter is None:
        if file_format is None:
            raise ValueError("Either custom_formatter or file_format must be provided.")
        if file_format not in factory.formatters:
            raise ValueError(f"Unsupported file format: {file_format}.")
        custom_formatter = factory.get_formatter(file_format)()

    # --- Start Parsing ---
    # TODO: Actually parse stuff