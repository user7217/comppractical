#return max face value in units place
def max_face_value(num1, num2):
    return num1 if num1%10 > num2%10 else num2
result = max_face_value(123,456)
print(result)