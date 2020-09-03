# -*- coding:utf-8 -*-
#@Time : 2020/9/3 9:55 上午
#@Author: cywaht
#@File : xiaowang.py
import pytest
from test_xiaowang import shell

shell = shell.Shell()

if __name__ == '__main__':

    try:
        print("开始执行脚本")
        pytest.main(['-v', './test_xiaowang/', "--alluredir", "./reports/json/"])
        print("脚本执行完成")
    except Exception as e:
        print("脚本批量执行失败！", e)

    try:
        cmd = 'allure generate %s -o %s --clean' % (' ./reports/json/', ' ./reports/html/')
        print("开始执行报告生成")
        shell.invoke(cmd)
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        raise