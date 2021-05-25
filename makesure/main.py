import re

#   some importend regxs 
class Regx:
    alphanum = r'^[A-Za-z0-9]+$'
    number = r'^[0-9]+$'
    alpha = r'^[A-Za-z]+$'
    email = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'



#   custom exception
class MakeSureException(Exception):
    pass


#   error functions
def _min_er(key,val):
    return f"{key} must be grater than {val}"

def _max_er(key,val):
    return f"{key} must be less than {val}"


def data_type_er(key,val):
    return f"{key} must be type of {val}"

def max_len_er(key,val):
    return f"{key} length must be less than {val}"

def min_len_er(key,val):
    return f"{key} length must be grater than {val}"

def regx_er(key,_):
    return f"{key} does not match with the regx"

def enum_er(key,val):
    return f"{key} must be in {val}"


#   validation functions

def _min(arg,val):
    return val >= arg

def _max(arg,val):
    return val <= arg

def data_type(arg,val):
    return arg==type(val)

def max_len(arg,val):
    return arg >= len(val)

def min_len(arg,val):
    return arg <= len(val)

def regx(arg,val):
    if re.match(arg,val):
        return True
    return False

def enum(arg,val):
    if type(arg)==set or type(arg)==list or type(arg)==tuple:
        return val in arg
    raise MakeSureException('enum must be iterable')
#   validation function dict
functions = {
    'min':_min,
    'max':_max,
    'type':data_type,
    'max_len':max_len,
    'min_len':min_len,
    'regx':regx,
    'enum':enum
}

#   error function dict
error_func = {
    'min':_min_er,
    'max':_max_er,
    'type':data_type_er,
    'max_len':max_len_er,
    'min_len':min_len_er,
    'regx':regx_er,
    'enum':enum_er
}


#   function to validate single item
def validate(key,val,opt,msg):
    res={}
    for func in opt:
        try:

            status = functions[func](opt[func],val)
        except KeyError:
            raise MakeSureException(f'invalid key {func}')
        if not status:
            if msg:
                raise MakeSureException(msg)
            raise MakeSureException(error_func[func](key,opt[func]))
    res[key]=val
    return res


#   function to validate all item
def make_sure(schema,data):
    args = {}
    for i in schema.keys():
        res = {}
        opt = schema[i]
        msg = None
        if opt.get('msg'):
            msg = opt.get('msg')
            del opt['msg']
        if opt.get('required'):
            if data.get(i):
                del opt['required']
                res = validate(i,data.get(i),opt,msg)
            else:
                if msg:
                   raise MakeSureException(msg) 
                raise MakeSureException(f'{i} is required')
        else:
            if data.get(i):
                res = validate(i,data.get(i),opt,msg)
        if res:
            args.update(res)

    return args
