---
schema: qual/card@1
id: P-ZBTCU
kind: problem
title: The Sylow theorems
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
relations: []
review: draft
---

::: {.problem}
State the three Sylow theorems.
:::

::: {.solution}
Let $G$ be a finite group, let $p$ be a prime, and write $\abs{G}=p^n m$ with $p\nmid m$. A subgroup of order $p^n$ is a Sylow $p$-subgroup, and $n_p$ denotes the number of Sylow $p$-subgroups of $G$.

::: pf

::: pf-step

(Existence) $G$ has a subgroup of order $p^n$.

:::

::: {.pf-step #conjugacy}

(Conjugacy and containment) Every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup, and any two Sylow $p$-subgroups are conjugate in $G$.

:::

::: pf-step

(Number) $n_p\equiv1\pmod p$ and $n_p\mid m$.

:::

::: pf-step

In particular, $n_p=1$ if and only if a Sylow $p$-subgroup is normal in $G$.

::: pf-proof

By step [](#conjugacy){.pf-ref}, the Sylow $p$-subgroups form one conjugacy class, so there is only one exactly when a Sylow $p$-subgroup equals all its conjugates, that is, when it is normal.

:::

:::

:::

:::
