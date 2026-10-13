---
schema: qual/card@1
id: P-WESRA14-8
kind: problem
title: 'Extend Radon–Nikodym from finite to sigma-finite measures'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Assuming the Radon–Nikodym theorem for finite measure spaces, prove it for $\sigma$-finite measure spaces.
:::

::: {.solution}
Let
\[
(X,\mathcal M)
\]
be a measurable space.
Let
\[
\mu
\quad\text{and}\quad
\nu
\]
be
\[
\sigma\text{-finite}
\]
positive measures with
\[
\nu\ll\mu.
\]
Assume the Radon--Nikodym theorem is known whenever both measures are finite.

<1>1. Choose measurable sets
\[
A_1,A_2,\dots
\]
and
\[
B_1,B_2,\dots
\]
such that
\[
X
=
\bigcup_{i=1}^{\infty}A_i
=
\bigcup_{j=1}^{\infty}B_j,
\]
with
\[
\mu(A_i)<\infty
\]
and
\[
\nu(B_j)<\infty.
\]

::: {.proof}
This follows from
\[
\sigma\text{-finiteness}
\]
of
\[
\mu
\]
and
\[
\nu,
\]
respectively.
:::

<1>2. The countable family
\[
\{A_i\cap B_j:i,j\ge1\}
\]
covers $X$, and on each member both measures are finite.

::: {.proof}
If
\[
x\in X,
\]
choose
\[
i
\]
with
\[
x\in A_i
\]
and
\[
j
\]
with
\[
x\in B_j.
\]
Then
\[
x\in A_i\cap B_j.
\]

Also
\[
\mu(A_i\cap B_j)
\le
\mu(A_i)
<
\infty,
\]
and
\[
\nu(A_i\cap B_j)
\le
\nu(B_j)
<
\infty.
\]
:::

<1>3. Enumerate the intersections from step <1>2 as
\[
C_1,C_2,\dots
\]
and define
\[
E_1=C_1,
\]
\[
E_n
\coloneqq
C_n
\setminus
\bigcup_{k=1}^{n-1}C_k
\qquad
(n\ge2).
\]
Then
\[
X
=
\bigsqcup_{n=1}^{\infty}E_n,
\]
and
\[
\mu(E_n)<\infty,
\qquad
\nu(E_n)<\infty.
\]

::: {.proof}
The disjointification procedure preserves the union.
Each
\[
E_n
\subseteq
C_n,
\]
so finiteness of both restricted measures follows from step <1>2.
:::

<1>4. For each
\[
n,
\]
define finite measures on
\[
(E_n,\mathcal M|_{E_n})
\]
by
\[
\mu_n(F)
\coloneqq
\mu(F)
\]
and
\[
\nu_n(F)
\coloneqq
\nu(F)
\]
for measurable
\[
F\subseteq E_n.
\]
Then
\[
\nu_n\ll\mu_n.
\]

::: {.proof}
Both measures are finite by step <1>3.
If
\[
\mu_n(F)=0,
\]
then
\[
\mu(F)=0.
\]
Since
\[
\nu\ll\mu,
\]
one has
\[
\nu(F)=0,
\]
so
\[
\nu_n(F)=0.
\]
:::

<1>5. By the finite-measure Radon--Nikodym theorem, for every $n$ there is
a measurable function
\[
f_n:E_n\to[0,\infty]
\]
such that
\[
\nu(F)
=
\int_F f_n\,d\mu
\]
for every measurable
\[
F\subseteq E_n.
\]

::: {.proof}
Apply the assumed finite Radon--Nikodym theorem to
\[
\nu_n\ll\mu_n.
\]
:::

<1>6. Define
\[
f:X\to[0,\infty]
\]
by
\[
f(x)=f_n(x)
\qquad
\text{when }x\in E_n.
\]
Then $f$ is measurable.

::: {.proof}
The sets
\[
E_n
\]
form a measurable partition of $X$.
Equivalently,
\[
f
=
\sum_{n=1}^{\infty}
f_n\mathbf 1_{E_n},
\]
where each summand is measurable after extending $f_n$ by zero outside
$E_n$.
Thus $f$ is measurable.
:::

<1>7. For every measurable
\[
A\subseteq X,
\]
\[
\nu(A)
=
\sum_{n=1}^{\infty}
\nu(A\cap E_n).
\]

::: {.proof}
The sets
\[
A\cap E_n
\]
are pairwise disjoint and their union is $A$.
Apply countable additivity of $\nu$.
:::

<1>8. For every measurable
\[
A\subseteq X,
\]
\[
\nu(A)
=
\sum_{n=1}^{\infty}
\int_{A\cap E_n}
f_n\,d\mu.
\]

::: {.proof}
Apply the local Radon--Nikodym formula from step <1>5 to each measurable
subset
\[
A\cap E_n
\subseteq
E_n,
\]
then substitute into step <1>7.
:::

<1>9. One has
\[
\sum_{n=1}^{\infty}
\int_{A\cap E_n}
f_n\,d\mu
=
\int_A f\,d\mu.
\]

::: {.proof}
Define
\[
g_N
\coloneqq
\sum_{n=1}^{N}
f_n\mathbf 1_{A\cap E_n}.
\]
Then
\[
0\le g_1\le g_2\le\cdots
\]
and
\[
g_N(x)
\uparrow
f(x)\mathbf 1_A(x)
\]
pointwise.

By the Monotone Convergence Theorem,
\[
\begin{aligned}
\int_A f\,d\mu
&=
\int_X f\mathbf 1_A\,d\mu\\
&=
\lim_{N\to\infty}
\int_X g_N\,d\mu\\
&=
\lim_{N\to\infty}
\sum_{n=1}^{N}
\int_{A\cap E_n}
f_n\,d\mu.
\end{aligned}
\]
:::

<1>10. Therefore
\[
\boxed{
\nu(A)
=
\int_A f\,d\mu
}
\]
for every
\[
A\in\mathcal M.
\]

::: {.proof}
Combine steps <1>8--<1>9.
Thus $f$ is a Radon--Nikodym derivative of $\nu$ with respect to $\mu$.
:::

<1>11. The derivative is unique
\[
\mu\text{-almost everywhere}.
\]

::: {.proof}
Suppose
\[
g
\]
is another measurable nonnegative function satisfying
\[
\nu(A)
=
\int_A g\,d\mu
\]
for every measurable $A$.

Restrict to any
\[
E_n.
\]
For every measurable
\[
F\subseteq E_n,
\]
\[
\int_F f_n\,d\mu
=
\nu(F)
=
\int_F g\,d\mu.
\]
By uniqueness in the finite Radon--Nikodym theorem,
\[
f_n=g
\]
almost everywhere on
\[
E_n.
\]

The countable union of these null exceptional sets is null.
Since the
\[
E_n
\]
cover $X$,
\[
f=g
\]
almost everywhere on $X$.
:::

<1>12. Hence the finite-measure Radon--Nikodym theorem implies the
$\sigma$-finite version.

::: {.proof}
Step <1>10 proves existence of the density, and step <1>11 proves its
almost-everywhere uniqueness.
These are the conclusions of the Radon--Nikodym theorem for
$\sigma$-finite measures.
:::

<1>13. Q.E.D.

::: {.proof}
Step <1>12 is the desired extension from finite to
\[
\sigma\text{-finite}
\]
measure spaces.
:::
:::
