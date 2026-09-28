---
schema: qual/card@1
id: P-BERK96S-06
kind: problem
title: Rational homogeneous systems with a complex solution have a rational solution
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
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified scalar-extension invariance of rank via minors and the
    rank-nullity argument producing a nonzero rational kernel vector.
---

::: {.problem}
Suppose a finite homogeneous system of linear equations with rational coefficients has a nonzero complex solution. Must it have a nonzero rational solution? Prove your answer or give a counterexample.
:::

::: {.solution}
Write the system as
$$
Ax=0,
$$
where $A\in M_{m\times n}(\QQ)$.

<1>1. The rank of $A$ over $\QQ$ equals its rank over $\CC$.

::: {.proof}
For each $k$, every $k\times k$ minor of $A$ is a rational number. Such a
minor is nonzero when regarded as an element of $\QQ$ if and only if it is
nonzero when regarded as an element of $\CC$. Since the rank is the largest
size of a nonzero minor, the two ranks are equal.
:::

<1>2. One has
$$
\rank_{\QQ}A<n.
$$

::: {.proof}
By hypothesis there is a nonzero vector
$$
v\in\CC^n
$$
with $Av=0$. Hence the complex-linear map defined by $A$ has nontrivial
kernel, so rank-nullity gives
$$
\rank_{\CC}A<n.
$$
Step <1>1 gives the same inequality over $\QQ$.
:::

<1>3. The system has a nonzero rational solution, so the answer is
$$
\boxed{\text{yes}}.
$$

::: {.proof}
By step <1>2 and rank-nullity over $\QQ$,
$$
\dim_{\QQ}\ker(A:\QQ^n\to\QQ^m)
=
n-\rank_{\QQ}A
>0.
$$
Thus this kernel contains a nonzero vector in $\QQ^n$, which is a nonzero
rational solution of the original system.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the required assertion.
:::
:::
