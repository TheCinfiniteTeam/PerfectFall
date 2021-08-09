#-*-coding:UTF-8 -*-
import json

class Resource():
    def __init__(self, runDir):
        self.runDir = runDir
        with open(file="%s/resource/REP.json" % self.runDir, encoding="utf-8") as REPFD:
            REPRAW = REPFD.read()
        self.REP = json.loads(REPRAW)

    def getPath(self, type, name):
        return '%s/resource/%s/%s.%s' % (
            self.runDir,
            self.REP[type][name]['path'],
            self.REP[type][name]['name'],
            self.REP[type][name]['type']
        )