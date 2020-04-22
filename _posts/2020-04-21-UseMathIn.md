---
title: MathJax와 TikzJax
category: etc
tags: [HTML, math]
tikzlink: /assets/tikzs/2020-04-21-UseMathIn.md
---

## MathJax로 수식 표현
`_includes`밑에 `mathjax_support.html`을 만든 뒤
`_layouts/default.html`에

```html
{% raw %}{% include mathjax_support.html %}{% endraw %}
```
를 추가해준다. 그 뒤 본문에다 `$...$`, `$$...$$`를 이용한다.

### example 1.

`$\sum_{k=1}^{n}{k} = \frac{n(n+1)}{2}$`

> $\sum_{k=1}^{n}{k} = \frac{n(n+1)}{2}$

### example 2.
```latex
$$
\sum_{k=1}^{n}{k} = \frac{n(n+1)}{2}
$$
```

$$
\sum_{k=1}^{n}{k} = \frac{n(n+1)}{2}
$$

## TikzJax로 그래프, 그림 표현
`_includes`밑에 `tikzjax_support.html`을 만든 뒤
`_layouts/default.html`에

```html
{% raw %}{% include tikzjax_support.html %}{% endraw %}
```

를 추가해주고, 본문에

```
<script type="text/tikz">
  ...
</script>
```

을 하여 tikz를 쓸 수 있다.

### example 1.
```latex
<script type="text/tikz">
  \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
</script>
```

### example 2.
```latex
<script type="text/tikz">
  \begin{tikzpicture}
    \draw[step=1cm,gray,very thin] (-1.9,-1.9) grid (5.9,5.9);
    \draw[thick,->] (0,0) -- (4.5,0);
    \draw[thick,->] (0,0) -- (0,4.5);
    \draw[thick,->] (0,0) -- (4.5,0) node[anchor=north west] {x axis};
    \draw[thick,->] (0,0) -- (0,4.5) node[anchor=south east] {y axis};
    \draw[domain=-1:5, samples=100] plot(\x,{sin(\x)} );
  \end{tikzpicture}
</script>
```

## 결론
이와 같은 일련의 과정을 통하여 `우리`는 수학을 웹사이트에서 마구 굴릴 수 있게 되었다.


## 현실
TikzJax가 `bundle exec jekyll serve`를 통한 로컬에선 잘 작동이 되어 `commit, push`를 하였다.
그러나 현실은 TikzJax가 잘 작동은 무슨 되지도 않았다.


### 문제 분석

먼저 `yenru0.github.io`에 들어간 뒤 F12를 눌렀더니 다음과 같은 오류를 보았다.
```
Mixed Content: The page at 'https://yenru0.github.io/etc/UseMathIn/' was loaded over HTTPS, but requested an insecure stylesheet 'http://tikzjax.com/v1/fonts.css'. This request has been blocked; the content must be served over HTTPS.
```
대충 HTTPS에서 HTTP를 로드한 것이 문제인 것 같았다.

그래서 `https://tikzjax.com/v1/tikzjax.js`를 찾고 싶었다. 그러나 그런 주소는 없었다.

## 해결(?)
애초에 그런 주소가 없으면 그냥 **생 코드**를 집어 넣으면 되지 않을까? 라는 미친 시도를 했다.

하지만 그런 생각과 이상과는 다르게 한번의 시도만에 털렸다.
솔직히 내가 javascript를 잘하는 것도 아니고 그런 노동을 할 시간도 없기 때문에 다른 방법을 모색해야했다.

## 생각
4시간 동안의 삽질을 계속 해보니 새로운 생각이 떠올랐다. 
'굳이 웹사이트에 tikz 코드 전문을 올릴 필요가 있을까?'
이렇게 생각해보니 커밋과 푸쉬 하기 전에 한번 마크다운을 읽고 svg파일을 만들면 되지 않을까? 라는 생각을 해보게 되었다.

이런 시도가 처음이었던 것은 아니다. 옛날에 박아둔 `sailview` 때도 tex를 이용해 이러한 시도를 했으니까 말이다.

