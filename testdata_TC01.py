#_*_ coding: utf-8 -*-

#TestData=[(Test Data 01),(Test Data 02)....]
import pytest

def func1():    
    pass

def func2():
    ""
    pass

def func3():#Doc String Length 50
    "12345678912345678912345678912345678912345678912345"
    pass

def func4():#Doc String Length 51
    "123456789123456789123456789123456789123456789123456"
    pass

TestData = [pytest.param(func1,False,id='TD01 Doc String None'),
            pytest.param(func2,False,id='TD02 Doc String len 0'),
            pytest.param(func3,False,id='TD04 Doc String len 50'),
            pytest.param(func4,True,id='TD05 Doc String len 51')]