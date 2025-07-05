from typing import Protocol


class TemplateFormatter(Protocol):
    """
    格式化器模版
    用来将从Pydantic模型中解析出来的数据处理成为实际的配置文件
    此处仅提供接口，不提供具体实现
    """

    # TODO: define funcs and provide implements elsewhere