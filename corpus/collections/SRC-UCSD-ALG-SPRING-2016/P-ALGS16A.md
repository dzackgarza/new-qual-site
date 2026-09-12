---
schema: qual/card@1
id: P-ALGS16A
kind: problem
title: $p$-groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $p$ be a prime number and let $G$ be a $p$-group.
Prove that $G$ is nilpotent.
:::

::: {.solution}
<1>1. Let
\[
1=Z_0(G)\le Z_1(G)\le Z_2(G)\le\cdots
\]
be the upper central series, defined inductively by
\[
Z_{i+1}(G)/Z_i(G)=Z\bigl(G/Z_i(G)\bigr).
\]
::: {.proof}
This is the definition of the upper central series.
A group is nilpotent precisely when this series reaches the whole group after finitely many steps.
:::

<1>2. If \(Z_i(G)\neq G\), then \(G/Z_i(G)\) is a nontrivial finite \(p\)-group.
::: {.proof}
Every quotient of a finite \(p\)-group is again a finite \(p\)-group.
Since \(Z_i(G)\neq G\), the quotient is nontrivial.
:::

<1>3. Hence, whenever \(Z_i(G)\neq G\), one has
\[
Z_i(G)<Z_{i+1}(G).
\]
::: {.proof}
Every nontrivial finite \(p\)-group has nontrivial center.
Applying this to \(G/Z_i(G)\), Step <1>2 gives
\[
Z\bigl(G/Z_i(G)\bigr)\neq 1.
\]
By the defining equality in Step <1>1, this means \(Z_{i+1}(G)/Z_i(G)\neq 1\), hence \(Z_i(G)<Z_{i+1}(G)\).
:::

<1>4. The upper central series must therefore reach \(G\) after finitely many steps.
::: {.proof}
As long as it has not reached \(G\), Step <1>3 gives a strict increase in subgroup order.
Since \(G\) is finite, there cannot be infinitely many strict subgroup inclusions.
Thus \(Z_c(G)=G\) for some finite \(c\).
:::

<1>5. Therefore \(G\) is nilpotent.
::: {.proof}
By Step <1>4, the upper central series terminates at \(G\), which is the defining criterion for nilpotence.
:::
:::
