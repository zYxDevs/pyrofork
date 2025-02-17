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

from typing import Union

import pyrofork
from pyrofork import raw, types


class GetChatAdminsWithInviteLinks:
    async def get_chat_admins_with_invite_links(
        self: "pyrofork.Client",
        chat_id: Union[int, str],
    ):
        """Get the list of the administrators that have exported invite links in a chat.

        You must be the owner of a chat for this to work.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).
                You can also use chat public link in form of *t.me/<username>* (str).

        Returns:
            List of :obj:`~pyrofork.types.ChatAdminWithInviteLink`: On success, the list of admins that have exported
            invite links is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetAdminsWithInvites(
                peer=await self.resolve_peer(chat_id)
            )
        )

        users = {i.id: i for i in r.users}

        return types.List(
            types.ChatAdminWithInviteLinks._parse(self, admin, users)
            for admin in r.admins
        )
