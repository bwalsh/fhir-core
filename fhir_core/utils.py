import typing
from functools import lru_cache
from typing import get_args, get_origin
import uuid
import datetime
from pydantic.fields import FieldInfo

__author__ = "Md Nazrul Islam"
__email__ = "email2nazrul@gmail.com"

PY_PRIMITIVES = frozenset(
    [
        str,
        int,
        bool,
        float,
        datetime.datetime,
        datetime.date,
        datetime.time,
        uuid.UUID,
    ]
)


def _is_primitive_type(annotation: typing.Any) -> typing.Union[bool, None]:
    """ """
    origin = get_origin(annotation)
    if origin is None:
        if annotation in PY_PRIMITIVES:
            return True
        raise NotImplementedError

    args = get_args(annotation)
    for arg in args:
        if _is_primitive_type(arg) is not None:
            # check number of args
            return True
    return


@lru_cache(maxsize=1024, typed=True)
def is_primitive_type(field: FieldInfo) -> bool:
    """ """
    return _is_primitive_type(field.annotation) is not None
