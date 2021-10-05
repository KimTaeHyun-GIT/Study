# 방법 1
print("나는 %d살입니다."%19)
print("나는 %s을 좋아해요."%"파이썬")
print("Python 은 %c로 시작해요." % "P")

# 방법 2
print("나는 {}살입니다. ".format(201391))
print("나는 {}과 {}을 좋아해요".format("코딩","파이썬"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="검은"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print("나는 {age}살이며, {color}색을 좋아해요.")