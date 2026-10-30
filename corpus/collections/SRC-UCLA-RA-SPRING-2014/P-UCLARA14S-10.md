---
schema: qual/card@1
id: P-UCLARA14S-10
kind: problem
title: A dense boundary pole set prevents analytic continuation
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $\alpha\in[0,1]\setminus\QQ$ and let $(a_n)\in\ell^1(\NN)$ with $a_n\ne0$ for all $n$.
Show that
$$
f(z)=\sum_{n\ge1}\frac{a_n}{z-e^{i\alpha n}}
$$
converges and defines a function analytic in the unit disk $\DD$, and that $f$ admits no analytic continuation to any domain properly containing $\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The natural-boundary assertion is false under the literal hypothesis
$$
\alpha\in[0,1]\setminus\QQ.
$$


::: pf-proof

Take
$$
\alpha=\frac\pi5,
\qquad
a_n=2^{-n}.
$$
Then $\alpha\in[0,1]\setminus\QQ$, but
$$
e^{i\alpha n}
=
e^{2\pi i n/10}
$$
takes only ten distinct values.

For $1\le j\le10$, set
$$
\zeta_j=e^{2\pi i j/10},
\qquad
b_j
\coloneqq
\sum_{m=0}^{\infty}2^{-(j+10m)}.
$$
Each $b_j$ is positive. Since the original series is absolutely convergent on compact subsets of $\DD$, terms may be grouped by residue class modulo $10$, giving
$$
f(z)
=
\sum_{j=1}^{10}
\frac{b_j}{z-\zeta_j}
\qquad
(z\in\DD).
$$
The right-hand side is a rational function, holomorphic on
$$
\CC\setminus\{\zeta_1,\dots,\zeta_{10}\}.
$$
Choose any point of the unit circle not among these ten poles and a sufficiently small disk around it avoiding all poles. The union of that disk with $\DD$ is a domain properly containing $\DD$ on which the rational expression gives an analytic continuation of $f$. Thus the literal claim is false.

:::

:::

