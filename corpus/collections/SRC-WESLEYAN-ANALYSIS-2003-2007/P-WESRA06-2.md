---
schema: qual/card@1
id: P-WESRA06-2
kind: problem
title: Norms, Banach spaces, Hahn--Banach, and inverse continuity
classification:
  areas: [real-analysis]
  topics: [Functional Analysis, Banach Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $N$ be a real vector space.

1. Define a norm on $N$.

2. When $N=\RR$ and $0<p<\infty$, determine for which $p$ the formula
   $$
   \norm{x}_p:=\abs{x}^p
   $$
   defines a norm.

3. Define a Banach space.

4. State the Hahn--Banach theorem for a normed linear space.

5. Let $B,B'$ be Banach spaces and let $T:B\to B'$ be a one-to-one continuous linear map onto $B'$.
   If $y_n=T(x_n)$ is Cauchy in $B'$, what can be concluded about $(x_n)$ in $B$, and why?
:::

::: {.solution}

::: pf

::: pf-step

Definition of a norm.

::: pf-proof

A norm on $N$ is a function $\norm{\cdot}:N\to[0,\infty)$ such that for all $x,y\in N$ and all real scalars $a$,
$$
\norm{x}=0\iff x=0,
\qquad
\norm{ax}=\abs{a}\,\norm{x},
\qquad
\norm{x+y}\le\norm{x}+\norm{y}.
$$

:::

:::

::: pf-step

Determine the admissible exponent.

::: pf-proof

If $\norm{x}_p=\abs{x}^p$ is a norm, absolute homogeneity requires
$$
\abs{ax}^p=\abs{a}\,\abs{x}^p
$$
for every $a,x\in\RR$.
Taking $x=1$ and $a=2$ gives
$$
2^p=2,
$$
so $p=1$.

Conversely, when $p=1$, the formula is the usual absolute-value norm on $\RR$.
Hence
$$
\boxed{\norm{x}_p=\abs{x}^p\text{ is a norm exactly when }p=1.}
$$

:::

:::

::: pf-step

Definition of a Banach space.

::: pf-proof

A normed vector space is a Banach space if it is complete for the metric induced by its norm, equivalently if every norm-Cauchy sequence converges in norm to an element of the space.

:::

:::

::: pf-step

Hahn--Banach theorem.

::: pf-proof

One standard real form is the following.
Let $X$ be a real normed vector space, let $M\subseteq X$ be a linear subspace, and let $f\in M^*$ be bounded.
Then there exists $F\in X^*$ such that
$$
F\restrict_M=f
\qquad\text{and}\qquad
\norm{F}=\norm{f}.
$$

:::

:::

::: pf-step

Pull the Cauchy sequence back through the inverse map.

::: pf-proof

The map $T:B\to B'$ is a bounded linear bijection between Banach spaces.
By the Open Mapping Theorem, its inverse
$$
T^{-1}:B'\to B
$$
is bounded.
Therefore there is $C>0$ such that
$$
\norm{x_n-x_m}_B
=\norm{T^{-1}(y_n-y_m)}_B
\le C\norm{y_n-y_m}_{B'}.
$$
Since $(y_n)$ is Cauchy in $B'$, it follows that $(x_n)$ is Cauchy in $B$.
Because $B$ is complete, $(x_n)$ converges in $B$.

:::

:::

:::

:::
