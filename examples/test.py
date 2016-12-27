from easycolor.parser import ColorParser
parser = ColorParser()
INFO = parser.parse("[<f:cyan>INFO</f>]<o:bold>{}")
print(INFO.format('Some info..'))
