def test_number3(x, y):
    if x == 3 or y == 3 and (x + y) == 3:
      return True
    else :
        return False

print(test_number3(0, 3))
print(test_number3(1, 2))
print(test_number3(3, 5))