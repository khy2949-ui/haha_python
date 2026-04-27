# import calc as c  (from calc import * 보다 이 방식이 좋다.)
# import calc 는 calc.py 전체 사용

# 특정 함수나 변수를 사용하고자 한다면 아래와같이 하면된다.
from calc import add

print(add(10,20))