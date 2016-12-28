Python Easy Color
======================
Color output in python2/3 made easy!

Description
===========

Make python color ouput easy in UNIX terminals
that support ANSI sequences.

Documentation
=============

Check the documentation at: (https://georgetg.github.io/easycolor/)

Source Code
===========

Check at github: (https://github.com/GeorgeTG/easycolor)

License
=======

Copyright George T. Gougoudis 2016. BSD 3-Clause license; see LICENSE file.


Basic usage
===========

To wrap text, the wrap function must be imported.

.. code-block:: python

    from easycolor.style import wrap as _w

The text is then wrapped as easy as

.. code-block:: python

    # wrap text, appends a style-reset
    print(_w('yellow on red', fg='yellow', bg='red'))
    print('normal text')

To compile a style, the make_style function is used:

.. code-block:: python

    from easycolor.style import make_style, RESET

Example:

.. code-block:: python

    # define some styles
    black_on_white = make_style(fg='black', bg='white')
    # we have to reset the background here
    red_bold = make_style(fg='red', bg='reset', opt='bold')
    # An options reset is only possible with a total reset
    # we can however negate an option to remove it('!option').
    green_bold_underline = make_style(fg='green', opt=('!bold', 'underline'))

    print(black_on_white + 'Black on white' + red_bold + 'Red bold' +
          green_bold_underline + 'Green not bold underline' + RESET)
    
**Note**: For advanced formatting use the easycolor.parser module.


Advanced usage
==============

First obtain an instance

.. code-block:: python
   
    from easycolor.parser import ColorParser
    parser = ColorParser()

Then for printing

.. code-block:: python

    cprint = parser.cprint
    # Add rainbow colors!
    cprint("""<f:red>r<f:yellow>ai<f:green>nb<f:blue>o<f:magenta>w"""
           """</f>o</f>bn</f>ia</f>r</f>""")
    # complex foreground - background
    cprint("""<f:red,b:yellow>red on yellow</b>just red<b:black>red on black!"""
           """<f:green>green on black</f>again red on black</f,b>normal""")

Parse a format string for a colored logger, for later use

.. code-block:: python
    
    INFO = parser.parse("[<f:cyan>INFO</f>] <o:bold>{}")
    print(INFO.format('Some info..'))

