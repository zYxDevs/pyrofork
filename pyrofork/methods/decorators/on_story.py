#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.


from typing import Callable

import pyrofork
from pyrofork.filters import Filter


class OnStory:
    def on_story(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling new stories.

        This does the same thing as :meth:`~pyrofork.Client.add_handler` using the
        :obj:`~pyrofork.handlers.StoryHandler`.

        Parameters:
            filters (:obj:`~pyrofork.filters`, *optional*):
                Pass one or more filters to allow only a subset of stories to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrofork.Client):
                self.add_handler(pyrofork.handlers.StoryHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrofork.handlers.StoryHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator
