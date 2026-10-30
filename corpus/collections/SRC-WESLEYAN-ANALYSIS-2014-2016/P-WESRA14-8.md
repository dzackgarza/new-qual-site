---
schema: qual/card@1
id: P-WESRA14-8
kind: problem
title: 'The Radon–Nikodym theorem from finite to $\sigma$-finite measures'
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
$$
(X,\mathcal M)
$$
be a measurable space.
Let
$$
\mu
\quad\text{and}\quad
\nu
$$
be
$$
\sigma\text{-finite}
$$
positive measures with
$$
\nu\ll\mu.
$$
Assume the Radon--Nikodym theorem is known whenever both measures are finite.

::: pf

::: pf-step

Choose measurable sets
$$
A_1,A_2,\dots
$$
and
$$
B_1,B_2,\dots
$$
such that
$$
X
=
\bigcup_{i=1}^{\infty}A_i
=
\bigcup_{j=1}^{\infty}B_j,
$$
with
$$
\mu(A_i)<\infty
$$
and
$$
\nu(B_j)<\infty.
$$


::: pf-proof

This follows from
$$
\sigma\text{-finiteness}
$$
of
$$
\mu
$$
and
$$
\nu,
$$
respectively.

:::

:::

::: {.pf-step #s1-2}

The countable family
$$
\{A_i\cap B_j:i,j\ge1\}
$$
covers $X$, and on each member both measures are finite.


::: pf-proof

If
$$
x\in X,
$$
choose
$$
i
$$
with
$$
x\in A_i
$$
and
$$
j
$$
with
$$
x\in B_j.
$$
Then
$$
x\in A_i\cap B_j.
$$

Also
$$
\mu(A_i\cap B_j)
\le
\mu(A_i)
<
\infty,
$$
and
$$
\nu(A_i\cap B_j)
\le
\nu(B_j)
<
\infty.
$$

:::

:::

::: {.pf-step #s1-3}

Enumerate the intersections from step [](#s1-2){.pf-ref} as
$$
C_1,C_2,\dots
$$
and define
$$
E_1=C_1,
$$
$$
E_n
\coloneqq
C_n
\setminus
\bigcup_{k=1}^{n-1}C_k
\qquad
(n\ge2).
$$
Then
$$
X
=
\bigsqcup_{n=1}^{\infty}E_n,
$$
and
$$
\mu(E_n)<\infty,
\qquad
\nu(E_n)<\infty.
$$


::: pf-proof

The disjointification procedure preserves the union.
Each
$$
E_n
\subseteq
C_n,
$$
so finiteness of both restricted measures follows from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

For each
$$
n,
$$
define finite measures on
$$
(E_n,\mathcal M\restrict_{E_n})
$$
by
$$
\mu_n(F)
\coloneqq
\mu(F)
$$
and
$$
\nu_n(F)
\coloneqq
\nu(F)
$$
for measurable
$$
F\subseteq E_n.
$$
Then
$$
\nu_n\ll\mu_n.
$$


::: pf-proof

Both measures are finite by step [](#s1-3){.pf-ref}.
If
$$
\mu_n(F)=0,
$$
then
$$
\mu(F)=0.
$$
Since
$$
\nu\ll\mu,
$$
one has
$$
\nu(F)=0,
$$
so
$$
\nu_n(F)=0.
$$

:::

:::

::: {.pf-step #s1-5}

By the finite-measure Radon--Nikodym theorem, for every $n$ there is
a measurable function
$$
f_n:E_n\to[0,\infty]
$$
such that
$$
\nu(F)
=
\int_F f_n\,d\mu
$$
for every measurable
$$
F\subseteq E_n.
$$


::: pf-proof

Apply the assumed finite Radon--Nikodym theorem to
$$
\nu_n\ll\mu_n.
$$

:::

:::

::: pf-step

Define
$$
f:X\to[0,\infty]
$$
by
$$
f(x)=f_n(x)
\qquad
\text{when }x\in E_n.
$$
Then $f$ is measurable.


::: pf-proof

The sets
$$
E_n
$$
form a measurable partition of $X$.
Equivalently,
$$
f
=
\sum_{n=1}^{\infty}
f_n\mathbf 1_{E_n},
$$
where each summand is measurable after extending $f_n$ by zero outside
$E_n$.
Thus $f$ is measurable.

:::

:::

::: {.pf-step #s1-7}

For every measurable
$$
A\subseteq X,
$$
$$
\nu(A)
=
\sum_{n=1}^{\infty}
\nu(A\cap E_n).
$$


::: pf-proof

The sets
$$
A\cap E_n
$$
are pairwise disjoint and their union is $A$.
Apply countable additivity of $\nu$.

:::

:::

::: {.pf-step #s1-8}

For every measurable
$$
A\subseteq X,
$$
$$
\nu(A)
=
\sum_{n=1}^{\infty}
\int_{A\cap E_n}
f_n\,d\mu.
$$


::: pf-proof

Apply the local Radon--Nikodym formula from step [](#s1-5){.pf-ref} to each measurable
subset
$$
A\cap E_n
\subseteq
E_n,
$$
then substitute into step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\sum_{n=1}^{\infty}
\int_{A\cap E_n}
f_n\,d\mu
=
\int_A f\,d\mu.
$$


::: pf-proof

Define
$$
g_N
\coloneqq
\sum_{n=1}^{N}
f_n\mathbf 1_{A\cap E_n}.
$$
Then
$$
0\le g_1\le g_2\le\cdots
$$
and
$$
g_N(x)
\uparrow
f(x)\mathbf 1_A(x)
$$
pointwise.

By the Monotone Convergence Theorem,
$$
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
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\nu(A)
=
\int_A f\,d\mu
}
$$
for every
$$
A\in\mathcal M.
$$


::: pf-proof

Combine steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.
Thus $f$ is a Radon--Nikodym derivative of $\nu$ with respect to $\mu$.

:::

:::

::: {.pf-step #s1-11}

The derivative is unique
$$
\mu\text{-almost everywhere}.
$$


::: pf-proof

Suppose
$$
g
$$
is another measurable nonnegative function satisfying
$$
\nu(A)
=
\int_A g\,d\mu
$$
for every measurable $A$.

Restrict to any
$$
E_n.
$$
For every measurable
$$
F\subseteq E_n,
$$
$$
\int_F f_n\,d\mu
=
\nu(F)
=
\int_F g\,d\mu.
$$
By uniqueness in the finite Radon--Nikodym theorem,
$$
f_n=g
$$
almost everywhere on
$$
E_n.
$$

The countable union of these null exceptional sets is null.
Since the
$$
E_n
$$
cover $X$,
$$
f=g
$$
almost everywhere on $X$.

:::

:::

::: {.pf-step #s1-12}

Hence the finite-measure Radon--Nikodym theorem implies the
$\sigma$-finite version.


::: pf-proof

Step [](#s1-10){.pf-ref} proves existence of the density, and step [](#s1-11){.pf-ref} proves its
almost-everywhere uniqueness.
These are the conclusions of the Radon--Nikodym theorem for
$\sigma$-finite measures.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the desired extension from finite to
$$
\sigma\text{-finite}
$$
measure spaces.

:::

:::

:::
