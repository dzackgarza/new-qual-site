---
schema: qual/card@1
id: P-BKF14-4B
kind: problem
title: Independence of boundary convergence and analytic continuation at $1$ for power series
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
    Independently checked the four examples in the retained Fall 2014
    solution packet and their boundary convergence and extension behavior.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked radius one for all four series, convergence at z=1 where
    required, and the derivative/function blow-up arguments excluding
    holomorphic extension for f_2 and f_4.
---

::: {.problem}
Find four power series $f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 }$ with radius of convergence 1 such that $f _ { 1 } , f _ { 2 }$ converge at 1 but $f _ { 3 } , f _ { 4 }$ do not, and the functions given by $f _ { 1 } , f _ { 3 }$ can be extended to functions holomorphic in a neighborhood of 1, but the functions given by $f _ { 2 } , f _ { 4 }$ cannot be.
:::

::: {.solution}
Take
$$
\begin{aligned}
f_1(z)&\coloneqq\sum_{n=1}^{\infty}\frac{(-1)^{n-1}z^n}{n},\\
f_2(z)&\coloneqq\sum_{n=1}^{\infty}\frac{z^n}{n^2},\\
f_3(z)&\coloneqq\sum_{n=0}^{\infty}(-1)^n z^n,\\
f_4(z)&\coloneqq\sum_{n=1}^{\infty}\frac{z^n}{n}.
\end{aligned}
$$

<1>1. Each of the four power series has radius of convergence exactly
$1$.

::: {.proof}
For the coefficient sequences
$$
\frac{(-1)^{n-1}}n,\qquad
\frac1{n^2},\qquad
(-1)^n,\qquad
\frac1n,
$$
respectively, the $n$th roots of the absolute values tend to $1$.
The Cauchy--Hadamard formula therefore gives radius of convergence
$1$ in every case.
:::

<1>2. The series $f_1$ converges at $1$ and extends holomorphically to
a neighborhood of $1$.

::: {.proof}
At $z=1$,
$$
f_1(1)=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}n
$$
converges by the alternating-series test.

For $|z|<1$, differentiating the power series gives
$$
f_1'(z)
=
\sum_{n=1}^{\infty}(-1)^{n-1}z^{n-1}
=
\frac1{1+z},
$$
and $f_1(0)=0$. Thus
$$
f_1(z)=\log(1+z)
$$
for the branch of the logarithm with $\log(1)=0$: on $|z|<1$ one has
$\Re(1+z)>0$, so this branch is well-defined and the derivative and
value at $0$ agree with those of $f_1$. The same expression
$\log(1+z)$ is holomorphic, for example, on the disk $|z-1|<1$.
Hence $f_1$ extends holomorphically across $1$.
:::

<1>3. The series $f_2$ converges at $1$ but does not extend
holomorphically to any neighborhood of $1$.

::: {.proof}
At $z=1$,
$$
f_2(1)=\sum_{n=1}^{\infty}\frac1{n^2}
$$
converges.

Inside the unit disk,
$$
f_2'(z)=\sum_{n=1}^{\infty}\frac{z^{n-1}}n.
$$
For real $0<r<1$, all terms are nonnegative, and for every $N$,
$$
f_2'(r)
\ge
\sum_{n=1}^{N}\frac{r^{n-1}}n.
$$
Letting $r\uparrow1$ and then choosing $N$ large shows
$$
f_2'(r)\longrightarrow+\infty.
$$
If $f_2$ admitted a holomorphic extension to a neighborhood of $1$,
its derivative would be continuous, hence bounded on a sufficiently
small closed disk about $1$. On the portion of that disk inside
$|z|<1$, the derivative would agree with $f_2'$, contradicting the
displayed blow-up.
:::

<1>4. The series $f_3$ does not converge at $1$, but its power-series
function extends holomorphically to a neighborhood of $1$.

::: {.proof}
At $z=1$, the terms of the series are $(-1)^n$, which do not tend to
$0$, so the series diverges.

For $|z|<1$, the geometric-series identity gives
$$
f_3(z)=\frac1{1+z}.
$$
The rational function $1/(1+z)$ is holomorphic on a neighborhood of
$z=1$, so it supplies the required extension.
:::

<1>5. The series $f_4$ does not converge at $1$ and does not extend
holomorphically to any neighborhood of $1$.

::: {.proof}
At $z=1$,
$$
f_4(1)=\sum_{n=1}^{\infty}\frac1n
$$
is the divergent harmonic series.

For real $0<r<1$,
$$
f_4(r)=\sum_{n=1}^{\infty}\frac{r^n}{n}.
$$
As in step <1>3, finite partial sums show that
$$
f_4(r)\longrightarrow+\infty
\qquad
\text{as }r\uparrow1.
$$
A holomorphic extension to a neighborhood of $1$ would be continuous,
and therefore bounded on a sufficiently small closed disk about $1$.
Its agreement with $f_4$ on the unit-disk side would contradict this
blow-up.
:::

<1>6. The four series have exactly the requested combination of
properties.

::: {.proof}
Step <1>1 gives radius $1$ for all four. Steps <1>2--<1>5 give,
respectively,
$$
\begin{array}{c|cc}
&\text{converges at }1&\text{extends holomorphically near }1\\
\hline
f_1&\text{yes}&\text{yes}\\
f_2&\text{yes}&\text{no}\\
f_3&\text{no}&\text{yes}\\
f_4&\text{no}&\text{no}.
\end{array}
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 matches all four requirements in the problem.
:::
:::
