from enum import Enum

class MyEnum(Enum):
    KEY1 = 1
    KEY2 = 2
    KEY3 = 3

my_dict = {
    MyEnum.KEY1: "value1",
    MyEnum.KEY2: "value2",
    MyEnum.KEY3: "value3"
}

input_key = "KEY2"

# string to enum for dict lookup

# using try/catch
try:
    key_enum = MyEnum.__members__[input_key]
    value = my_dict[key_enum]
    print(value)
except KeyError:
    print(f"{input_key} is not a valid key in MyEnum or my_dict")


# without using try/catch
input_key = "key1"
key_enum = MyEnum.__members__.get(input_key, None)
if key_enum:
    value = my_dict[key_enum]
    print(value)
else:
    print(f"{input_key} is not a valid key in MyEnum or my_dict")
