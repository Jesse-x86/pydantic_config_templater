# Parser
# Use to parse pydantic (config) model to provide templates
# Core of the entire lib
from pydantic import BaseModel

from app.factory import FormatterFactory
from app.formatters import BaseFormatter
from factory import _factory

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
    # 我想把这部分抽象成一个类方便继承，但是还没想好怎么写
    # I'm thinking bout making this a class but idk how is better yet
    # --- Initialize Formatter ---
    if custom_formatter is None:
        # all error handling happens in get_formatter()
        custom_formatter = FormatterFactory.get_formatter(file_format)

    # --- Start Parsing ---
    final_obj: list[str] = []
    if not isinstance(model, BaseModel):
        raise TypeError("model must be a pydantic BaseModel.")
    for field_name, field_info in model.model_fields.items():
        # --- Get Field Type ---
        field_type = field_info.annotation

        # How do i format these bs...?

        # --- Get Field Default Value ---
        field_default = field_info.default
        field_default_factory = field_info.default_factory
        # --- Get Field Description ---
        field_description = field_info.description
        # --- Get Field Examples ---
        field_examples = field_info.examples

        # I don't think we need those but I'll add them when needed
        # --- Get Field Alias ---
        # field_alias = field_info.alias
        # field_alias_priority = field_info.alias_priority
        # --- ...


    return "\n".join(final_obj)

