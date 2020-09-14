# -*- coding: utf-8 -*-
import pytest
import string
import inspect
import re
import session8 as session_ut
import math
import sys
import os.path

def test_TC00_01_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session_ut)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_TC00_02_function_name_had_cap_letter():
    functions = inspect.getmembers(session_ut, inspect.isfunction)
    for function in functions:  
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_TC00_02_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_TC00_03readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_TC01_01_check_doc_string_len_closure_used():
    func_TC01_01 = session_ut.check_doc_string_len()
    assert func_TC01_01.__closure__ != None, f'You need to use closure'

from testdata_TC01 import TestData as TestData_TC01
@pytest.mark.parametrize("Fnc,expected",TestData_TC01)
def test_TC01_02_check_doc_string_len(Fnc,expected):
    func_TC01_02 = session_ut.check_doc_string_len()
    assert func_TC01_02(Fnc) == expected, f'Doc String Check function Check failed!'

def test_TC02_01_fibonacci_closure_used():
    func_TC02_01 = session_ut.fibo()
    assert func_TC02_01.__closure__ != None, f'You need to use closure'

def test_TC02_02_fibonacci():
    func_TC02_02 = session_ut.fibo()
    TC02_02_result =[]
    for i in range(10):
        TC02_02_result.append(func_TC02_02())
    assert TC02_02_result == [0,1,1,2,3,5,8,13,21,34],f'Fibonacci series {TC02_02_result} is not correct!'

def test_TC03_01_func_call_count_closure_used():
    func_TC03_01 = session_ut.fnc_tracker(session_ut.add)
    assert func_TC03_01.__closure__ != None, f'You need to use closure'

def test_TC03_02_func_call_count_check_counter_init():
    func_TC03_02_add = session_ut.fnc_tracker(session_ut.add)
    assert func_TC03_02_add()=='add called 0 times,'
    assert func_TC03_02_add()=='add called 0 times,'

def test_TC03_03_func_call_count_check_counter_init_all_fnc():
    func_TC03_03_add = session_ut.fnc_tracker(session_ut.add)
    func_TC03_03_mul = session_ut.fnc_tracker(session_ut.mul)
    func_TC03_03_div = session_ut.fnc_tracker(session_ut.div)
    assert func_TC03_03_add()=='add called 0 times, mul called 0 times, div called 0 times,'
    assert func_TC03_03_mul()=='add called 0 times, mul called 0 times, div called 0 times,'
    assert func_TC03_03_div()=='add called 0 times, mul called 0 times, div called 0 times,'

def test_TC03_04_func_call_count_test_fnc_count():
    func_TC03_04_add = session_ut.fnc_tracker(session_ut.add)
    func_TC03_04_mul = session_ut.fnc_tracker(session_ut.mul)
    func_TC03_04_div = session_ut.fnc_tracker(session_ut.div)
    assert func_TC03_04_add(1,2)==3
    assert func_TC03_04_add()=='add called 1 times, mul called 0 times, div called 0 times,'
    assert func_TC03_04_mul()=='add called 1 times, mul called 0 times, div called 0 times,'
    assert func_TC03_04_div()=='add called 1 times, mul called 0 times, div called 0 times,'

    assert func_TC03_04_mul(-1,2)==-2
    assert func_TC03_04_add()=='add called 1 times, mul called 1 times, div called 0 times,'
    assert func_TC03_04_mul()=='add called 1 times, mul called 1 times, div called 0 times,'
    assert func_TC03_04_div()=='add called 1 times, mul called 1 times, div called 0 times,'

    assert func_TC03_04_div(4,2)==2
    assert func_TC03_04_add()=='add called 1 times, mul called 1 times, div called 1 times,'
    assert func_TC03_04_mul()=='add called 1 times, mul called 1 times, div called 1 times,'
    assert func_TC03_04_div()=='add called 1 times, mul called 1 times, div called 1 times,'

    assert func_TC03_04_add(-1,2)==1
    assert func_TC03_04_add()=='add called 2 times, mul called 1 times, div called 1 times,'
    assert func_TC03_04_mul()=='add called 2 times, mul called 1 times, div called 1 times,'
    assert func_TC03_04_div()=='add called 2 times, mul called 1 times, div called 1 times,'

    assert func_TC03_04_mul(-8,6)==-48
    assert func_TC03_04_add()=='add called 2 times, mul called 2 times, div called 1 times,'
    assert func_TC03_04_mul()=='add called 2 times, mul called 2 times, div called 1 times,'
    assert func_TC03_04_div()=='add called 2 times, mul called 2 times, div called 1 times,'

    assert func_TC03_04_div(-8,2)==-4
    assert func_TC03_04_add()=='add called 2 times, mul called 2 times, div called 2 times,'
    assert func_TC03_04_mul()=='add called 2 times, mul called 2 times, div called 2 times,'
    assert func_TC03_04_div()=='add called 2 times, mul called 2 times, div called 2 times,'

