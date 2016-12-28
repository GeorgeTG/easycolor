# Copyright George T. Gougoudis 2016. BSD 3-Clause license; see LICENSE file.
import sys
from .style import make_style, RESET
if sys.version_info.major >= 3:
    from html.parser import HTMLParser
else:
    from HTMLParser import HTMLParser


class ColorParser(HTMLParser, object):
    """ A Parser that supports html-like syntax
    to add advanced style to your text.

    The syntax is as follows:

    Open tag: <f:color,b:color,o:option,o:option....>
    All text in the tag will have the configured
    style applied to it, unless a nested tag overrides it.

    Close tag: </f,b,o:option,o:option...>
    Note: options must be explicitly closed.
    """

    def __init__(self, *args, **kwargs):
        super(ColorParser, self).__init__(*args, **kwargs)

    def reset(self):
        self.result = ''
        self.fg = list()
        self.bg = list()
        self.opt = list()
        super(ColorParser, self).reset()

    def add_sequence(self):
        fg = self.fg[-1] if self.fg else None
        bg = self.bg[-1] if self.bg else None
        opt = self.opt if self.opt else ()
        self.result += make_style(fg=fg, bg=bg, opt=opt)

    def handle_starttag(self, tag, attrs):
        # Tag example: <f:color,b:color,o:opt,o:opt>
        tags = ''.join(tag.split()).split(',')  # remove all whitespace
        for current in tags:
            try:
                k, v = current.split(':')
            except ValueError:
                raise ValueError('Bad tag at {}: {}'.format(
                    self.getpos(),
                    self.get_starttag_text()))
            if k == 'f':
                self.fg.append(v)
            elif k == 'b':
                self.bg.append(v)
            elif k == 'o':
                self.opt.append(v)

        # add a format sequence with the current options
        self.add_sequence()

    def handle_endtag(self, tag):
        # End-Tag example: </f,b,o:opt,o:opt>
        tags = ''.join(tag.split()).split(',')  # remove all whitespace
        try:
            for k in tags:
                if k == 'f':
                    if len(self.fg) == 1:
                        self.fg.pop()
                        self.result += make_style(fg='reset')
                    elif len(self.fg) >= 2:
                        self.fg.pop()   # delete the last one
                        # restore previous style
                        self.result += make_style(fg=self.fg[-1])
                    else:
                        raise ValueError(k)
                elif k == 'b':
                    if len(self.bg) == 1:
                        self.bg.pop()
                        self.result += make_style(bg='reset')
                    elif len(self.bg) >= 2:
                        self.bg.pop()   # delete the last one
                        # restore previous style
                        self.result += make_style(bg=self.bg[-1])
                    else:
                        raise ValueError(k)
                elif k.startswith('o'):
                    opt = k.split(':')[1]
                    # reverse - remove - reverse
                    self.opt.reverse()
                    # NOTE: this is done beforehand to throw
                    # if an invalid option is used, instead of
                    # recognising the option as stray
                    style = make_style(opt=('!' + opt))
                    try:
                        self.opt.remove(opt)
                        # add negated option
                        self.result += style
                    except ValueError:
                        raise ValueError(opt)
                    finally:
                        self.opt.reverse()
        except ValueError as err:
            print('WARN: Stray end-tag "{}" at {}'.format(
                str(err),
                str(self.getpos())))

    def handle_data(self, data):
        self.result += data

    def parse(self, data):
        """
        Parse a string that contains formatting.
        Automatically appends a RESET at the end.
        The parser resets everytime this method is called.
        """
        self.reset()
        self.feed(data)
        return self.result + RESET

    def cprint(self, data):
        """
        A wrapper around parse, to print text
        """
        print(self.parse(data))
