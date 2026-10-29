---
schema: qual/card@1
id: P-UCLAB16F-11
kind: problem
title: Topology of the metric measuring where continuous functions last disagree
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 11 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
We define a metric space $(X, \operatorname{dist})$ as follows:

$$
X := \{f : [0, 1] \to [0, 1] \mid f \text{ is continuous and } f(1) = 0\},
$$

$$
\operatorname{dist}(f, g) = \inf\{r \in [0, 1] \mid f(t) = g(t) \text{ for all } r \leq t \leq 1\}.
$$

Prove any TWO of the following statements about $(X, \operatorname{dist})$:

(a) It is not compact. (b) It is not connected.
(c) It is not separable. (d) It is not complete.
:::

::: {.solution}

The proof establishes (b) and (d).

::: pf

::: {.pf-step #s1-1}

The metric satisfies the strong triangle inequality
$$
\operatorname{dist}(f,h)
\le
\max\{
\operatorname{dist}(f,g),
\operatorname{dist}(g,h)
\}.
$$


::: pf-proof

Set
$$
a=\operatorname{dist}(f,g),
\qquad
b=\operatorname{dist}(g,h).
$$
Fix
$$
r>\max\{a,b\}.
$$
By the definition of infimum, there exist
$$
r_1<r,
\qquad
r_2<r
$$
such that
$$
f(t)=g(t)
\quad\text{for }r_1\le t\le1
$$
and
$$
g(t)=h(t)
\quad\text{for }r_2\le t\le1.
$$
Hence
$$
f(t)=h(t)
$$
for
$$
\max\{r_1,r_2\}\le t\le1.
$$
Therefore
$$
\operatorname{dist}(f,h)
\le
\max\{r_1,r_2\}
<
r.
$$
Since this holds for every
$$
r>\max\{a,b\},
$$
the strong triangle inequality follows.

:::

:::

::: {.pf-step #s1-2}

Every open ball in $(X,\operatorname{dist})$ is also closed.


::: pf-proof

Fix
$$
f\in X
$$
and $\rho>0$, and let
$$
U=B(f,\rho).
$$
Take
$$
g\notin U.
$$
Then
$$
\operatorname{dist}(f,g)\ge\rho.
$$
If
$$
h\in B(g,\rho),
$$
then
$$
\operatorname{dist}(g,h)<\rho.
$$
If $h$ belonged to $U$, then
$$
\operatorname{dist}(f,h)<\rho.
$$
The strong triangle inequality from step [](#s1-1){.pf-ref} would give
$$
\operatorname{dist}(f,g)
\le
\max\{
\operatorname{dist}(f,h),
\operatorname{dist}(h,g)
\}
<
\rho,
$$
contradicting
$$
\operatorname{dist}(f,g)\ge\rho.
$$
Thus
$$
B(g,\rho)
\subseteq
X\setminus U.
$$
So the complement of $U$ is open, and $U$ is closed.

:::

:::

::: {.pf-step #s1-3}

The space $X$ is not connected.


::: pf-proof

Let
$$
f_0(t)=0.
$$
The ball
$$
U=B(f_0,1/2)
$$
is nonempty because it contains $f_0$.
It is both open and closed by step [](#s1-2){.pf-ref}.

It is proper.
Indeed, define
$$
g(t)=1-t.
$$
Then
$$
g\in X.
$$
For every
$$
r<1,
$$
the functions $g$ and $f_0$ differ at every
$$
t\in[r,1),
$$
so they do not agree on $[r,1]$.
They agree on $[1,1]$.
Hence
$$
\operatorname{dist}(g,f_0)=1,
$$
so
$$
g\notin U.
$$
Thus $U$ is a nonempty proper clopen subset of $X$, and therefore $X$ is not connected.
This proves (b).

:::

:::

::: {.pf-step #s1-4}

Define, for $0<t\le1$,
$$
h(t)
=
\frac{1-t}{2}
\left(
1+\sin\frac1t
\right).
$$
Then
$$
0\le h(t)\le1,
\qquad
h(1)=0,
$$
and $h$ has no limit as $t\downarrow0$.


::: pf-proof

Since
$$
-1\le\sin(1/t)\le1,
$$
one has
$$
0
\le
\frac{1+\sin(1/t)}2
\le1.
$$
Multiplication by
$$
1-t\in[0,1)
$$
preserves the interval $[0,1]$, so
$$
0\le h(t)\le1.
$$
At $t=1$,
$$
h(1)=0.
$$

As $t\downarrow0$, the factor
$$
1-t
$$
tends to $1$, while
$$
\frac{1+\sin(1/t)}2
$$
oscillates between values arbitrarily close to $0$ and $1$.
Hence $h$ has no limit at $0$.

:::

:::

::: pf-step

For each $n\ge1$, define
$$
f_n(t)
=
\begin{cases}
h(1/n),&0\le t\le1/n,\\
h(t),&1/n\le t\le1.
\end{cases}
$$
Then
$$
f_n\in X.
$$


::: pf-proof

The two formulas agree at
$$
t=1/n,
$$
so $f_n$ is continuous.
By step [](#s1-4){.pf-ref}, its values lie in $[0,1]$.
Also
$$
f_n(1)=h(1)=0.
$$
Thus $f_n\in X$.

:::

:::

::: {.pf-step #s1-6}

If $m\ge n$, then
$$
\operatorname{dist}(f_m,f_n)
\le
\frac1n.
$$


::: pf-proof

For every
$$
t\ge\frac1n,
$$
one also has
$$
t\ge\frac1m,
$$
because $m\ge n$.
Thus both functions use the formula $h(t)$ there:
$$
f_m(t)=h(t)=f_n(t).
$$
Hence they agree on
$$
\left[\frac1n,1\right],
$$
so the defining infimum of the distance is at most $1/n$.

:::

:::

::: {.pf-step #s1-7}

The sequence $(f_n)$ is Cauchy in $(X,\operatorname{dist})$.


::: pf-proof

Let $\varepsilon>0$.
Choose $N$ with
$$
\frac1N<\varepsilon.
$$
For
$$
m,n\ge N,
$$
assume without loss of generality that $m\ge n$.
Then step [](#s1-6){.pf-ref} gives
$$
\operatorname{dist}(f_m,f_n)
\le
\frac1n
\le
\frac1N
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-8}

If $(f_n)$ converged in $X$ to some $f$, then
$$
f(t)=h(t)
$$
for every
$$
t>0.
$$


::: pf-proof

Fix $t>0$.
Choose $N$ so large that
$$
\operatorname{dist}(f_n,f)<t
$$
for every $n\ge N$, and also
$$
\frac1n<t
$$
for every $n\ge N$.

For such $n$, the inequality
$$
\operatorname{dist}(f_n,f)<t
$$
means there exists
$$
r<t
$$
such that
$$
f_n(s)=f(s)
$$
for all
$$
r\le s\le1.
$$
In particular,
$$
f_n(t)=f(t).
$$
Since
$$
t>\frac1n,
$$
the definition of $f_n$ gives
$$
f_n(t)=h(t).
$$
Therefore
$$
f(t)=h(t).
$$

:::

:::

::: {.pf-step #s1-9}

The Cauchy sequence $(f_n)$ has no limit in $X$.


::: pf-proof

If it converged to some
$$
f\in X,
$$
step [](#s1-8){.pf-ref} would give
$$
f(t)=h(t)
$$
for every $t>0$.
Since $f$ is continuous on $[0,1]$, the limit
$$
\lim_{t\downarrow0}f(t)
$$
would exist and equal $f(0)$.
But step [](#s1-4){.pf-ref} says $h(t)$ has no limit as $t\downarrow0$.
This is a contradiction.

:::

:::

::: {.pf-step #s1-10}

Therefore $(X,\operatorname{dist})$ is not complete.


::: pf-proof

Step [](#s1-7){.pf-ref} gives a Cauchy sequence in $X$, and step [](#s1-9){.pf-ref} shows that it does not converge to any point of $X$.
This proves (d).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves (b), and step [](#s1-10){.pf-ref} proves (d), as requested.

:::

:::

:::
