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
\[
(r + (p)) \cdot (a + pA) = ra + pA.
\]
In particular, show that if $(p)$ is a maximal ideal, $A/pA$ is a vector space over the field $R/(p)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
The scalar multiplication $(r + (p)) \cdot (a + pA) = ra + pA$ is well-defined.

::: pf-proof

::: pf-step
Suppose $r + (p) = r' + (p)$ and $a + pA = a' + pA$.

::: pf-proof
setup of coset representatives.
:::

:::

::: pf-step
Then $r - r' = c p$ for some $c \in R$, and $a - a' \in pA$, so $a - a' = p u$ for some $u \in A$.

::: pf-proof
definition of ideals and submodules.
:::

:::

::: {.pf-step #s1-3}
Compute the difference of the outputs:
\[
ra - r'a' = r(a - a') + (r - r')a' = r(pu) + (cp)a' = p(ru + ca').
\]

::: pf-proof
ring and module arithmetic.
:::

:::

::: {.pf-step #s1-4}
Since $ru + ca' \in A$, $p(ru + ca') \in pA$.

::: pf-proof
definition of $pA = \{px : x \in A\}$.
:::

:::

::: pf-step
Hence $ra + pA = r'a' + pA$, so the action is independent of the choice of coset representatives.

::: pf-proof
step [](#s1-3){.pf-ref} and step [](#s1-4){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s2}
The action satisfies all module axioms:

::: pf-proof

::: pf-step
Distributivity over module addition:
\[
(r + (p)) \cdot \bigl((a + pA) + (b + pA)\bigr) = (r + (p)) \cdot (a + b + pA) = r(a+b) + pA = (ra + pA) + (rb + pA).
\]

::: pf-proof
distributivity in the $R$-module $A$: $r(a+b) = ra + rb$.
:::

:::

::: pf-step
Distributivity over ring addition:
\[
\bigl((r + (p)) + (s + (p))\bigr) \cdot (a + pA) = (r + s + (p)) \cdot (a + pA) = (r+s)a + pA = (ra + pA) + (sa + pA).
\]

::: pf-proof
module axiom $(r+s)a = ra + sa$.
:::

:::

::: pf-step
Compatibility with ring multiplication:
\[
\bigl((r + (p))(s + (p))\bigr) \cdot (a + pA) = (rs + (p)) \cdot (a + pA) = (rs)a + pA = r(sa) + pA = (r + (p)) \cdot (sa + pA).
\]

::: pf-proof
module axiom $(rs)a = r(sa)$.
:::

:::

::: pf-step
Action of the ring identity:
\[
(1_R + (p)) \cdot (a + pA) = 1_R a + pA = a + pA.
\]

::: pf-proof
module axiom $1_R a = a$.
:::

:::

:::

:::

::: {.pf-step #s3}
If $(p)$ is a maximal ideal in $R$, then $R/(p)$ is a field, and any module over a field is a vector space.

::: pf-proof
quotient of a commutative ring by a maximal ideal is a field.
:::

:::

::: pf-qed
Conclusion: $A/pA$ is an $R/(p)$-module, and is a vector space over $R/(p)$ when $(p)$ is maximal.
step [](#s1){.pf-ref}, step [](#s2){.pf-ref}, and step [](#s3){.pf-ref}.
:::

:::

:::
