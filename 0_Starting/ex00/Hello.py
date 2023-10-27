ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# replace "tata!" by "World!" in ft_list
ft_list[1] = "World!"

# replace "toto!" by "France!" in ft_tuple
replace = list(ft_tuple)
replace[1] = "France!"
ft_tuple = tuple(replace)

# replace "tutu!" by "Paris!" in ft_set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# replace "titi!" by "42Paris!" in ft_dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
