---
title: MathJax와 TikzJax
category: etc
tags: [HTML, math]
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

<script type="text/tikz">
  \begin{tikzpicture}
    \draw (0,0) circle (1in);
  \end{tikzpicture}
</script>

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
<script type="text/tikz">
  \begin{tikzpicture}
    \draw[step=1cm,gray,very thin] (-1.9,-1.9) grid (5.9,1.9);
    \draw[thick,->] (0,0) -- (4.5,0) node[anchor=north west] {x axis};
    \draw[thick,->] (0,0) -- (0,1.9) node[anchor=south east] {y axis};
    \draw[domain=-1:4.2, samples=100] plot(\x,{sin(40*\x)} ) node [right] {$\sin(x)$};
  \end{tikzpicture}
</script>

## 결론
이와 같은 일련의 과정을 통하여 `우리`는 수학을 웹사이트에서 마구 굴릴 수 있게 되었다.
