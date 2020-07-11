---
title: Display Video In Jupyter
category: [Dev, python]
tag: python, jupyter
---

## 가장 빠른 방법
주피터에서 비디오를 보여주기 위해선 `IPython.display.Video`를 사용하는 것이 가장 빠르다. [*참조*](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html)

Video의 첫번째 매개 변수인 data에 raw data, url, file name을 넣어 사용할 수 있다. embed 매개 변수가 참일때에는 노트북에 data가 다 포함된다. 다만 raw data의 경우엔 매개 변수 embed가 참이어야만 한다.


```python
from IPython.display import Video

Video("./Video.mp4")
```

동영상을 그대로 이용하는 방법은 vs code, pycharm에서 볼 수 없다는 것이 단점이다. 

## png 파일들을 비디오같이 보는 방법(프레임 단위)
보통 `pygame.image.save`를 이용해 결과를 프레임마다 이미지로 저장하는데 그 결과를 프레임마다 보여주기 위해 다음과 같이 `ipywidgets`와 `IPython.display.Image`를 이용해 저장된 png파일들을 프레임단위로 보여준다. [*참조*](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

```python
from IPython
from ipywidgets import interact

x = widgets.IntSlider(min=0, max=100-1, step=1, value=0)
interact(lambda x: display(Image("image/{0}.png".format(x))), x=x)
```

다만 이 방법은 재시작을 하거나 다른 곳에서 열게되면 다시한번 리로드가 필요하다는 단점이 있고, vs code, pycharm에서 조금 끊긴다는 단점이 있다.


## 결론

둘 다 장단점이 확실한 방법이다.

보통 jupyter를 웹에서 실행하면 코드 자동완성이 부족하고, pycharm에서 실행하게 되면 비디오를 못보니까 이게 바로 균형의 수호자 아닐까;;

결국 둘다 병용해서 쓴다;;


