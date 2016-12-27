from easycolor.style import wrap as _w
from easycolor.style import make_style, RESET

# wrap text, appends a style-reset
print(_w('yellow on red', fg='yellow', bg='red'))
print('normal text')

# NOTE: for complex formatting use the parser module

# define some styles
black_on_white = make_style(fg='black', bg='white')
# we have to reset the background here
red_bold = make_style(fg='red', bg='reset', opt='bold')
# An options reset is only possible with a total reset
# we can however negate an option to remove it('!option').
green_bold_underline = make_style(fg='green', opt=('!bold', 'underline'))

print(black_on_white + 'Black on white' + red_bold + 'Red bold' +
      green_bold_underline + 'Green not bold underline' + RESET)

# everything was reset
print('normal text')
