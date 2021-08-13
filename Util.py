# -*-coding:UTF-8 -*-
import os,uuid,threading

from colorama import init
import datetime
import json


# class

class Logger():
    def __init__(self):
        init(autoreset=True)
        self.OKGREEN = '\033[32m'
        self.ERRRED = '\033[31m'
        self.WARNYELLOW = '\33[33m'
        self.PreLog = "[{0}:{1}:{2}] [{3}]{4}"
        self.logs = []

    def info(self, t):
        msg_info = str("[{0}/{ thread }] [{1}]{2}".format(str(datetime.datetime.now()), "INFO", t, thread=threading.current_thread().name))
        print(self.OKGREEN + msg_info)
        self.logs.append(msg_info)

    def warn(self, t):
        msg_warn = str("[{0}/{ thread }] [{1}]{2}".format(str(datetime.datetime.now()), "WARN", t, thread=threading.current_thread().name))
        print(self.WARNYELLOW + msg_warn)
        self.logs.append(msg_warn)

    def error(self, t):
        msg_error = str("[{0}/{ thread }] [{1}]{2}".format(str(datetime.datetime.now()), "ERROR", t, thread=threading.current_thread().name))
        print(self.ERRRED + msg_error)
        self.logs.append(msg_error)

    def testMode(self):
        self.info("HI my is info")
        self.warn("HI my is warn")
        self.error("HI my is error")
        print("HI my is List -> %s" % self.logs)


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


# functions
def gradient_color(color_list, color_sum=700):
    """ 给定颜色List，输出渐变色 """
    color_center_count = len(color_list)
    color_sub_count = int(color_sum / (color_center_count - 1))
    color_index_start = 0
    color_map = []
    for color_index_end in range(1, color_center_count):
        color_rgb_start = color_list[color_index_start]
        color_rgb_end = color_list[color_index_end]
        r_step = (color_rgb_end[0] - color_rgb_start[0]) / color_sub_count
        g_step = (color_rgb_end[1] - color_rgb_start[1]) / color_sub_count
        b_step = (color_rgb_end[2] - color_rgb_start[2]) / color_sub_count
        # 生成中间渐变色
        now_color = color_rgb_start
        color_map.append(now_color)
        for color_index in range(1, color_sub_count):
            now_color = [now_color[0] + r_step, now_color[1] + g_step, now_color[2] + b_step]
            color_map.append(now_color)
        color_index_start = color_index_end
    return color_map


def rePlaceAlphaImg(window, img, pos, step):
    for i in range(0, 256, step):
        img.set_alpha(i)
        window.blit(img, pos)
def getUUID(name):
    return uuid.uuid5(uuid.NAMESPACE_DNS, name)