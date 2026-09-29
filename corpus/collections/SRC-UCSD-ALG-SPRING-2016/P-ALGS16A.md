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

::: {.problem}
Let $p$ be a prime number and let $G$ be a $p$-group.
Prove that $G$ is nilpotent.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
\[
1=Z_0(G)\le Z_1(G)\le Z_2(G)\le\cdots
\]
be the upper central series, defined inductively by
\[
Z_{i+1}(G)/Z_i(G)=Z\bigl(G/Z_i(G)\bigr).
\]

::: pf-proof

This is the definition of the upper central series.
A group is nilpotent precisely when this series reaches the whole group after finitely many steps.

:::

:::

::: {.pf-step #s2}

If \(Z_i(G)\neq G\), then \(G/Z_i(G)\) is a nontrivial finite \(p\)-group.

::: pf-proof

Every quotient of a finite \(p\)-group is again a finite \(p\)-group.
Since \(Z_i(G)\neq G\), the quotient is nontrivial.

:::

:::

::: {.pf-step #s3}

Hence, whenever \(Z_i(G)\neq G\), one has
\[
Z_i(G)<Z_{i+1}(G).
\]

::: pf-proof

Every nontrivial finite \(p\)-group has nontrivial center.
Applying this to \(G/Z_i(G)\), Step [](#s2){.pf-ref} gives
\[
Z\bigl(G/Z_i(G)\bigr)\neq 1.
\]
By the defining equality in Step [](#s1){.pf-ref}, this means \(Z_{i+1}(G)/Z_i(G)\neq 1\), hence \(Z_i(G)<Z_{i+1}(G)\).

:::

:::

::: {.pf-step #s4}

The upper central series must therefore reach \(G\) after finitely many steps.

::: pf-proof

As long as it has not reached \(G\), Step [](#s3){.pf-ref} gives a strict increase in subgroup order.
Since \(G\) is finite, there cannot be infinitely many strict subgroup inclusions.
Thus \(Z_c(G)=G\) for some finite \(c\).

:::

:::

::: pf-step

Therefore \(G\) is nilpotent.

::: pf-proof

By Step [](#s4){.pf-ref}, the upper central series terminates at \(G\), which is the defining criterion for nilpotence.

:::

:::

:::

:::
