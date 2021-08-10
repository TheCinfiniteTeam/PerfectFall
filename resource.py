#-*-coding:UTF-8 -*-
import json

class Resource():
    def __init__(self, runDir):
        self.runDir = runDir
        with open(file="%s/resource/assets.json" % self.runDir, encoding="utf-8") as assetsFD:
            assetsRAW = assetsFD.read()
        self.assets = json.loads(assetsRAW)

    def getPath(self, type, name):
        return '%s/resource/%s/%s.%s' % (
            self.runDir,
            self.assets[type][name]['path'],
            self.assets[type][name]['name'],
            self.assets[type][name]['type']
        )