from easycolor.parser import ColorParser
parser = ColorParser()
cprint = parser.cprint

# Add rainbow colors!
cprint("""<f:red>r<f:yellow>ai<f:green>nb<f:blue>o<f:magenta>w"""
       """</f>o</f>bn</f>ia</f>r</f>""")
# complex foreground - background
cprint("""<f:red,b:yellow>red on yellow</b>just red<b:black>red on black!"""
       """<f:green>green on black</f>again red on black</f,b>normal""")

# with opts
cprint("""<o:bold,o:italic>bold and italic</o:bold> only italic""")

# Nice log messages
some_string = "spam"
some_int = 15
cprint("""<f:red,f:green>[</f>ERROR<f:green>]</f> Your eggs need some: """
       """<f:blue>{}</f>. Also this is a number </f><b:red>{}</b>""".format(
             some_string, some_int))

# lets make this re-usable
# we can leave a tag open, since a reset is automatically appended
WARN = parser.parse("[<f:yellow>WARN</f>]<f:yellow,o:bold> {}")
ERROR = parser.parse("[<f:red>ERROR</f>]<f:red,o:bold> {}")
INFO = parser.parse("[<f:cyan>INFO</f>] <o:bold>{}")

print(INFO.format('Some info..'))
print(WARN.format('You better be careful!'))
print(ERROR.format('Oh noes!'))
