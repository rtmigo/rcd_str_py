# SPDX-FileCopyrightText: (c) 2020-2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import re
from pathlib import Path

from typing import Union, Optional


class LazyRegex:
    """Регулярное выражение, которое будет скомпилировано только при запросе
    свойства `compiled`.

    При создании объекта достаточно иметь это выражение в строке или даже
    просто ссылку на файл с выражением."""
    def __init__(self, source: Union[str, Path], flags: int):
        if source is None:
            raise ValueError
        self._source: Optional[Union[str, Path]] = source
        self._rx: Optional[re.Pattern] = None
        self._flags = flags

    @property
    def compiled(self) -> re.Pattern:
        if self._rx is not None:
            return self._rx

        if isinstance(self._source, Path):
            pattern = self._source.read_text()
        else:
            assert self._source is not None
            pattern = self._source

        if self._rx is None:
            self._rx = re.compile(pattern, self._flags)
            # _source может содержать дольно большие строки (мы ведь даже
            # захотели ленивую компиляцию). Поэтому скомпилировав регекс,
            # удаляем ссылку на исходник
            self._source = None

        assert self._rx is not None
        return self._rx
