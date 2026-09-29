---
schema: qual/card@1
id: P-BKF16-3A
kind: problem
title: Completeness of $K$-Lipschitz functions under locally uniform convergence
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
    Independently checked the retained Fall 2016 solution packet: the
    weighted compact sup norms are finite on K-Lipschitz functions, and a
    d-Cauchy sequence is uniformly Cauchy on every bounded interval.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked all metric axioms, compact-uniform convergence of a Cauchy
    sequence, preservation of the K-Lipschitz bound, and convergence in the
    weighted metric.
---

::: {.problem}
Given $K \geq 0$ , let $\mathrm { L i p } _ { K }$ be the set of functions $f : \mathbb { R } \to \mathbb { R }$ which satisfy $| f ( x ) - f ( y ) | \leq$ $K | x - y |$ for all $x , y \in \mathbb { R }$

(a) Show that the formula

$$
d ( f _ { 1 } , f _ { 2 } ) = \sum _ { j = 1 } ^ { \infty } 2 ^ { - j } \operatorname* { s u p } _ { z \in [ - j , j ] } | f _ { 1 } ( z ) - f _ { 2 } ( z ) |
$$

converges and defines a metric d on $\mathrm { L i p } _ { K }$

(b) Show that $\mathrm { L i p } _ { K }$ is a complete metric space with this metric.
:::

::: {.solution}
For $f,g\in\operatorname{Lip}_K$, put
$$
M_j(f,g)
\coloneqq
\sup_{z\in[-j,j]}\abs{f(z)-g(z)}.
$$
Then
$$
d(f,g)
=
\sum_{j=1}^{\infty}2^{-j}M_j(f,g).
$$

::: pf

