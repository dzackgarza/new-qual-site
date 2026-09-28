---
schema: qual/card@1
id: P-BKF13-5B
kind: problem
title: Holomorphic self-maps of a bounded domain tangent to the identity have $a_2=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2013 solution packet: the
    n-fold iterate has quadratic coefficient n a_2, and Cauchy's coefficient
    formula bounds that coefficient uniformly in n.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the iterate expansion by induction and the Cauchy estimate on a
    closed disk compactly contained in U.
---

::: {.problem}
Let $U\subset\CC$ be a bounded open set containing $0$, and let $f\colon U\to U$ be an analytic function, whose Taylor series at $0$ is

$$
f(z)=z+a_2z^2+a_3z^3+\cdots
$$

Prove that $a_2=0$. (Hint: consider the functions $g_n(z)=f\circ\cdots\circ f(z)$ obtained by composing $f$ with itself $n$ times.)
:::

::: {.solution}
For $n\ge1$, let $g_n=f^{\circ n}$. Choose $R>0$ such that
$|w|\le R$ for every $w\in U$, and choose $r>0$ such that
$\{z:|z|\le r\}\subset U$.

<1>1. For every $n\ge1$,
$$
g_n(z)=z+na_2z^2+O(z^3)
$$
as $z\to0$.

::: {.proof}
For $n=1$ this is the given Taylor expansion of $f$. Suppose
$$
g_n(z)=z+na_2z^2+O(z^3).
$$
Then $g_n(z)=z+O(z^2)$, so
$$
g_n(z)^2=z^2+O(z^3)
\quad\text{and}\quad
g_n(z)^3=O(z^3).
$$
Using
$$
f(w)=w+a_2w^2+O(w^3)
$$
with $w=g_n(z)$ gives
$$
\begin{aligned}
g_{n+1}(z)
&=f(g_n(z))\\
&=g_n(z)+a_2g_n(z)^2+O(g_n(z)^3)\\
&=z+(n+1)a_2z^2+O(z^3).
\end{aligned}
$$
The claim follows by induction.
:::

<1>2. For every $n\ge1$ and every $z$ with $|z|=r$,
$$
|g_n(z)|\le R.
$$

::: {.proof}
Each iterate $g_n$ maps $U$ into $U$ because $f(U)\subset U$. Since the
circle $|z|=r$ lies in $U$, one has $g_n(z)\in U$, and the choice of $R$
gives the estimate.
:::

<1>3. For every $n\ge1$,
$$
n|a_2|\le\frac{R}{r^2}.
$$

::: {.proof}
By step <1>1, the coefficient of $z^2$ in the Taylor expansion of $g_n$
at $0$ is $na_2$. Cauchy's coefficient formula therefore gives
$$
na_2
=
\frac{1}{2\pi i}
\int_{|z|=r}\frac{g_n(z)}{z^3}\,dz.
$$
Using step <1>2 and the fact that the circle has length $2\pi r$,
$$
\begin{aligned}
n|a_2|
&\le
\frac{1}{2\pi}(2\pi r)\frac{R}{r^3}\\
&=
\frac{R}{r^2}.
\end{aligned}
$$
:::

<1>4. One has
$$
\boxed{a_2=0}.
$$

::: {.proof}
Step <1>3 yields
$$
|a_2|\le\frac{R}{nr^2}
$$
for every $n\ge1$. Letting $n\to\infty$ gives $|a_2|=0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
