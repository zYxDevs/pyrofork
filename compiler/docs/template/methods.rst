Available Methods
=================

This page is about Pyrofork methods. All the methods listed here are bound to a :class:`~pyrofork.Client` instance,
except for :meth:`~pyrofork.idle()` and :meth:`~pyrofork.compose()`, which are special functions that can be found in
the main package directly.

.. code-block:: python

    from pyrofork import Client

    app = Client("my_account")

    with app:
        app.send_message("me", "hi")

-----

.. currentmodule:: pyrofork.Client

Utilities
---------

.. autosummary::
    :nosignatures:

    {utilities}

.. toctree::
    :hidden:

    {utilities}

.. currentmodule:: pyrofork

.. autosummary::
    :nosignatures:

    idle
    compose

.. toctree::
    :hidden:

    idle
    compose

.. currentmodule:: pyrofork.Client

Conversation
------------

.. autosummary::
    :nosignatures:

    {conversation}

.. toctree::
    :hidden:

    {conversation}

Messages
--------

.. autosummary::
    :nosignatures:

    {messages}

.. toctree::
    :hidden:

    {messages}

Stories
-------

.. autosummary::
    :nosignatures:

    {stories}

.. toctree::
    :hidden:

    {stories}

Chats
-----

.. autosummary::
    :nosignatures:

    {chats}

.. toctree::
    :hidden:

    {chats}

Stickers
--------

.. autosummary::
    :nosignatures:

    {stickers}

.. toctree::
    :hidden:

    {stickers}

Users
-----

.. autosummary::
    :nosignatures:

    {users}

.. toctree::
    :hidden:

    {users}

Invite Links
------------

.. autosummary::
    :nosignatures:

    {invite_links}

.. toctree::
    :hidden:

    {invite_links}

Contacts
--------

.. autosummary::
    :nosignatures:

    {contacts}

.. toctree::
    :hidden:

    {contacts}

Password
--------

.. autosummary::
    :nosignatures:

    {password}

.. toctree::
    :hidden:

    {password}

Bots
----

.. autosummary::
    :nosignatures:

    {bots}

.. toctree::
    :hidden:

    {bots}

Authorization
-------------

.. autosummary::
    :nosignatures:

    {authorization}

.. toctree::
    :hidden:

    {authorization}

Advanced
--------

Methods used only when dealing with the raw Telegram API.
Learn more about how to use the raw API at :doc:`Advanced Usage <../../topics/advanced-usage>`.

.. autosummary::
    :nosignatures:

    {advanced}

.. toctree::
    :hidden:

    {advanced}