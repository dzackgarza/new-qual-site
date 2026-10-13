---
schema: qual/card@1
id: P-UCLAB08F-03
kind: problem
title: Continuous pointwise limits without convergence of integrals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Give an example of continuous functions $f_n\colon[0,1]\to\mathbb R$ such that
\[
f(t)=\lim_{n\to\infty}f_n(t)
\]
is continuous, but
\[
\int_0^1 f_n(t)\,dt
\]
does not converge to $\int_0^1 f(t)\,dt$.
:::

::: {.solution}
For each integer $n\ge2$, define
\[
f_n(t)=
\begin{cases}
n^2t,
&0\le t\le \frac1n,\\[1mm]
n^2\left(\frac2n-t\right),
&\frac1n\le t\le\frac2n,\\[1mm]
0,
&\frac2n\le t\le1.
\end{cases}
\]

<1>1. Each $f_n$ is continuous on $[0,1]$.

::: {.proof}
Each piece is linear or constant. At the break points,
\[
n^2\cdot\frac1n
=
n
=
n^2\left(\frac2n-\frac1n\right),
\]
and
\[
n^2\left(\frac2n-\frac2n\right)=0.
\]
Thus the pieces match continuously.
:::

<1>2. The sequence $(f_n)$ converges pointwise to the zero function
\[
f(t)=0.
\]

::: {.proof}
At $t=0$,
\[
f_n(0)=0
\]
for every $n$.

Fix $t>0$. Since
\[
\frac2n\to0,
\]
for all sufficiently large $n$ one has
\[
\frac2n<t.
\]
Then the third case in the definition gives
\[
f_n(t)=0.
\]
Hence $f_n(t)\to0$ for every $t\in[0,1]$.
:::

<1>3. The pointwise limit $f$ is continuous.

::: {.proof}
The limit function is the constant zero function.
:::

<1>4. For every $n\ge2$,
\[
\int_0^1 f_n(t)\,dt=1.
\]

::: {.proof}
The graph of $f_n$ is a triangle of base length
\[
\frac2n
\]
and height
\[
n.
\]
Therefore its area is
\[
\frac12\cdot\frac2n\cdot n=1.
\]
Equivalently, the same value follows by integrating the two linear pieces directly.
:::

<1>5. The integrals do not converge to the integral of the pointwise limit.

::: {.proof}
By step <1>4,
\[
\lim_{n\to\infty}\int_0^1f_n(t)\,dt=1.
\]
By steps <1>2--<1>3,
\[
f\equiv0,
\]
so
\[
\int_0^1f(t)\,dt=0.
\]
Hence
\[
\boxed{
\lim_{n\to\infty}\int_0^1f_n(t)\,dt
\ne
\int_0^1f(t)\,dt
}.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 give the required example.
:::
:::
