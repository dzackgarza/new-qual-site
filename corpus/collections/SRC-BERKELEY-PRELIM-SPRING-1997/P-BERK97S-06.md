---
schema: qual/card@1
id: P-BERK97S-06
kind: problem
title: Interpolation basis for a finite-dimensional space of continuous functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $X$ be a topological space and let $V$ be an $n$-dimensional subspace of the real vector space of continuous functions on $X$.
Prove that there are a basis
\[
\{f_1,\dots,f_n\}
\]
of $V$ and points $x_1,\dots,x_n\in X$ such that
\[
f_i(x_j)=\delta_{ij}.
\]
:::

::: {.solution}
For each $x\in X$, let
$$
\operatorname{ev}_x:V\longrightarrow\RR,
\qquad
\operatorname{ev}_x(f)=f(x)
$$
be the evaluation functional.

::: pf

::: {.pf-step #s1}

The evaluation functionals span $V^*$:
$$
\spanof\{\operatorname{ev}_x:x\in X\}=V^*.
$$

::: pf-proof

Let
$$
W\coloneqq\spanof\{\operatorname{ev}_x:x\in X\}\subseteq V^*.
$$
Suppose $W\neq V^*$.
Since $V$ is finite-dimensional, the annihilator
$$
W^\perp
=
\{f\in V:\lambda(f)=0\text{ for every }\lambda\in W\}
$$
is then nonzero.
Choose $0\neq f\in W^\perp$.
For every $x\in X$,
$$
f(x)=\operatorname{ev}_x(f)=0,
$$
because $\operatorname{ev}_x\in W$.
Hence $f$ is the zero function, a contradiction.
Thus $W=V^*$.

:::

:::

::: {.pf-step #s2}

There are points $x_1,\ldots,x_n\in X$ such that
$$
\operatorname{ev}_{x_1},\ldots,\operatorname{ev}_{x_n}
$$
is a basis of $V^*$.

::: pf-proof

By step [](#s1){.pf-ref}, the family of all evaluation functionals spans the $n$-dimensional vector space $V^*$.
A spanning family in a finite-dimensional vector space contains a basis, so choose $n$ evaluations forming one.

:::

:::

::: {.pf-step #s3}

There is a basis $f_1,\ldots,f_n$ of $V$ satisfying
$$
f_i(x_j)=\delta_{ij}.
$$

::: pf-proof

Define
$$
T:V\longrightarrow\RR^n,
\qquad
T(f)=\bigl(f(x_1),\ldots,f(x_n)\bigr).
$$
If $T(f)=0$, then
$$
\operatorname{ev}_{x_j}(f)=0
$$
for every $j$.
Since the functionals in step [](#s2){.pf-ref} form a basis of $V^*$, every element of $V^*$ vanishes on $f$, hence $f=0$.
Thus $T$ is injective.
Both $V$ and $\RR^n$ have dimension $n$, so $T$ is an isomorphism.

For the standard basis $e_1,\ldots,e_n$ of $\RR^n$, put
$$
f_i\coloneqq T^{-1}(e_i).
$$
Then $f_1,\ldots,f_n$ is a basis of $V$, and the $j$-th coordinate of $T(f_i)=e_i$ gives
$$
f_i(x_j)=\delta_{ij}.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} constructs the required basis and points.

:::

:::

:::
