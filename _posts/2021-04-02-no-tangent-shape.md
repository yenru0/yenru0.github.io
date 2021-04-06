---
title: 접선이 만들지 못하는 도형
category: [Math]
tag: []
---

> 원의 모든 접선은 원 내부의 어떠한 점도 지나지 않는다.

사실 이 사실은 직관적으로 맞다는 것을 잘 알 수 있다. 그림을 보면 알 수 있다.

![fig1](/assets/img/2021-04-02-no-tangent-shape-fig-1.png)
![fig2](/assets/img/2021-04-02-no-tangent-shape-fig-2.png)
![fig3](/assets/img/2021-04-02-no-tangent-shape-fig-3.png)

이는 비단 원 뿐만이 아니라 타원에서 성립한다.

![fig11](/assets/img/2021-04-02-no-tangent-shape-fig-11.png)
![fig12](/assets/img/2021-04-02-no-tangent-shape-fig-12.png)
![fig13](/assets/img/2021-04-02-no-tangent-shape-fig-13.png)

하지만 이것이 모든 점에서 접선이 존재하는 폐곡선에서 성립하지는 않는다는 걸 이 반례를 통해서 쉽게 알 수 있다.

$$x(t) = 2\sin{t} + \cos{t},\quad y(t)=2\cos(t)-\sin(2t)$$

![fig20](/assets/img/2021-04-02-no-tangent-shape-fig-20.png)

이 곡선이 왜 안되는지는 좀 그려보면 안다.

![fig21](/assets/img/2021-04-02-no-tangent-shape-fig-21.png)
![fig22](/assets/img/2021-04-02-no-tangent-shape-fig-22.png)
![fig23](/assets/img/2021-04-02-no-tangent-shape-fig-23.png)

왜 이럴까? 나도 모르겠다.

좀 물어보니까 이것의 증명은 귀류법을 하면될 것 같기도 하다.

그리고 이걸 확장시켜 볼록한 닫힌 도형에서는 그 접선이 내부를 관통하지 못한다고 추측할 수 있을 것 같다.

좀 함수적으로 생각해보면 모든 $x\in \mathbb{R}$에 대해$f''(x) > 0$ 혹은 $f''(x) < 0$이 성립하면 그 함수 내부점은 관통하지 못한다 할 수 있지 않을까?