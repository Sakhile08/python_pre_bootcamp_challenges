def convert_c_to_f(c):
  fahrenheit = (5/9) * c + 32
  print(fahrenheit)

c = int(input("Enter a temperature in celsius: "))

convert_c_to_f(c) 

def convert_f_to_c(f):
  celsius = (f - 32) * 5 /9 
  print(celsius)

f = int(input("Enter a temperature in fahrenheit: "))

convert_f_to_c(f)