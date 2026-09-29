---
schema: qual/card@1
id: P-BKS09-9B
kind: problem
title: $\sin nx$ has no pointwise convergent subsequence
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
  note: Compared the authored statement and elementary nested-interval solution with the Spring 2009 solution-packet extraction.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently supplied and checked the interval-oscillation lemma and the nested compact interval argument for an arbitrary subsequence.
---

::: {.problem}
Prove that the sequence of functions $f _ { n } ( x ) = \sin n x$ has no pointwise convergent subsequence.
(Hint: show that given any subsequence and any interval of positive length there is a subinterval such that some element of the subsequence is at least $1 / 2$ on this subinterval, and another element is at most $- 1 / 2$.)
:::

::: {.solution}
Let
$$
\sin(n_kx)
$$
be an arbitrary subsequence of the original sequence. Then
$$
n_k\longrightarrow\infty.
$$

::: pf

::: {.pf-step #interval-with-sin-large}
Let $I=[a,b]$ be a closed interval with $a<b$. For every sufficiently
large positive integer $n$, there is a nondegenerate closed subinterval
$J^+\subseteq I$ on which
$$
\sin(nx)\geq\frac12.
$$

::: pf-proof
For each integer $m$, set
$$
J_{m,n}^+
\coloneqq
\left[
\frac{2\pi m+\pi/6}{n},
\frac{2\pi m+5\pi/6}{n}
\right].
$$
On this interval,
$$
nx\in
[2\pi m+\pi/6, 2\pi m+5\pi/6],
$$
so
$$
\sin(nx)\geq\frac12.
$$

The left endpoints of the intervals $J_{m,n}^+$ are spaced by
$2\pi/n$. Choose $m$ so that the left endpoint lies in
$$
[a,a+2\pi/n).
$$
The corresponding right endpoint is then less than
$$
a+\frac{2\pi}{n}+\frac{2\pi}{3n}
=
a+\frac{8\pi}{3n}.
$$
For all sufficiently large $n$,
$$
\frac{8\pi}{3n}<b-a,
$$
so this whole interval $J_{m,n}^+$ lies inside $I$.
:::

:::

::: {.pf-step #interval-with-sin-small}
Let $I=[a,b]$ be a closed interval with $a<b$. For every sufficiently
large positive integer $n$, there is a nondegenerate closed subinterval
$J^-\subseteq I$ on which
$$
\sin(nx)\leq-\frac12.
$$

::: pf-proof
For each integer $m$, set
$$
J_{m,n}^-
\coloneqq
\left[
\frac{2\pi m+7\pi/6}{n},
\frac{2\pi m+11\pi/6}{n}
\right].
$$
On this interval,
$$
nx\in
[2\pi m+7\pi/6, 2\pi m+11\pi/6],
$$
so
$$
\sin(nx)\leq-\frac12.
$$
The left endpoints are again spaced by $2\pi/n$. The same argument as in
step [](#interval-with-sin-large){.pf-ref} shows that one of these intervals is contained in $I$ for all
sufficiently large $n$.
:::

:::

::: {.pf-step #nested-intervals-exist}
There exist indices
$$
k_1<k_2<k_3<\cdots
$$
and nested nondegenerate closed intervals
$$
I_1\supseteq I_2\supseteq I_3\supseteq\cdots
$$
such that
$$
\sin(n_{k_j}x)\geq\frac12
$$
for every $x\in I_j$ when $j$ is odd, and
$$
\sin(n_{k_j}x)\leq-\frac12
$$
for every $x\in I_j$ when $j$ is even.

::: pf-proof
Begin with the compact interval
$$
I_0=[0,1].
$$
Because $n_k\to\infty$, step [](#interval-with-sin-large){.pf-ref} permits choosing an index $k_1$ and a
nondegenerate closed interval $I_1\subseteq I_0$ on which
$$
\sin(n_{k_1}x)\geq\frac12.
$$

Suppose $k_j$ and $I_j$ have been chosen. Since the tail
$$
n_{k_j+1},n_{k_j+2},\ldots
$$
is still unbounded, choose $k_{j+1}>k_j$ sufficiently large that step [](#interval-with-sin-small){.pf-ref}
applies to $I_j$ when $j+1$ is even, or step [](#interval-with-sin-large){.pf-ref} applies when $j+1$ is
odd. The corresponding subinterval is $I_{j+1}$. This recursive
construction has all the stated properties.
:::

:::

::: {.pf-step #exists-nonconvergent-point}
There exists $x_0\in\RR$ such that the numerical sequence
$$
\sin(n_{k_j}x_0)
$$
does not converge.

::: pf-proof
The intervals in step [](#nested-intervals-exist){.pf-ref} are nonempty compact subsets of the compact
interval $I_0$ and are nested. Hence
$$
\bigcap_{j=1}^{\infty}I_j\neq\varnothing.
$$
Choose
$$
x_0\in\bigcap_{j=1}^{\infty}I_j.
$$
Then step [](#nested-intervals-exist){.pf-ref} gives
$$
\sin(n_{k_j}x_0)\geq\frac12
$$
for every odd $j$, while
$$
\sin(n_{k_j}x_0)\leq-\frac12
$$
for every even $j$. A sequence with these two infinite families of values
cannot converge.
:::

:::

::: {.pf-step #subsequence-not-convergent}
The original sequence $f_n(x)=\sin(nx)$ has no pointwise convergent
subsequence.

::: pf-proof
The subsequence $\sin(n_kx)$ was arbitrary. Step [](#exists-nonconvergent-point){.pf-ref} constructs a further
subsequence that fails to converge at the point $x_0$. If
$\sin(n_kx)$ converged pointwise, then every further subsequence would
converge at every point, in particular at $x_0$. This contradiction shows
that the arbitrary subsequence is not pointwise convergent.
:::

:::

::: pf-qed
Step [](#subsequence-not-convergent){.pf-ref} proves the required assertion.
:::

:::

:::

::: {.solution}

::: pf

::: {.pf-step #orthogonality-integral}
If $n\neq m$ are positive integers, then
$$
\int_0^{2\pi}(\sin nx-\sin mx)^2\,dx=2\pi.
$$

::: pf-proof
Expanding the square,
$$
\int_0^{2\pi}\sin^2 nx\,dx=\int_0^{2\pi}\sin^2 mx\,dx=\pi
\qquad\text{and}\qquad
\int_0^{2\pi}\sin nx\,\sin mx\,dx=0
$$
for $n\neq m$.
:::

:::

::: {.pf-step #l2-argument-conclusion}
For $n_1<n_2<\cdots$, the sequence $\sin(n_kx)$ does not converge
pointwise on $[0,2\pi]$.

::: pf-proof
Suppose it does. Then
$$
g_k(x)\coloneqq(\sin n_kx-\sin n_{k+1}x)^2
$$
tends to $0$ for every $x\in[0,2\pi]$, and $0\leq g_k\leq4$. By the
bounded convergence theorem on $[0,2\pi]$,
$\int_0^{2\pi}g_k\,dx\to0$. Since $n_k\neq n_{k+1}$, step [](#orthogonality-integral){.pf-ref} gives
$\int_0^{2\pi}g_k\,dx=2\pi$ for every $k$, a contradiction.
:::

:::

::: pf-qed
Every subsequence of $f_n$ has the form in step [](#l2-argument-conclusion){.pf-ref}.
:::

:::

:::
