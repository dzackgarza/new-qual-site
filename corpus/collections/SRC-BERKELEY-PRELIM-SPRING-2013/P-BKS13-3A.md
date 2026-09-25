---
schema: qual/card@1
id: P-BKS13-3A
kind: problem
title: Convergence of $\int_0^\infty x\exp(-x^6\sin^2 x)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2013 solution PDF and independently reviewed its spike estimate.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the interval decomposition around n*pi, the linear lower bound for |sin x|, and the resulting O(n^-2) summable bound.
---

::: {.problem}
Show that $\begin{array} { r } { \int _ { 0 } ^ { \infty } x \exp ( - x ^ { 6 } ( \sin x ) ^ { 2 } ) } \end{array}$ dx is finite.
:::

::: {.solution}
Set
$$
F(x)\coloneqq x e^{-x^6\sin^2x},
\qquad
x\geq0.
$$

<1>1. The integral of $F$ over $[0,\pi/2]$ is finite.

::: {.proof}
The function $F$ is continuous on the compact interval $[0,\pi/2]$.
Hence its integral there is finite.
:::

<1>2. For every real $u$ with
$$
\abs{u}\leq\frac\pi2,
$$
one has
$$
\abs{\sin u}
\geq
\frac{2}{\pi}\abs{u}.
$$

::: {.proof}
On $[0,\pi/2]$, the sine function is concave and lies above the chord
joining $(0,0)$ to $(\pi/2,1)$. Therefore
$$
\sin u\geq\frac{2u}{\pi}
$$
for $0\leq u\leq\pi/2$. The assertion for negative $u$ follows from the
oddness of sine.
:::

<1>3. For every integer $n\geq1$, let
$$
I_n
\coloneqq
\left[
n\pi-\frac\pi2,
n\pi+\frac\pi2
\right].
$$
If $x\in I_n$, then
$$
\frac{\pi n}{2}
\leq
x
\leq
\frac{3\pi n}{2}.
$$

::: {.proof}
Since $n\geq1$,
$$
n-\frac12\geq\frac n2
$$
and
$$
n+\frac12\leq\frac{3n}{2}.
$$
Multiplying by $\pi$ gives the result.
:::

<1>4. If $x\in I_n$ and
$$
u\coloneqq x-n\pi,
$$
then
$$
x^6\sin^2x
\geq
\frac{\pi^4}{16}n^6u^2.
$$

::: {.proof}
One has
$$
\abs{u}\leq\frac\pi2.
$$
Since
$$
\sin(n\pi+u)=(-1)^n\sin u,
$$
step <1>2 gives
$$
\sin^2x
\geq
\frac{4u^2}{\pi^2}.
$$
Step <1>3 gives
$$
x^6
\geq
\left(\frac{\pi n}{2}\right)^6.
$$
Multiplying,
$$
x^6\sin^2x
\geq
\left(\frac{\pi^6n^6}{64}\right)
\left(\frac{4u^2}{\pi^2}\right)
=
\frac{\pi^4}{16}n^6u^2.
$$
:::

<1>5. There is a constant $C>0$, independent of $n$, such that
$$
\int_{I_n}F(x)\,dx
\leq
\frac{C}{n^2}
$$
for every $n\geq1$.

::: {.proof}
Let
$$
c\coloneqq\frac{\pi^4}{16}.
$$
By steps <1>3 and <1>4,
$$
\begin{aligned}
\int_{I_n}F(x)\,dx
&\leq
\frac{3\pi n}{2}
\int_{-\pi/2}^{\pi/2}
e^{-cn^6u^2}\,du\\
&\leq
\frac{3\pi n}{2}
\int_{-\infty}^{\infty}
e^{-cn^6u^2}\,du.
\end{aligned}
$$
With the substitution
$$
v=n^3u,
$$
the last integral becomes
$$
\frac1{n^3}
\int_{-\infty}^{\infty}e^{-cv^2}\,dv.
$$
The Gaussian integral on the right is finite. Hence
$$
\int_{I_n}F(x)\,dx
\leq
\frac{C}{n^2}
$$
for the constant
$$
C
\coloneqq
\frac{3\pi}{2}
\int_{-\infty}^{\infty}e^{-cv^2}\,dv.
$$
:::

<1>6. The improper integral over $[\pi/2,\infty)$ is finite.

::: {.proof}
The intervals
$$
I_1,I_2,\ldots
$$
cover $[\pi/2,\infty)$ and meet only at endpoints. Since $F\geq0$,
step <1>5 gives
$$
\int_{\pi/2}^{\infty}F(x)\,dx
=
\sum_{n=1}^{\infty}
\int_{I_n}F(x)\,dx
\leq
C\sum_{n=1}^{\infty}\frac1{n^2}
<
\infty.
$$
:::

<1>7. Therefore
$$
\boxed{
\int_0^\infty
x e^{-x^6\sin^2x}\,dx
<
\infty
}.
$$

::: {.proof}
Step <1>1 gives finiteness on $[0,\pi/2]$, and step <1>6 gives
finiteness on $[\pi/2,\infty)$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required convergence statement.
:::
:::
