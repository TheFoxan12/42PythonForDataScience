from in_out import outer
from in_out import square
from in_out import ft_pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())

print("---")
another_counter = outer(1.5, ft_pow)
print(another_counter())
print(another_counter())
print(another_counter())
