---
schema: qual/card@1
id: P-ALGS05D
kind: problem
title: "A finite abelian group with a unique subgroup of each order is cyclic"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $G$ be a finite abelian group of order $n$.
Suppose that $G$ has a unique subgroup of order $d$ for each positive divisor $d$ of $n$.
Prove that $G$ is cyclic.
:::

::: {.solution}
<1>1. Write $G$ as a direct product of cyclic groups of prime-power order: $G \cong \prod_i \mathbb{Z}/p_i^{e_i}$.
::: {.proof}
fundamental theorem of finite abelian groups.
:::

<1>2. Suppose for contradiction that $G$ is not cyclic, so some prime $p$ appears in at least two cyclic factors (i.e. $G$ has a subgroup isomorphic to $\mathbb{Z}/p \times \mathbb{Z}/p$).
::: {.proof}
$G$ is cyclic iff no prime appears in more than one factor.
:::

<1>3. Then $G$ has at least two distinct subgroups of order $p$ (the subgroups $\mathbb{Z}/p \times 0$ and $0 \times \mathbb{Z}/p$ inside $\mathbb{Z}/p \times \mathbb{Z}/p$).
::: {.proof}
<1>2.
:::

<1>4. This contradicts the hypothesis that $G$ has a unique subgroup of order $p$ (where $p$ is a divisor of $n$).
::: {.proof}
<1>3 and the hypothesis.
:::

<1>5. Hence $G$ is cyclic.
::: {.proof}
<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
