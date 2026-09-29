---
schema: qual/card@1
id: P-HGRO23
kind: problem
title: A finite p-group has nontrivial center
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group of order $p^r$, where $p$ is prime.
Prove that $G$ has nontrivial center.
:::

::: {.solution}
Use the class equation for the conjugation action of $G$ on itself.

::: pf

::: {.pf-step #s1}

Every noncentral conjugacy class has cardinality divisible by $p$.

::: pf-proof

If $x\notin Z(G)$, then its conjugacy class has size
\[
[G:C_G(x)].
\]
Since $C_G(x)$ is a proper subgroup of the $p$-group $G$, this index is a power
of $p$ greater than $1$, hence is divisible by $p$.

:::

:::

::: pf-step

The order of the center is divisible by $p$.

::: pf-proof

The class equation is
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the $x_i$ represent the noncentral conjugacy classes. By step [](#s1){.pf-ref} every term
in the sum is divisible by $p$, and $|G|=p^r$ is divisible by $p$. Hence
\[
|Z(G)|\equiv0\pmod p.
\]

:::

:::

::: pf-step

Therefore $Z(G)$ is nontrivial.

::: pf-proof

Since $p$ divides $|Z(G)|$, we have $|Z(G)|\ge p>1$.

:::

:::

:::

:::
