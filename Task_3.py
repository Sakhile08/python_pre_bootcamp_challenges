def test_number65(x, y):
    if x == 65 or y == 65 or (x + y) == 65:
      return True
    else :
        return False

print(test_number65(65, 2))
print(test_number65(64, 1))
print(test_number65(6, 5))