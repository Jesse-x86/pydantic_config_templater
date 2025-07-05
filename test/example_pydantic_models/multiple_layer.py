from .base import BaseConfig

class Layer_1(BaseConfig):
    """
    Layer 1 configuration class.
    Test case: Multiple layers of inheritance
    """
    layer_1: str = "layer_1"

class Layer_2(Layer_1):
    """
    Layer 2 configuration class.
    Test case: Multiple layers of inheritance
    """
    layer_2: str = "layer_2"

class Layer_3(Layer_2):
    """
    Layer 3 configuration class.
    Test case: Multiple layers of inheritance
    """
    layer_3: str = "layer_3"