def test_TC04_01_multiuser_func_call_count_closure_used():
    User1_dict={'User':1}
    func_TC04_01 = session_ut.multiuser_fnc_tracker(session_ut.add,User1_dict)
    assert func_TC04_01.__closure__ != None, f'You need to use closure'

def test_TC04_02_multiuserfunc_call_count_check_counter_init():
    User1_dict={'User':1}
    User2_dict={'User':2}
    func_TC04_02_add1 = session_ut.multiuser_fnc_tracker(session_ut.add,User1_dict)
    assert User1_dict=={'User':1,'add':0}
    assert User2_dict=={'User':2}
    func_TC04_02_mul2 = session_ut.multiuser_fnc_tracker(session_ut.mul,User2_dict)
    assert User1_dict=={'User':1,'add':0}
    assert User2_dict=={'User':2,'mul':0}

def test_TC04_03_multiuserfunc_call_count_check_counter_init_all_fnc_user1():
    User1_dict={'User':1}
    User2_dict={'User':2}
    func_TC04_03_add1 = session_ut.multiuser_fnc_tracker(session_ut.add,User1_dict)
    func_TC04_03_mul1 = session_ut.multiuser_fnc_tracker(session_ut.mul,User1_dict)
    func_TC04_03_div1 = session_ut.multiuser_fnc_tracker(session_ut.div,User1_dict)
    assert User1_dict=={'User':1,'add':0,'mul':0,'div':0}
    assert User2_dict=={'User':2}

def test_TC04_04_multiuserfunc_call_count_check_counter_init_all_fnc_user2():
    User1_dict={'User':1}
    User2_dict={'User':2}
    func_TC04_04_add2 = session_ut.multiuser_fnc_tracker(session_ut.add,User2_dict)
    func_TC04_04_mul2 = session_ut.multiuser_fnc_tracker(session_ut.mul,User2_dict)
    func_TC04_04_div2 = session_ut.multiuser_fnc_tracker(session_ut.div,User2_dict)
    assert User2_dict=={'User':2,'add':0,'mul':0,'div':0}
    assert User1_dict=={'User':1}

def test_TC04_05_multiuserfunc_call_count_test_fnc_count():
    User1_dict={'User':1}
    User2_dict={'User':2}
    func_TC04_05_add1 = session_ut.multiuser_fnc_tracker(session_ut.add,User1_dict)
    func_TC04_05_mul1 = session_ut.multiuser_fnc_tracker(session_ut.mul,User1_dict)
    func_TC04_05_div1 = session_ut.multiuser_fnc_tracker(session_ut.div,User1_dict)
    func_TC04_05_add2 = session_ut.multiuser_fnc_tracker(session_ut.add,User2_dict)
    func_TC04_05_mul2 = session_ut.multiuser_fnc_tracker(session_ut.mul,User2_dict)
    func_TC04_05_div2 = session_ut.multiuser_fnc_tracker(session_ut.div,User2_dict)
    assert User1_dict=={'User':1,'add':0,'mul':0,'div':0}
    assert User2_dict=={'User':2,'add':0,'mul':0,'div':0}

    assert func_TC04_05_add1(1,2)==3
    assert User1_dict=={'User':1,'add':1,'mul':0,'div':0}
    assert User2_dict=={'User':2,'add':0,'mul':0,'div':0}

    assert func_TC04_05_add2(-1,-2)==-3
    assert User1_dict=={'User':1,'add':1,'mul':0,'div':0}
    assert User2_dict=={'User':2,'add':1,'mul':0,'div':0}

    assert func_TC04_05_mul1(8,2)==16
    assert User1_dict=={'User':1,'add':1,'mul':1,'div':0}
    assert User2_dict=={'User':2,'add':1,'mul':0,'div':0}

    assert func_TC04_05_mul2(-8,-5)==40
    assert User1_dict=={'User':1,'add':1,'mul':1,'div':0}
    assert User2_dict=={'User':2,'add':1,'mul':1,'div':0}

    assert func_TC04_05_div1(8,2)==4
    assert User1_dict=={'User':1,'add':1,'mul':1,'div':1}
    assert User2_dict=={'User':2,'add':1,'mul':1,'div':0}

    assert func_TC04_05_div2(40,10)==4
    assert User1_dict=={'User':1,'add':1,'mul':1,'div':1}
    assert User2_dict=={'User':2,'add':1,'mul':1,'div':1}
