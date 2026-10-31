---
schema: qual/card@1
id: P-PRACT20-W6-01
kind: problem
title: Continuity of the function equal to $x/2$ on $\QQ$ and $x/3$ off $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Continuity
relations: []
review: draft
---

::: {.problem}
Where is the function
$$
f(x)=\begin{cases}x/2,&x\in\QQ,\\x/3,&x\in\RR\setminus\QQ\end{cases}
$$
continuous?
:::

::: {.solution}
The function is continuous only at $x=0$.

If $x\neq0$, take sequences $(q_n)\subset\QQ$ and $(r_n)\subset\RR\setminus\QQ$ converging to $x$; both exist because $\QQ$ and $\RR\setminus\QQ$ are dense in $\RR$. Then

$$
\frac x2=\lim_{n\to\infty}f(q_n)\neq\lim_{n\to\infty}f(r_n)=\frac x3,
$$

so $f$ is discontinuous at $x$ by the sequential criterion.

At $x=0$, we have $\abs{f(x)}\leq\abs{x}/2$ for every $x$. Given $\varepsilon>0$, set $\delta=2\varepsilon$; then $\abs{f(x)-f(0)}<\varepsilon$ when $\abs{x}<\delta$. So $f$ is continuous at $0$.

More generally, let $D\subset\RR$ be such that $D$ and $\RR\setminus D$ are both dense in $\RR$ (for example $D=\QQ$), and define

$$
f(x)=\begin{cases}g(x),&x\in D,\\h(x),&x\in\RR\setminus D,\end{cases}
$$

where $g,h\colon\RR\to\RR$ are continuous. The same argument shows that $f$ is continuous at $x$ if and only if $g(x)=h(x)$.
:::
