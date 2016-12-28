:mod:`easycolor.style` - Simple text style
=============================================

.. module:: easycolor.style
    :synopsis: A module that provides simple styling

---------------

This module defines the :class:`.TextStyle` class which is the basis
for creating text styles.
It also provides helper functions for easier usage.

.. attribute:: RESET

Reset all style.

-------------------

.. autoclass:: TextStyle
    :members: fg, bg, opt, compile
    :special-members: __str__, __call__

-------------------

.. autofunction:: make_style

-------------------

.. autofunction:: wrap


Usage
--------
To wrap text, the :func:`.wrap` function must be imported.

::

    from easycolor.style import wrap as _w

The text is then wrapped as easy as::
    
    # wrap text, appends a style-reset
    print(_w('yellow on red', fg='yellow', bg='red'))
    print('normal text')

To compile a style, the :func:`.make_style` function is used:

::

    from easycolor.style import make_style, RESET

Example:

::

    # define some styles
    black_on_white = make_style(fg='black', bg='white')
    # we have to reset the background here
    red_bold = make_style(fg='red', bg='reset', opt='bold')
    # An options reset is only possible with a total reset
    # we can however negate an option to remove it('!option').
    green_bold_underline = make_style(fg='green', opt=('!bold', 'underline'))

    print(black_on_white + 'Black on white' + red_bold + 'Red bold' +
          green_bold_underline + 'Green not bold underline' + RESET)
    
**Note**: For advanced formatting use the :mod:`easycolor.parser` module.


