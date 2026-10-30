---
schema: qual/card@1
id: P-UCLARA18S-09
kind: problem
title: The Weierstrass product $\prod(1+\frac1n)^z(1-\frac zn)$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Consider the formal product
$$
\prod_{n=1}^{\infty}\left(1+\frac1n\right)^z\left(1-\frac zn\right).
$$

(a) Show that the product converges for every $z\in(-\infty,0)$.

(b) Show that the resulting function extends from this interval to an entire function of $z\in\CC$.
:::

::: {.solution}

For $n\ge1$, define the entire function
$$
q_n(z)
=
\left(1+\frac1n\right)^z
\left(1-\frac zn\right)
=
e^{z a_n}
\left(1-\frac zn\right),
\qquad
a_n=\log\left(1+\frac1n\right).
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\boxed{
\abs{
a_n-\frac1n
}
\le
\frac1{2n^2}}.
$$


::: pf-proof

Using
$$
\log(1+x)
=
\int_0^x\frac{dt}{1+t},
$$
one obtains
$$
\begin{aligned}
\frac1n-a_n
&=
\int_0^{1/n}
\left(
1-\frac1{1+t}
\right)dt\\
&=
\int_0^{1/n}
\frac{t}{1+t}\,dt.
\end{aligned}
$$
The integrand is nonnegative and at most $t$, so
$$
0
\le
\frac1n-a_n
\le
\int_0^{1/n}t\,dt
=
\frac1{2n^2}.
$$

:::

:::

::: {.pf-step #s1-2}

Fix $R>0$. There is a constant $C_R$ such that for every
$$
\abs{z}\le R
$$
and all sufficiently large $n$,
$$
\boxed{
\abs{q_n(z)-1}
\le
\frac{C_R}{n^2}}.
$$


::: pf-proof

Write
$$
w=za_n.
$$
For $n$ sufficiently large,
$$
\abs{w}
\le
\frac{2R}{n}.
$$
Using
$$
\abs{e^w-1-w}
\le
\frac12\abs{w}^2e^{\abs{w}},
$$
step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
\abs{
e^{za_n}-1-\frac zn
}
&\le
\abs{e^{za_n}-1-za_n}
+
\abs{z}
\abs{
a_n-\frac1n
}\\
&\le
\frac{C_R'}{n^2}.
\end{aligned}
$$
Also
$$
\abs{e^{za_n}-1}
\le
\abs{za_n}e^{\abs{za_n}}
\le
\frac{C_R''}{n}.
$$
Now
$$
\begin{aligned}
q_n(z)-1
&=
e^{za_n}
\left(1-\frac zn\right)-1\\
&=
\left(
e^{za_n}-1-\frac zn
\right)
-
\frac zn
\left(
e^{za_n}-1
\right).
\end{aligned}
$$
The first term is $O_R(n^{-2})$, and the second is also
$O_R(n^{-2})$. This proves the bound.

:::

:::

::: {.pf-step #s1-3}

For every compact set $K\subset\CC$,
$$
\boxed{
\sum_{n=1}^{\infty}
\sup_{z\in K}\abs{q_n(z)-1}
<\infty}.
$$


::: pf-proof

Choose $R$ with
$$
K\subseteq\{z:\abs{z}\le R\}.
$$
Step [](#s1-2){.pf-ref} bounds the tail by a constant multiple of
$$
\sum_{n=1}^{\infty}\frac1{n^2},
$$
and the finitely many initial terms cause no problem.

:::

:::

::: {.pf-step #s1-4}

The partial products
$$
P_N(z)
=
\prod_{n=1}^{N}q_n(z)
$$
converge uniformly on every compact subset of $\CC$.


::: pf-proof

Fix a compact $K$. Put
$$
u_n(z)=q_n(z)-1.
$$
By step [](#s1-3){.pf-ref},
$$
\sum_n\norm{u_n}_{K,\infty}<\infty.
$$
For $M>N$,
$$
\prod_{n=N+1}^{M}(1+u_n(z))-1
$$
has absolute value at most
$$
\exp\left(
\sum_{n=N+1}^{M}\abs{u_n(z)}
\right)-1.
$$
The right-hand side tends uniformly to $0$ on $K$ as $N\to\infty$.
The initial product
$$
\prod_{n=1}^{N}q_n
$$
is uniformly bounded on $K$, since
$$
\prod_{n=1}^{N}\abs{q_n(z)}
\le
\prod_{n=1}^{N}(1+\abs{u_n(z)})
\le
\exp\left(
\sum_{n=1}^{\infty}\norm{u_n}_{K,\infty}
\right).
$$
Hence $(P_N)$ is uniformly Cauchy on $K$.

:::

:::

::: {.pf-step #s1-5}

The locally uniform limit
$$
\boxed{
P(z)
=
\prod_{n=1}^{\infty}
\left(1+\frac1n\right)^z
\left(1-\frac zn\right)}
$$
is entire on $\CC$.


::: pf-proof

Each finite product $P_N$ is entire because every $q_n$ is entire.
Step [](#s1-4){.pf-ref} gives locally uniform convergence on $\CC$. By the
Weierstrass theorem, the locally uniform limit $P$ is entire.

:::

:::

::: {.pf-step #s1-6}

Fix $z<0$. Then every factor $q_n(z)$ is positive.


::: pf-proof

For real $z<0$,
$$
\left(1+\frac1n\right)^z>0
$$
and
$$
1-\frac zn>1>0.
$$
Thus their product is positive.

:::

:::

::: {.pf-step #s1-7}

For each fixed $z<0$, the infinite product converges to a strictly
positive finite number.


::: pf-proof

Step [](#s1-2){.pf-ref}, applied to the compact singleton $\{z\}$, gives
$$
\sum_{n=1}^{\infty}\abs{q_n(z)-1}<\infty.
$$
Hence $q_n(z)\to1$. For all sufficiently large $n$,
$$
\abs{q_n(z)-1}\le\frac12.
$$
Since the factors are positive by step [](#s1-6){.pf-ref}, the real logarithm is defined,
and
$$
\abs{\log q_n(z)}
\le
2\abs{q_n(z)-1}.
$$
Thus
$$
\sum_n\log q_n(z)
$$
converges, and therefore
$$
\prod_nq_n(z)
=
\exp\left(
\sum_n\log q_n(z)
\right)
$$
converges to a positive finite number.

:::

:::

::: {.pf-step #s1-8}

Part (a) holds for every $z\in(-\infty,0)$.


::: pf-proof

This is exactly step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The function obtained in part (a) extends to the entire function $P$
from step [](#s1-5){.pf-ref}.


::: pf-proof

For every negative real $z$, both constructions are limits of the same
partial products
$$
P_N(z).
$$
Hence the entire function $P$ restricts on $(-\infty,0)$ to the
convergent product from part (a).

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves part (a), and steps [](#s1-5){.pf-ref} and [](#s1-9){.pf-ref} prove part (b).

:::

:::

:::
