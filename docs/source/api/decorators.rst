Decorators
==========

Decorators are able to register callback functions for handling updates in a much easier and cleaner way compared to
:doc:`Handlers <handlers>`; they do so by instantiating the correct handler and calling
:meth:`~pyrofork.Client.add_handler` automatically. All you need to do is adding the decorators on top of your
functions.

.. code-block:: python

    from pyrofork import Client

    app = Client("my_account")


    @app.on_message()
    def log(client, message):
        print(message)


    app.run()

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

-----

.. currentmodule:: pyrofork

Index
-----

.. hlist::
    :columns: 3

    - :meth:`~Client.on_message`
    - :meth:`~Client.on_edited_message`
    - :meth:`~Client.on_callback_query`
    - :meth:`~Client.on_message_reaction_updated`
    - :meth:`~Client.on_message_reaction_count_updated`
    - :meth:`~Client.on_inline_query`
    - :meth:`~Client.on_chosen_inline_result`
    - :meth:`~Client.on_chat_member_updated`
    - :meth:`~Client.on_chat_join_request`
    - :meth:`~Client.on_deleted_messages`
    - :meth:`~Client.on_user_status`
    - :meth:`~Client.on_story`
    - :meth:`~Client.on_poll`
    - :meth:`~Client.on_disconnect`
    - :meth:`~Client.on_raw_update`

-----

Details
-------

.. Decorators
.. autodecorator:: pyrofork.Client.on_message()
.. autodecorator:: pyrofork.Client.on_edited_message()
.. autodecorator:: pyrofork.Client.on_callback_query()
.. autodecorator:: pyrofork.Client.on_message_reaction_updated()
.. autodecorator:: pyrofork.Client.on_message_reaction_count_updated()
.. autodecorator:: pyrofork.Client.on_inline_query()
.. autodecorator:: pyrofork.Client.on_chosen_inline_result()
.. autodecorator:: pyrofork.Client.on_chat_member_updated()
.. autodecorator:: pyrofork.Client.on_chat_join_request()
.. autodecorator:: pyrofork.Client.on_deleted_messages()
.. autodecorator:: pyrofork.Client.on_user_status()
.. autodecorator:: pyrofork.Client.on_story()
.. autodecorator:: pyrofork.Client.on_poll()
.. autodecorator:: pyrofork.Client.on_disconnect()
.. autodecorator:: pyrofork.Client.on_raw_update()
