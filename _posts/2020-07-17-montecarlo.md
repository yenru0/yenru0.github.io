---
title: 몬테카를로 방법
category: [Math]
tag: [python, numerical]
---

몬테 카를로 방법은 **난수를 이용해 함수의 값을 확률적으로 계산하는 방법**이다.

보통 원의 면적으로 구하는 것을 예시로 많이 든다. 나는 원의 면적을 통해 원주율 구하기로 해봤다.

$0 \leq x \leq 1,\,0 \leq y \leq 1$이 사이의 무작위적인 $(x,\,y)$를 표집하고
$x^2+y^2 \leq 1$을 만족하는 모든 $(x,\,y)$의 개수를 세면 된다.
이때 위를 만족하는 $(x,\,y)$의 개수와 전체 개수의 비율은 원의 면적에 가까울 것이다.
여기에 4를 곱해주면 원주율 $\pi$가 나온다.

이를 python code로 구현해보면 다음과 같다.

```python
import random

total = int(input()) # 전체 개수
count = 0     # 조건을 만족하는 개수

for x, y in [(random.random(), random.random()) for i in range(total)]:
    if x**2 + y**2 <= 1:
        count += 1
        
print(4*count/total)
```

위 코드를 `total=10`, `total=100`, `total=1000`, `total=10000`, `total=100000`, `total=1000000`일 때 각각 실행시켰다.
```python
# total=10
3.6
# total=100
3.0
# total=1000
3.124
# total=10000
3.132
# total=100000
3.14796
# total=1000000
3.140364
# real pi
3.141592653589793
```
표본의 개수가 많을수록 값에 근접하는 경향을 보인다.
