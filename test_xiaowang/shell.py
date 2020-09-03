# -*- coding:utf-8 -*-
#@Time : 2020/7/9 4:57 下午
#@Author: cywaht
#@File : shell.py
import subprocess
import allure

class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o