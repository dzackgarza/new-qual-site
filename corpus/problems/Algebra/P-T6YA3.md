---
schema: qual/card@1
id: P-T6YA3
kind: problem
title: The $R/(p)$-module structure on $A/pA$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Vector Spaces
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring with identity, $p \in R$ an element, and $A$ an $R$-module.
Show that the quotient group $A/pA$ is naturally an $R/(p)$-module with scalar multiplication defined by
$$
(r + (p)) \cdot (a + pA) = ra + pA.
$$
In particular, show that if $(p)$ is a maximal ideal, $A/pA$ is a vector space over the field $R/(p)$.
:::

::: {.solution}

::: pf

::: pf-step
The scalar multiplication $(r + (p)) \cdot (a + pA) = ra + pA$ is well defined.

::: pf-proof
Suppose $r + (p) = r' + (p)$ and $a + pA = a' + pA$.
Then $r - r' = cp$ for some $c \in R$, and $a - a' = pu$ for some $u \in A$.
Hence
$$
ra - r'a' = r(a - a') + (r - r')a' = r(pu) + (cp)a' = p(ru + ca') \in pA,
$$
so $ra + pA = r'a' + pA$, and the product does not depend on the choice of coset representatives.
:::

:::

::: pf-step
This scalar multiplication makes $A/pA$ an $R/(p)$-module.

::: pf-proof
Each module axiom for $A/pA$ is the image in $A/pA$ of the same axiom for the $R$-module $A$:
$$
\begin{aligned}
(r + (p)) \cdot \bigl((a + pA) + (b + pA)\bigr) &= r(a+b) + pA = (ra + pA) + (rb + pA),\\
\bigl((r + (p)) + (s + (p))\bigr) \cdot (a + pA) &= (r+s)a + pA = (ra + pA) + (sa + pA),\\
\bigl((r + (p))(s + (p))\bigr) \cdot (a + pA) &= (rs)a + pA = (r + (p)) \cdot (sa + pA),\\
(1 + (p)) \cdot (a + pA) &= 1a + pA = a + pA.
\end{aligned}
$$
:::

:::

::: pf-step
If $(p)$ is a maximal ideal, then $A/pA$ is a vector space over the field $R/(p)$.

::: pf-proof
The quotient of a commutative ring by a maximal ideal is a field, and a module over a field is a vector space.
:::

:::

:::

:::