### 재시도
새로운 파이썬 코드를 만들었다.
```python
# preload.py
from os import walk
from os.path import join, splitext
import re
import subprocess as sp

postDir = "_posts"

pattern_tikzs = re.compile(r"\$%%%tikzs\$((?:[\n]|.)*?)\$%%%tikzs\$")

CS = r"""\documentclass[dvisvgm]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{kotex}
\usepackage{tikz}
\usepackage{tkz-euclide}
\usepackage{pgfplots}
\usepackage{tikz-3dplot}
\pgfplotsset{compat=1.9}
\thispagestyle{empty}
\begin{document}
%s
\end{document}
"""


for path, dirs, files in walk(postDir):
    for file in files:
        temp_str = ""
        with open(join(path, file), "r", encoding="utf-8") as f:
            temp_str = f.read()

        temp_tikzs = pattern_tikzs.findall(temp_str)
        for i, ttkzs in enumerate( temp_tikzs):
            with open(join("assets\\tikzs", file + "." + str(i) + ".tex"), "w", encoding="utf-8") as f:
                f.write(CS%ttkzs)
            op = sp.call(
                "xelatex --no-pdf --output-directory={0} --interaction=nonstopmode --halt-on-error {1}".format(r"./assets/tikzs/", r"./assets/tikzs/" + file + "." + str(i) + ".tex")
            )
            print(join(".\\assets\\tikzs", file + "." + str(i) + ".tex"))
            if op == 1:
                continue

            temp_dvifname = join("assets\\tikzs", file + "." + str(i) + ".xdv")
            temp_svgfname = join("assets\\tikzs", file + "." + str(i) + ".svg")
            op2 = sp.call(
                "dvisvgm --bbox=min -o {1} --clipjoin -e --no-fonts {0}".format(temp_dvifname, temp_svgfname)
            )
```
이 파이썬 코드는 `_posts/`아래 있는 모든 파일, 즉 모든 포스트들을 순회하며 `r"\$%%%tikzs\$((?:[\n]|.)*?)\$%%%tikzs\$"`이러한 정규식 패턴을 찾아낸다.
그리고 그 사이에 **tex**코드를 찾아내 `assets/tikzs/`에다 `<파일이름>.<순서>.tex`라는 형식으로 저장한다음 컴파일하여 `<파일이름>.<순서>.svg`로 저장한다.

이를 포스트내에서 `![]({{site.url}}/assets/tikzs/<파일이름>.<순서>.svg)`라는 이름으로 링크하면 8시간 동안의 삽질이 어느정도 일단락되는 것이다.
이를 조금더 편하게 이용하기 위해
```yaml
---
...
tikzlink: /assets/tikzs/<파일이름>
---
```
```md
![]({{site.url}}{{page.tikzlink}}.<순서>.svg)
```
다음과 같이 이용한다면 오타가 나는 일은 미연에 방지할 수 있을 것 같다.

## 진짜 결론
<!--
$%%%tikzs$
    \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
$%%%tikzs$
-->
<!--
$%%%tikzs$
    \begin{tikzpicture}
    \draw[step=1cm,gray,very thin] (-1.9,-1.9) grid (5.9,5.9);
    \draw[thick,->] (0,0) -- (4.5,0);
    \draw[thick,->] (0,0) -- (0,4.5);
    \draw[thick,->] (0,0) -- (4.5,0) node[anchor=north west] {x axis};
    \draw[thick,->] (0,0) -- (0,4.5) node[anchor=south east] {y axis};
    \draw[domain=-1:5, samples=100] plot(\x,{sin(\x)} );
  \end{tikzpicture}
$%%%tikzs$
-->


![]({{site.url}}{{page.tikzlink}}.0.svg)

![]({{site.url}}{{page.tikzlink}}.1.svg)


어쨋든 결론적으로 github pages에 tikz를 사용해보았다.
문제점이 아직 많이 산재해있지만 tikz를 그만큼 쓸것 같지도 않고 MathJax는 제대로 작동하니 일반적인 수식 쓸 때에는
딱히 문제가 없을 것 같아. 여기서 마무리지어도 될 것 같다.