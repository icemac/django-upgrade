from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    str_removeprefix = str.removeprefix
else:

    def str_removeprefix(self: str, prefix: str, /) -> str:  # pragma: no cover
        return self[len(prefix) :] if self.startswith(prefix) else self[:]
