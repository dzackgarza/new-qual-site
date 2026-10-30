---
schema: qual/card@1
id: P-UCLARA14S-04
kind: problem
title: 'Functionals on $C([0,1])$ and $L^\infty$ not represented by $L^1$ densities'
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
Let $(a_n)\subset[0,1]$ and define, for $f\in C([0,1])$,
$$
\varphi(f)=\sum_{n=1}^{\infty}2^{-n}f(a_n).
$$

(a) Prove that there is no $g\in L^1([0,1])$ such that
$$
\varphi(f)=\int_0^1 f(x)g(x)\,dx
$$
for every $f\in C([0,1])$.

(b) Each $g\in L^1([0,1])$ defines a continuous functional $T_g$ on $L^\infty([0,1])$ by
$$
T_g(f)=\int_0^1 f(x)g(x)\,dx.
$$
Prove that there are continuous linear functionals on $L^\infty([0,1])$ that are not of this form.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The functional
$$
\varphi:C([0,1])\to\CC
$$
is bounded and satisfies
$$
\norm{\varphi}\le1.
$$


::: pf-proof

For $f\in C([0,1])$,
$$
\begin{aligned}
\abs{\varphi(f)}
&\le
\sum_{n=1}^{\infty}2^{-n}\abs{f(a_n)}\\
&\le
\norm{f}_\infty
\sum_{n=1}^{\infty}2^{-n}\\
&=
\norm{f}_\infty.
\end{aligned}
$$
Thus $\varphi$ is continuous.

:::

:::

::: {.pf-step #s1-2}

There is a sequence $(f_k)\subset C([0,1])$ such that
$$
0\le f_k\le1,
\qquad
f_k(a_1)=1,
$$
and
$$
f_k(x)\longrightarrow0
$$
for every $x\ne a_1$.


::: pf-proof

Define
$$
f_k(x)
\coloneqq
\max\{1-k\abs{x-a_1},0\}.
$$
Each $f_k$ is continuous, takes values in $[0,1]$, and satisfies $f_k(a_1)=1$. If $x\ne a_1$, then for all sufficiently large $k$ one has
$$
k\abs{x-a_1}>1,
$$
so $f_k(x)=0$.

:::

:::

::: {.pf-step #s1-3}

For every $k$,
$$
\varphi(f_k)\ge\frac12.
$$


::: pf-proof

All terms in
$$
\varphi(f_k)
=
\sum_{n=1}^{\infty}2^{-n}f_k(a_n)
$$
are nonnegative, and the $n=1$ term equals
$$
2^{-1}f_k(a_1)=\frac12.
$$

:::

:::

::: {.pf-step #s1-4}

There is no $g\in L^1([0,1])$ such that
$$
\varphi(f)
=
\int_0^1f(x)g(x)\,dx
$$
for every $f\in C([0,1])$.


::: pf-proof

Suppose such a $g$ existed. By step [](#s1-2){.pf-ref},
$$
f_k(x)g(x)\longrightarrow0
$$
for almost every $x\in[0,1]$, because the only possible exceptional point is $a_1$. Also
$$
\abs{f_k(x)g(x)}
\le
\abs{g(x)},
$$
and $g\in L^1([0,1])$. Dominated convergence therefore gives
$$
\int_0^1f_k(x)g(x)\,dx
\longrightarrow0.
$$
Under the assumed representation, this says
$$
\varphi(f_k)\longrightarrow0,
$$
contradicting step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Regard $C([0,1])$ as a closed linear subspace of $L^\infty([0,1])$ via the natural inclusion. The functional $\varphi$ extends to a bounded linear functional
$$
\widetilde\varphi\in(L^\infty([0,1]))^*.
$$


::: pf-proof

For a continuous function on $[0,1]$, the supremum norm equals the essential supremum norm, so the natural map
$$
C([0,1])\hookrightarrow L^\infty([0,1])
$$
is isometric. By step [](#s1-1){.pf-ref}, $\varphi$ is bounded on this subspace. The Hahn--Banach theorem therefore gives a bounded linear extension $\widetilde\varphi$ to all of $L^\infty([0,1])$.

:::

:::

::: {.pf-step #s1-6}

The functional $\widetilde\varphi$ is not equal to $T_g$ for any $g\in L^1([0,1])$.


::: pf-proof

If
$$
\widetilde\varphi=T_g
$$
for some $g\in L^1([0,1])$, then restricting both sides to $C([0,1])$ would give
$$
\varphi(f)
=
\int_0^1f(x)g(x)\,dx
$$
for every continuous $f$. This contradicts step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} prove part (b).

:::

:::

:::
