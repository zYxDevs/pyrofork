#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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

from .handler import Handler


class ChatJoinRequestHandler(Handler):
    """The ChatJoinRequest handler class. Used to handle join chat requests.
    It is intended to be used with :meth:`~pyrofork.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrofork.Client.on_chat_join_request` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new ChatJoinRequest event arrives. It takes
            *(client, chat_join_request)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrofork.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        chat_join_request (:obj:`~pyrofork.types.ChatJoinRequest`):
            The received chat join request.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
