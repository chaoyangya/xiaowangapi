# -*- coding:utf-8 -*-
#@Time : 2020/9/3 9:56 上午
#@Author: cywaht
#@File : test_api.py
import pytest
import allure

@allure.feature('练习jenkins')
class TestApi:

    @allure.story('练习列表--修改练习')
    def test_add(self):
        a = 1
        b = 2
        c = a+b
        assert c == 3

    @pytest.mark.dependency(depends=['test_add'])
    @allure.story('练习列表--修改练习')
    def test_jian(self):
        a = 1
        b = 2
        c = b - a
        assert c == 1



if __name__ == '__main__':
    pytest.main(['-v', 'test_exercise.py::TestExerciseMent'])

