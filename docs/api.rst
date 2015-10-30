:mod:`gs.group.messages.text` API
=================================

.. currentmodule:: gs.group.messages.text

There are three parts to the API provided by the
:mod:`gs.group.messages.text` product. The `split message`_ code
separates the bottom quoting and signatures from the rest of the
message. The `HTML body`_ code will format the parts of the
message, using the matcher_ code.

Split message
-------------

An email message is normally in two parts: the actual body of the
message, and then some trailing bottom quoting and
signatures. The :data:`SplitMessage` named tuple represents this
duality, while the :func:`split_message` function does the actual
splitting. Both parts of the message can be fed into the
:class:`HTMLBody` class to generate the markup.

.. autodata:: gs.group.messages.text.SplitMessage
   :annotation: (:class:`collections.namedtuple`)

.. autofunction:: gs.group.messages.text.split_message

HTML body
---------

The :class:`HTMLBody` class will format a plain-text message as
HTML. The changes that are made include the following.

* The characters that would cause issues with the XML are
  escaped. This includes ``"`` and ``'`` characters.

* Each line is placed within a ``<span>`` element, with the CSS
  class set to ``line``.

  .. code-block:: xml

     <span class="line">Like this</span>

* Lines that start with ``>`` but not ``>From`` are considered
  quotes, and given the additional CSS class ``muted``.

  .. code-block:: xml

     <span class="line muted">&gt; Like this</span>

* The words of the line markup by the matcher_ classes.

.. autoclass:: gs.group.messages.text.HTMLBody
   :member-order: bysource
   :members:
   :special-members: __iter__, __str__, __unicode__

Matcher
-------

The *matcher* classes 

* Test that a word matches, and
* Produce a substitute for the word.

They all inherit from the :class:`Matcher` class.

.. autoclass:: gs.group.messages.text.Matcher
   :member-order: bysource
   :members:

Instances
~~~~~~~~~

Four instances of the :class:`Matcher` class are provided to make
the following changes to the email.

* Words in ``*asterisk*`` characters are made bold

  .. autodata:: gs.group.messages.text.boldMatcher

* Email addresses are made clickable 

  .. autodata:: gs.group.messages.text.emailMatcher

* Site names starting with ``www`` are made clickable.

  .. autodata:: gs.group.messages.text.wwwMatcher

* URLs (``http`` and ``https``) are made clickable.

  .. autodata:: gs.group.messages.text.uriMatcher
