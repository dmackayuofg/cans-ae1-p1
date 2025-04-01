from enum import Enum
import sys
from pathlib import Path

WW = False
V = False
VV = False
DBG = False

seenSources = {}
programFile=sys.argv[1]


def includeSource(src):
    programText = Path(src).read_text()
    programLines = programText.splitlines()
    for line in programLines:        
        if len(line)>0 and line[0] == '~':
            inc = line[1:]
            if not (inc in seenSources):
                includeSource(inc)
                seenSources[inc]=True
        else:
            print(line)

includeSource(programFile)