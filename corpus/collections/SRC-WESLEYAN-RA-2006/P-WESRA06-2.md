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

2. When $N=\mathbb R$ and $0<p<\infty$, determine for which $p$ the formula
   \[
   \|x\|_p:=|x|^p
   \]
   defines a norm.

3. Define a Banach space.

4. State the Hahn--Banach theorem for a normed linear space.

5. Let $B,B'$ be Banach spaces and let $T:B\to B'$ be a one-to-one continuous linear map onto $B'$.
   If $y_n=T(x_n)$ is Cauchy in $B'$, what can be concluded about $(x_n)$ in $B$, and why?
:::

::: {.solution}
<1>1. Definition of a norm.
::: {.proof}
A norm on $N$ is a function $\|\cdot\|:N\to[0,\infty)$ such that for all $x,y\in N$ and all real scalars $a$,
\[
\|x\|=0\iff x=0,
\qquad
\|ax\|=|a|\,\|x\|,
\qquad
\|x+y\|\le\|x\|+\|y\|.
\]
:::

<1>2. Determine the admissible exponent.
::: {.proof}
If $\|x\|_p=|x|^p$ is a norm, absolute homogeneity requires
\[
|ax|^p=|a|\,|x|^p
\]
for every $a,x\in\mathbb R$.
Taking $x=1$ and $a=2$ gives
\[
2^p=2,
\]
so $p=1$.

Conversely, when $p=1$, the formula is the usual absolute-value norm on $\mathbb R$.
Hence
\[
\boxed{\|x\|_p=|x|^p\text{ is a norm exactly when }p=1.}
\]
:::

<1>3. Definition of a Banach space.
::: {.proof}
A normed vector space is a Banach space if it is complete for the metric induced by its norm, equivalently if every norm-Cauchy sequence converges in norm to an element of the space.
:::

<1>4. Hahn--Banach theorem.
::: {.proof}
One standard real form is the following.
Let $X$ be a real normed vector space, let $M\subseteq X$ be a linear subspace, and let $f\in M^*$ be bounded.
Then there exists $F\in X^*$ such that
\[
F|_M=f
\qquad\text{and}\qquad
\|F\|=\|f\|.
\]
:::

<1>5. Pull the Cauchy sequence back through the inverse map.
::: {.proof}
The map $T:B\to B'$ is a bounded linear bijection between Banach spaces.
By the Open Mapping Theorem, its inverse
\[
T^{-1}:B'\to B
\]
is bounded.
Therefore there is $C>0$ such that
\[
\|x_n-x_m\|_B
=\|T^{-1}(y_n-y_m)\|_B
\le C\|y_n-y_m\|_{B'}.
\]
Since $(y_n)$ is Cauchy in $B'$, it follows that $(x_n)$ is Cauchy in $B$.
Because $B$ is complete, $(x_n)$ converges in $B$.
:::
:::
