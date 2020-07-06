---
title: Python In Unity
category: [Dev]
tag: unity, python
---

문득, 갑자기 유니티에다 Python을 내장시켜보고 싶었다.

유니티의 스크립팅 언어가 C#이다보니 C#에서 굴러가는 파이썬3 구현체가 있을 것이라고 생각 했다. 찾아봤더니 역시 [IronPython](https://ironpython.net/)이라는게 툭 튀어나왔다.

하지만 IronPython2(즉, Python2) 밖에 나오지 않았고 역시 적절한 Python3를 너무나 좋아하는 나로서는 Python3 구현체를 찾기로 했다. 하지만 Python3 구현체로 보이는 [IronPython3](https://github.com/IronLanguages/ironpython3)는 아직 사용하지 말라고 권고를 하니 말을 잘 들어보자는 생각으로 IronPython2를 다운로드 받아 내장시켰다.

그런데, IronPython2를 깃헙에서 받아 dll을 내장시켜봤는데 뭔가 약간 이상한 에러가 뜨는 것이다. 다운로드 받은 IronPython2가 .Net 4.5, .Net 4.0, NetCore2.0 등 다양한 버전이 있길래 모두 내장시켜봤는데도 작동을 안하는 것이다. 그래서 [Unity-Python](https://github.com/exodrifter/unity-python)이라는 사람의 유니티 패키지의 IronPython으로 사용했는데 이건 또 이상하게 작동이 잘된다;;

어우 대체 내가 뭘 이상하게 한거지; 스ㅡ읍;