::: {.pf-step #s1-2}

The intended statement is correct under the corrected hypothesis
$$
\frac{\alpha}{2\pi}\notin\QQ.
$$
Assume this hypothesis for the remainder of the proof.


::: pf-proof

The correction is exactly the condition that the rotation
$$
z\longmapsto e^{i\alpha}z
$$
have infinite order. Under it, the points
$$
\zeta_n
\coloneqq
e^{i\alpha n}
$$
are pairwise distinct and dense in the unit circle.

:::

:::

::: {.pf-step #s1-3}

Under the corrected hypothesis, the series
$$
f(z)
=
\sum_{n=1}^{\infty}
\frac{a_n}{z-\zeta_n}
$$
converges uniformly on compact subsets of $\DD$.


::: pf-proof

Fix $0<r<1$. For $\abs{z}\le r$ and every $n$,
$$
\abs{z-\zeta_n}
\ge
1-\abs{z}
\ge
1-r.
$$
Hence
$$
\abs{
\frac{a_n}{z-\zeta_n}
}
\le
\frac{\abs{a_n}}{1-r}.
$$
Since $(a_n)\in\ell^1$, the Weierstrass M-test gives uniform absolute convergence on $\abs{z}\le r$. Every compact subset of $\DD$ is contained in such a disk, so the convergence is locally uniform.

:::

:::

::: {.pf-step #s1-4}

Under the corrected hypothesis, $f$ is holomorphic on $\DD$.


::: pf-proof

Each summand
$$
z\longmapsto
\frac{a_n}{z-\zeta_n}
$$
is holomorphic on $\DD$, because $\abs{\zeta_n}=1$. By step [](#s1-3){.pf-ref}, the series converges uniformly on compact subsets. A locally uniform limit of holomorphic functions is holomorphic.

:::

:::

::: {.pf-step #s1-5}

Let $\Omega$ be a domain properly containing $\DD$. Then $\Omega$ contains at least one point $\zeta_k=e^{i\alpha k}$.


::: pf-proof

Because $\Omega$ properly contains $\DD$, it contains a point $w\notin\DD$. If $\abs{w}=1$, openness of $\Omega$ gives a nearby point of modulus greater than $1$ that also lies in $\Omega$. Thus $\Omega$ contains a point outside the closed unit disk as well as points inside $\DD$.

Open connected subsets of $\CC$ are path connected, so a path in $\Omega$ from an interior point of $\DD$ to a point outside the closed unit disk must meet the unit circle. Thus $\Omega$ contains some point of $\partial\DD$.

Since $\Omega$ is open, it contains a nonempty open arc of the unit circle around that boundary point. By density of the set $\{\zeta_n\}$ from step [](#s1-2){.pf-ref}, that arc contains some $\zeta_k$.

:::

:::

::: {.pf-step #s1-6}

Suppose, toward a contradiction, that $f$ has a holomorphic continuation $F$ to such a domain $\Omega$. For the index $k$ from step [](#s1-5){.pf-ref}$, define
$$
G(z)
\coloneqq
(z-\zeta_k)F(z).
$$
Then
$$
G(\zeta_k)=0.
$$


::: pf-proof

The function $F$ is holomorphic at $\zeta_k\in\Omega$, so $G$ is holomorphic there and the factor $z-\zeta_k$ vanishes at $z=\zeta_k$.

:::

:::

::: {.pf-step #s1-7}

For $0<r<1$,
$$
G(r\zeta_k)
=
a_k
+
\sum_{n\ne k}
a_n
\frac{(r-1)\zeta_k}
{r\zeta_k-\zeta_n}.
$$


::: pf-proof

Inside $\DD$, the continuation $F$ agrees with the original function $f$. Thus
$$
\begin{aligned}
G(r\zeta_k)
&=
(r\zeta_k-\zeta_k)
\sum_{n=1}^{\infty}
\frac{a_n}{r\zeta_k-\zeta_n}\\
&=
a_k
+
\sum_{n\ne k}
a_n
\frac{(r-1)\zeta_k}
{r\zeta_k-\zeta_n}.
\end{aligned}
$$
The series is absolutely convergent for each fixed $r<1$ by step [](#s1-3){.pf-ref}, so the algebraic separation of the $k$-th term is justified.

:::

:::

::: {.pf-step #s1-8}

For every $n\ne k$ and every $0<r<1$,
$$
\abs{
\frac{(r-1)\zeta_k}
{r\zeta_k-\zeta_n}
}
\le1,
$$
and for each fixed $n\ne k$ this quantity tends to $0$ as $r\uparrow1$.


::: pf-proof

Since $\abs{\zeta_k}=\abs{\zeta_n}=1$,
$$
\abs{r\zeta_k-\zeta_n}
\ge
\abs{\abs{\zeta_n}-\abs{r\zeta_k}}
=
1-r.
$$
The numerator has modulus $1-r$, proving the bound.

For fixed $n\ne k$, pairwise distinctness from step [](#s1-2){.pf-ref} gives
$$
\zeta_k-\zeta_n\ne0.
$$
Hence the denominator tends to this nonzero number while the numerator tends to $0$, so the quotient tends to $0$.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\lim_{r\uparrow1}G(r\zeta_k)
=
a_k.
$$


::: pf-proof

By steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref},
$$
\abs{
a_n
\frac{(r-1)\zeta_k}
{r\zeta_k-\zeta_n}
}
\le
\abs{a_n}
\qquad
(n\ne k).
$$
The sequence $(\abs{a_n})$ is summable, and each summand tends to $0$ for fixed $n\ne k$. Dominated convergence for series therefore gives
$$
\sum_{n\ne k}
a_n
\frac{(r-1)\zeta_k}
{r\zeta_k-\zeta_n}
\longrightarrow0.
$$
Substitute into step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The assumed continuation leads to a contradiction.


::: pf-proof

Since $G$ is holomorphic on $\Omega$, it is continuous at $\zeta_k$. Therefore
$$
\lim_{r\uparrow1}G(r\zeta_k)
=
G(\zeta_k)
=0
$$
by step [](#s1-6){.pf-ref}. But step [](#s1-9){.pf-ref} gives the same limit as
$$
a_k\ne0.
$$
This is a contradiction.

:::

:::

::: {.pf-step #s1-11}

Under the corrected hypothesis $\alpha/(2\pi)\notin\QQ$, the unit circle is a natural boundary for $f$.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-10){.pf-ref} show that no domain properly containing $\DD$ can support a holomorphic continuation of $f$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} refutes the literal source statement. Steps [](#s1-2){.pf-ref} through [](#s1-11){.pf-ref} prove the intended theorem under the minimal density hypothesis $\alpha/(2\pi)\notin\QQ$.

:::

:::

:::
