#_*_ coding: utf-8 _*_

def check_doc_string_len()->'Returns function object which checks doc string length':
    '''This function checks if given fucntion has doc string with more than 50 charactors
    Inputs:
        No inputs
    Returns:
        Function object which checks doc string length'''

    doc_str_len_thd=51

    def inner_check_len(fnc:'Function Object')->'Returns true if doc string len > 50':
        '''This function checks if given fucntion has doc string with more than 50 charactors
        Inputs:
            Function object
        Returns:
            True if doc string has more than 50 charactors, otherwise false'''
        doc_str=fnc.__doc__
        if doc_str == None or (len(doc_str)<doc_str_len_thd):
            return False
        else:
            return True
    return inner_check_len

def fibo()->'Returns function object to send next fibonacci value':
    '''This generates fibonacci numbers
    Inputs:
        No inputs
    Returns:
        Function object which gives next fibonacci number'''

    fib_list=[]
    def next_fibo()->'Returns Next fibonacci number':
        nonlocal fib_list
        if len(fib_list)==0:
            fib_list.append(0)
        elif len(fib_list)==1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
        return fib_list[-1]
    return next_fibo

def add(a,b):
    '''returns sum of two variable'''
    return a+b

def mul(a,b):
    '''returns product of two variable'''
    return a*b

def div(a,b):
    '''returns division of two variable'''
    return a/b

fnc_tracker_dict = {}
def fnc_tracker(fnc):
    '''This function keeps track of function called
    Inputs:
        Function object
    Returns:
        Function object'''
    if not callable(fnc):
        raise TypeError(f"{fnc} is not callable")

    global fnc_tracker_dict
    fnc_tracker_dict[fnc.__name__]=0

    def inner_fnc_tracker(*args,**kwargs):
        global fnc_tracker_dict
        if len(args):
            fnc_tracker_dict[fnc.__name__]+=1
            return fnc(*args,**kwargs)
        else:
            fnccalls=''
            for fnc_name,call_count in fnc_tracker_dict.items():
                fnccalls=fnccalls+' '+f'{fnc_name} called {call_count} times,'
            return fnccalls.lstrip()        
    return inner_fnc_tracker

def multiuser_fnc_tracker(fnc,user_dict):
    '''This function keeps track of function called
    Inputs:
        Function object
    Returns:
        Function object'''
    if not callable(fnc):
        raise TypeError(f"{fnc} is not callable")
    user_dict[fnc.__name__]=0

    def inner_fnc_tracker(*args,**kwargs):
        nonlocal user_dict
        if len(args):       
            user_dict[fnc.__name__]+=1
            return fnc(*args,**kwargs)
        else:
            fnccalls=''
            for fnc_name,call_count in user_dict.items():
                if fnc_name=='User':
                    fnccalls=f'{fnc_name}:{call_count}, '
                else:
                    fnccalls=fnccalls+(f'{fnc_name} called {call_count} times, ')
            return fnccalls.rstrip()        
    return inner_fnc_tracker