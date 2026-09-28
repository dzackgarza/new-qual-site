---
schema: qual/card@1
id: P-BKS11-9B
kind: problem
title: 'Interchanging limits: integrals, double series, and pointwise limits'
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
  note: Compared all three parts with page 6 of the retained Spring 2011 solution PDF and independently reviewed its counterexamples.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked continuity and pointwise convergence of the spike and step-limit examples and computed both iterated sums in the double-series counterexample.
---

::: {.problem}
For each of the following statements, either prove it or give a counterexample:

(a) If $f(x)$ and $f_n(x)$ are continuous real-valued functions on the unit interval, and $\lim_{n\to\infty}f_n(x)=f(x)$ for all $x$, then
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx=\int_0^1 f(x)\,dx.
$$

(b) If $g(m,n)$ is real for all integers $m,n$, and
$$
\sum_{m=0}^{\infty}\left(\sum_{n=0}^{\infty}g(m,n)\right)
\quad\text{and}\quad
\sum_{n=0}^{\infty}\left(\sum_{m=0}^{\infty}g(m,n)\right)
$$
are both defined, then they are equal.

(c) If the functions $h_n(x)$ are continuous real-valued functions on the unit interval, and $\lim_{n\to\infty}h_n(x)=h(x)$ for all $x$, then $h(x)$ is a continuous function of $x$.
:::

::: {.solution}
<1>1. Assertion (a) is false.

::: {.proof}
For $n\geq1$, define
$$
f_n(x)
\coloneqq
\begin{cases}
4n^2x,
&
0\leq x\leq \dfrac{1}{2n},
\\[4pt]
4n-4n^2x,
&
\dfrac{1}{2n}\leq x\leq\dfrac1n,
\\[4pt]
0,
&
\dfrac1n\leq x\leq1.
\end{cases}
$$
The formulas agree at the break points, so each $f_n$ is continuous.
Geometrically, its graph is a triangle of base $1/n$ and height $2n$.
Hence
$$
\int_0^1f_n(x)\,dx
=
\frac12\frac1n(2n)
=
1
$$
for every $n$.

For $x=0$, one has $f_n(0)=0$. If $x>0$ is fixed, then for all
sufficiently large $n$,
$$
\frac1n<x,
$$
so $f_n(x)=0$. Thus
$$
f_n(x)\longrightarrow0
$$
pointwise on $[0,1]$. The pointwise limit
$$
f(x)\equiv0
$$
is continuous, but
$$
\lim_{n\to\infty}\int_0^1f_n(x)\,dx
=
1
\neq
0
=
\int_0^1f(x)\,dx.
$$
:::

<1>2. Assertion (b) is false.

::: {.proof}
For nonnegative integers $m,n$, define
$$
g(m,n)
\coloneqq
\begin{cases}
1,&m=n,\\
-1,&m=n+1,\\
0,&\text{otherwise}.
\end{cases}
$$
For $m=0$,
$$
\sum_{n=0}^{\infty}g(0,n)=1.
$$
For every $m\geq1$, the only nonzero terms in the $m$th row are
$$
g(m,m)=1
$$
and
$$
g(m,m-1)=-1,
$$
so the row sum is $0$. Therefore
$$
\sum_{m=0}^{\infty}
\left(
\sum_{n=0}^{\infty}g(m,n)
\right)
=
1.
$$

For every fixed $n\geq0$, the only nonzero terms in the $n$th column are
$$
g(n,n)=1
$$
and
$$
g(n+1,n)=-1.
$$
Thus every column sum is $0$, and therefore
$$
\sum_{n=0}^{\infty}
\left(
\sum_{m=0}^{\infty}g(m,n)
\right)
=
0.
$$
Both iterated sums are defined, but they are unequal.
:::

<1>3. Assertion (c) is false.

::: {.proof}
For $n\geq1$, define
$$
h_n(x)
\coloneqq
\max(1-nx,0),
\qquad
0\leq x\leq1.
$$
Each $h_n$ is continuous. At $x=0$,
$$
h_n(0)=1
$$
for every $n$. If $x>0$ is fixed, then for all sufficiently large $n$,
$$
nx>1,
$$
so $h_n(x)=0$. Hence the pointwise limit is
$$
h(x)
=
\begin{cases}
1,&x=0,\\
0,&0<x\leq1.
\end{cases}
$$
This function is not continuous at $0$.
:::

<1>4. The three assertions are all false.

::: {.proof}
Steps <1>1, <1>2, and <1>3 give explicit counterexamples to parts (a),
(b), and (c), respectively.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 settles every requested assertion.
:::
:::
