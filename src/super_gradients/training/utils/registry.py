import inspect
from typing import Callable, Dict, Optional

from super_gradients.training.models.all_architectures import ARCHITECTURES


def create_register_decorator(registry: Dict[str, Callable]) -> Callable:
    """
    Create a decorator that registers object of specified type (model, metric, ...)

    :param registry: The registry (maps name to object that you register)
    :return:         Register function
    """
    def register(name: Optional[str] = None) -> Callable:
        """
        Set up a register decorator.

        :param name: If specified, the decorated object will be registered with this name.
        :return:     Decorator that registers the callable.
        """
        def decorator(cls: Callable) -> Callable:
            """Register the decorated callable"""
            cls_name = name if name is not None else cls.__name__

            if cls_name in registry:
                ref = registry[cls_name]
                raise Exception(f"`{cls_name}` is already registered and points to `{inspect.getmodule(ref).__name__}.{ref.__name__}")

            registry[cls_name] = cls
            return cls
        return decorator
    return register


register_model = create_register_decorator(registry=ARCHITECTURES)