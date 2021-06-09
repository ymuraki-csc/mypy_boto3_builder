from typing import Any

from botocore.exceptions import CapacityNotAvailableError as CapacityNotAvailableError

class Clock:
    def __init__(self) -> None: ...
    def sleep(self, amount: Any) -> None: ...
    def current_time(self) -> Any: ...

class TokenBucket:
    def __init__(self, max_rate: Any, clock: Any, min_rate: Any = ...) -> None: ...
    @property
    def max_rate(self) -> Any: ...
    @max_rate.setter
    def max_rate(self, value: Any) -> None: ...
    @property
    def max_capacity(self) -> Any: ...
    @property
    def available_capacity(self) -> Any: ...
    def acquire(self, amount: int = ..., block: bool = ...) -> Any: ...