::: {.pf-step #s1}

For every $f,g\in\operatorname{Lip}_K$ and every $j\ge1$,
$$
M_j(f,g)
\le
\abs{f(0)-g(0)}+2Kj.
$$

::: pf-proof

If $z\in[-j,j]$, then
$$
\begin{aligned}
\abs{f(z)-g(z)}
&\le
\abs{f(z)-f(0)}
+
\abs{f(0)-g(0)}
+
\abs{g(0)-g(z)}\\
&\le
K\abs z
+
\abs{f(0)-g(0)}
+
K\abs z\\
&\le
\abs{f(0)-g(0)}+2Kj.
\end{aligned}
$$
Taking the supremum over $[-j,j]$ proves the claim.

:::

:::

::: {.pf-step #s2}

The series defining $d(f,g)$ converges for every
$f,g\in\operatorname{Lip}_K$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
0
\le
2^{-j}M_j(f,g)
\le
2^{-j}\abs{f(0)-g(0)}
+
2Kj\,2^{-j}.
$$
Both
$$
\sum_{j=1}^{\infty}2^{-j}
\qquad\text{and}\qquad
\sum_{j=1}^{\infty}j2^{-j}
$$
converge. The comparison test therefore gives convergence of the
series defining $d(f,g)$.

:::

:::

::: {.pf-step #s3}

The function $d$ is nonnegative and symmetric, and
$$
d(f,g)=0
\quad\Longleftrightarrow\quad
f=g.
$$

::: pf-proof

Each summand is nonnegative and symmetric in $f,g$, so the same is
true of $d$.

If $f=g$, then every summand is $0$, hence $d(f,g)=0$. Conversely, if
$d(f,g)=0$, then a sum of nonnegative terms is zero, so
$$
M_j(f,g)=0
$$
for every $j$. Given any $z\in\RR$, choose an integer
$j\ge\abs z$. Then
$$
\abs{f(z)-g(z)}
\le
M_j(f,g)
=
0.
$$
Thus $f=g$ on $\RR$.

:::

:::

::: {.pf-step #s4}

The triangle inequality holds:
$$
d(f,h)
\le
d(f,g)+d(g,h).
$$

::: pf-proof

For every $z\in[-j,j]$,
$$
\abs{f(z)-h(z)}
\le
\abs{f(z)-g(z)}
+
\abs{g(z)-h(z)}.
$$
Taking suprema gives
$$
M_j(f,h)
\le
M_j(f,g)+M_j(g,h).
$$
Multiply by $2^{-j}$ and sum over $j\ge1$.

:::

:::

::: {.pf-step #s5}

Therefore the formula in the problem defines a metric on
$\operatorname{Lip}_K$.

::: pf-proof

Step [](#s2){.pf-ref} proves finiteness, while steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the metric
axioms. This completes part (a).

:::

:::

::: {.pf-step #s6}

Let $(f_m)$ be a $d$-Cauchy sequence. For every fixed $j\ge1$,
the sequence $(f_m)$ is uniformly Cauchy on $[-j,j]$.

::: pf-proof

For all $m,n$,
$$
d(f_m,f_n)
\ge
2^{-j}M_j(f_m,f_n).
$$
Hence
$$
M_j(f_m,f_n)
\le
2^j d(f_m,f_n).
$$
Since the right-hand side tends uniformly to $0$ as $m,n\to\infty$,
the restrictions to $[-j,j]$ form a uniformly Cauchy sequence.

:::

:::

::: {.pf-step #s7}

There is a function
$$
g:\RR\to\RR
$$
such that
$$
f_m\longrightarrow g
$$
uniformly on every interval $[-j,j]$.

::: pf-proof

For each fixed $j$, step [](#s6){.pf-ref} and completeness of $\RR$ imply that
the uniformly Cauchy sequence of real-valued functions on $[-j,j]$
has a uniform limit, call it $g_j$.

If $j<k$, both $g_j$ and the restriction of $g_k$ to $[-j,j]$ are
pointwise limits of the same sequence $(f_m)$, so they agree. The
compatible functions $g_j$ therefore define one function
$g:\RR\to\RR$, and the convergence to $g$ is uniform on every
$[-j,j]$.

:::

:::

::: {.pf-step #s8}

The limit function $g$ belongs to
$$
\operatorname{Lip}_K.
$$

::: pf-proof

Take $x,y\in\RR$ and choose $j$ with
$$
x,y\in[-j,j].
$$
By step [](#s7){.pf-ref},
$$
f_m(x)\to g(x),
\qquad
f_m(y)\to g(y).
$$
Since every $f_m$ is $K$-Lipschitz,
$$
\abs{f_m(x)-f_m(y)}
\le
K\abs{x-y}.
$$
Passing to the limit gives
$$
\abs{g(x)-g(y)}
\le
K\abs{x-y}.
$$

:::

:::

::: {.pf-step #s9}

For each fixed $n$ and $j$,
$$
M_j(f_n,f_m)
\longrightarrow
M_j(f_n,g)
$$
as $m\to\infty$.

::: pf-proof

For any functions $u,v,w$ on a set,
$$
\left|
\sup\abs{u-v}
-
\sup\abs{u-w}
\right|
\le
\sup\abs{v-w}.
$$
Apply this on $[-j,j]$ with
$$
u=f_n,\qquad v=f_m,\qquad w=g.
$$
The right-hand side tends to $0$ by the uniform convergence in step
[](#s7){.pf-ref}.

:::

:::

::: {.pf-step #s10}

One has
$$
d(f_n,g)\longrightarrow0.
$$

::: pf-proof

Let $\varepsilon>0$. Since $(f_m)$ is $d$-Cauchy, choose $N$ such
that
$$
d(f_n,f_m)<\varepsilon
$$
whenever $m,n\ge N$.

Fix $n\ge N$. By step [](#s9){.pf-ref} and Fatou's lemma for the nonnegative
series,
$$
\begin{aligned}
d(f_n,g)
&=
\sum_{j=1}^{\infty}
2^{-j}
\lim_{m\to\infty}M_j(f_n,f_m)\\
&\le
\liminf_{m\to\infty}
\sum_{j=1}^{\infty}
2^{-j}M_j(f_n,f_m)\\
&=
\liminf_{m\to\infty}d(f_n,f_m)\\
&\le
\varepsilon.
\end{aligned}
$$
Thus $d(f_n,g)\to0$.

:::

:::

::: {.pf-step #s11}

The metric space
$$
\boxed{(\operatorname{Lip}_K,d)}
$$
is complete.

::: pf-proof

Every $d$-Cauchy sequence has, by steps [](#s7){.pf-ref} and [](#s8){.pf-ref}, a limit
$g\in\operatorname{Lip}_K$, and step [](#s10){.pf-ref} shows convergence to that
limit in the metric $d$. This proves part (b).

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves part (a), and step [](#s11){.pf-ref} proves part (b).

:::

:::

:::
