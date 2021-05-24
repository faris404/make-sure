# makesure

>  _Simple validation for input datas_

## Installation
```sh
pip install makesure
```
## Usage
Create a schema that defines your data and call the function `make_sure(your_schema,input_data)`
if any validation fails it will raise an exception `MakeSureException` otherwise it return the data.

## Schemas
A schema is a dict that defines your data.

|Keys|Description|
| ------ | ------ |
| required | key must be in data and cannot be None |
| min | value grater than or equal to min |
| max | value less than or equal to max |
| min_len | len of value less than or equal to min_len|
| max_len | len of value less than or equal to max_len |
| regx | value must satisfy this reguler expressions |
| type | data types such as int, str, list, dict, tuple |

#### sample schema
```py
user_schema = {
    'name':{
        'required':True,
        'type':str
    },
    'email':{
        'type':str,
        'required':True,
        'regx':Regx.email
    },
    'age':{
        'type':int,
        'min':18
    }
}
```


## Some Useful Regx
```py
from makesure import Regx
```
|Regx|Description|
| ------ | ------ |
| Regx.email | email regx |
| Regx.aplha | only alphabets |
| Regx.number | only numbers |
| Regx.alphanum | alphanumerics string |
## Example
```py
# app.py
from makesure import make_sure, Regx, MakeSureException

user_schema = {
    'name':{
        'required':True,
        'type':str,
    },
    'age':{
        'type':int,
        'min':18
    },
    'email':{
        'regx':Regx.email
    }
}

data = {
    'name':'Your Name',
    'age':12,
    'email':'asdasd'
}

try:
    result = make_sure(user_schema,data)
    print(result)
except MakeSureException as e:
    print(e)

```

## License

MIT
