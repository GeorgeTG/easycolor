# Copyright George T. Gougoudis 2016. BSD 3-Clause license; see LICENSE file.
import collections
import functools

# Constants
COLOR_NAMES = ('black', 'red', 'green', 'yellow',
               'blue', 'magenta', 'cyan', 'white')
OPT_NAMES = ('bold', 'faint', 'italic', 'underline',
             'blink', 'blink_fast', 'negative',
             'conceal', 'strikeout')


_TEMPLATE = '\x1b[%sm'
_FOREGROUND = {COLOR_NAMES[x]: 30 + x for x in range(8)}
_FOREGROUND['reset'] = 39
_BACKGROUND = {COLOR_NAMES[x]: 40 + x for x in range(8)}
_BACKGROUND['reset'] = 49
_OPT_DICT = {OPT_NAMES[x-1]: x for x in range(1, 10)}

RESET = _TEMPLATE % '0'
""" Reset all style """


def _opt_reverse(opt):
    return 20 + opt


def _get_iterable(x):
    if isinstance(x, str):
        return (x,)
    elif isinstance(x, collections.Iterable):
        return x
    else:
        return (x,)


def make_style(fg=None, bg=None, opt=()):
    """
    The keyword arguments fg, bg, opt can be used to define the style.
    """
    return TextStyle(fg=fg, bg=bg, opt=opt).compile()


def wrap(text, fg=None, bg=None, opt=()):
    """
    The keyword arguments fg, bg, opt can be used to define the style,
    appends reset after the text.
    """
    return (TextStyle(fg=fg, bg=bg, opt=opt).compile() +
            text + TextStyle.RESET)


class InvalidOption(Exception):
    pass


def _try_key(function):
    @functools.wraps(function)
    def wrapper(self, value):
        try:
            function(self, value)
        except KeyError as err:
            raise InvalidOption('Invalid {}: {}'.format(
                function.__name__, str(err)))
    return wrapper


class TextStyle(object):
    """
    Create a text style
    The keyword arguments fg, bg, opt can be used to initiallize the style.
    The foreground and background colors can be then changed and options
    can be added later.

    Note: The bg, fg, opt methods return the style instance, to enable
    method chaining.

    Valid colors:
        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
    Valid options:
        'bold', 'faint', 'italic', 'undeline',
        'blink', 'blink_fast', 'negative',
        'conceal', 'strikeout'.
    """
    RESET = _TEMPLATE % '0'

    def __init__(self, fg=None, bg=None, opt=None, **kwargs):
        self._code_list = list()
        if fg:
            self.fg(fg)
        if bg:
            self.bg(bg)
        if opt:
            self.opt(opt)

    @_try_key
    def fg(self, value):
        """
        Add a foreground color.
        """
        self._code_list.append(_FOREGROUND[value])
        return self

    @_try_key
    def bg(self, value):
        """
        Add a background color.
        """
        self._code_list.append(_BACKGROUND[value])
        return self

    @_try_key
    def opt(self, value):
        """
        Add (an) option(s).
        value can be an itterable or a single string.
        """
        for opt in _get_iterable(value):
            self._add_opt(opt)
        return self

    def _add_opt(self, opt):
        """
        Helper to add option, taking into account negated options
        """
        if opt[0] == '!':
            self._code_list.append(_opt_reverse(_OPT_DICT[opt[1:]]))
        else:
            self._code_list.append(_OPT_DICT[opt])

    def __call__(self):
        """ See: compile """
        return self.compile()

    def __str__(self):
        """ See: compile """
        return self.compile()

    def compile(self):
        """
        Get the compiled ANSI espace sequence as a string.
        """
        return _TEMPLATE % (';'.join(str(code) for code in self._code_list))
