# -*-coding:UTF-8 -*-
import os, uuid, threading

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
        self.__debugMode = False

    def info(self, t, safeLevel=10):
        msg_info = str(
            "[{0}/{3}] [{1}]{2}".format(str(datetime.datetime.now()), "INFO", t, threading.current_thread().name))
        print(self.OKGREEN + msg_info)
        self.logs.append(msg_info)
        return safeLevel

    def warn(self, t, safeLevel=5):
        msg_warn = str(
            "[{0}/{3}] [{1}]{2}".format(str(datetime.datetime.now()), "WARN", t, threading.current_thread().name))
        print(self.WARNYELLOW + msg_warn)
        self.logs.append(msg_warn)
        return safeLevel

    def error(self, t, safeLevel=-1):
        msg_error = str(
            "[{0}/{3}] [{1}]{2}".format(str(datetime.datetime.now()), "ERROR", t, threading.current_thread().name))
        print(self.ERRRED + msg_error)
        self.logs.append(msg_error)
        return safeLevel

    def callingLog(self, func):
        """函数调用时，触发装饰器，仅在调试模式可用"""

        def wrapper(*args, **kw):
            msg = "%s() was been called." % func.__name__
            log = "[{0}/{1}] [{2}] {3}".format(str(datetime.datetime.now()), "DEBUG", threading.current_thread().name,
                                               msg)
            print(log)
            self.logs.append(log)
            return func(*args, **kw)

        return wrapper

    def DebugMode(self):
        self.__debugMode = True
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
        self.logger = Logger()

    def getPath(self, type, name):
        try:
            path = '%s/resource/%s/%s' % (
                self.runDir,
                self.assets[type][name]['path'],
                self.assets[type][name]['name'],
            )
            return path
        except KeyError:
            self.logger.error("Can not find resource named {0}/{1}".format("type", "name"))
            return ""


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
