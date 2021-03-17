---
title: 병적인 함수
category: [Math]
tag: []
---

바이어 슈트라스 함수에 대해 찾아보던 중 **병적인(pathological) 함수**라는 말을 처음 들어보았다. 함수가 아플리는 전혀 없기 때문에 이 병적인 것에 대해 매우 궁금했다.

**병적인 함수**는 한마디로 말해 일반적이지 않은 함수이다. 그리고 이 병적인 함수의 반대되는 용어는 **well-behaved 함수**라고 한다.

사실 이것의 정확한 정의는 있을거 같기도 않지만 정확히 모르겠다.

어쨋든 이 병적인 함수의 예시는 대표적으로 모든 점에서 연속이나 미분 불가능한 함수 바이어 슈트라스 함수, 디리클레 함수 등이 있다.

# 바이어슈트라스 함수

모든 점에서 연속이나 모든 점에서 미분 불가능한 특이한 함수이다.

$$f(x)=\sum^{\infty}_{n=0}{a^n cos(b^n \pi x)}\quad (0 < a < 1,\,ab\geq1)$$

# 디리클레 함수

모든 점에서 불연속인 함수로 정의는 다음과 같다.

$$\mathbf{1} _{\mathbb{Q}}=\begin{cases}1 && x \in Q \\ 0 && x \notin Q \end{cases}$$

# 토메 함수

유리수에서는 불연속이고, 무리수에서는 연속이며, 모든 점에서 미분 불가능하고 리만 적분은 가능한 함수이다.

$$f(x)=\begin{cases}0 && x \notin Q \\ 1 && x = 0 \\ 1/q && x = \frac{p}{q},\, \text{gcd}(p, q) = 1,\, q > 0  \end{cases}$$

이외에도 많은 병적 함수가 있다.