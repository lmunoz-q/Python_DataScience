from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi"}
ft_str = "quarante deux"
ft_complex = 1j
ft_range = range(42)
ft_frozenset = ({"lulu", "dors", "et pete"})
ft_true = True
ft_false = False
ft_bytes = b"Hello"
ft_bytearray = bytearray(42)
ft_memoryview = (bytes(42))
ft_int = 42
ft_float = 42.42

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj(ft_str)
all_thing_is_obj("Brian")
all_thing_is_obj(ft_complex)
all_thing_is_obj(ft_range)
all_thing_is_obj(ft_frozenset)
all_thing_is_obj(ft_true)
all_thing_is_obj(ft_false)
all_thing_is_obj(ft_bytes)
all_thing_is_obj(ft_bytearray)
all_thing_is_obj(ft_memoryview)
all_thing_is_obj(ft_int)
all_thing_is_obj(ft_float)
print(all_thing_is_obj(10))
