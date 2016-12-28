:mod:`easycolor.parser` --- Advanced text style
===============================================

.. module:: easycolor.parser
    :synopsis: A module that provides advanced styling

---------------

This module defines the :class:`.ColorParser` class which is used to
create advnaced text styles.

.. currentmodule:: easycolor.parser

.. autoclass:: ColorParser
    :members: parse, cprint

Usage
--------
First obtain an instance::
   
    from easycolor.parser import ColorParser
    parser = ColorParser()

Then for printing::
    
    cprint = parser.cprint
    # Add rainbow colors!
    cprint("""<f:red>r<f:yellow>ai<f:green>nb<f:blue>o<f:magenta>w"""
           """</f>o</f>bn</f>ia</f>r</f>""")
    # complex foreground - background
    cprint("""<f:red,b:yellow>red on yellow</b>just red<b:black>red on black!"""
           """<f:green>green on black</f>again red on black</f,b>normal""")

Parse a format string for a colored logger, for later use::
    
    INFO = parser.parse("[<f:cyan>INFO</f>] <o:bold>{}")
    print(INFO.format('Some info..'))

