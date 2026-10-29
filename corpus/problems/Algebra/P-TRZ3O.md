---
schema: qual/card@1
id: P-TRZ3O
kind: problem
title: $\Aut(\ZZ/p)$, $\Aut((\ZZ/p)^n)$, and $\Aut(\ZZ/n)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Matrix Groups
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source declares neither $p$ nor $n$; the statement takes $p$ prime and $n$ a positive integer.
---

::: {.problem}
Let $p$ be a prime and $n$ a positive integer. Identify
$$
\Aut(\ZZ/p\ZZ),
\qquad
\Aut((\ZZ/p\ZZ)^n),
\qquad
\Aut(\ZZ/n\ZZ).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #cyclic}
$\Aut(\ZZ/n\ZZ)\cong(\ZZ/n\ZZ)^\times$.

::: pf-proof
An endomorphism of the additive group $\ZZ/n\ZZ$ is determined by $1\mapsto a$, and it is multiplication by $a$.
It is invertible exactly when $a$ is a unit modulo $n$, and composition corresponds to multiplication of the residues $a$.
:::

:::

::: pf-step
$\Aut(\ZZ/p\ZZ)\cong(\ZZ/p\ZZ)^\times$, a cyclic group of order $p-1$.

::: pf-proof
This is step [](#cyclic){.pf-ref} with $n=p$; since $\ZZ/p\ZZ=\FF_p$ is a field, its multiplicative group is cyclic of order $p-1$.
:::

:::

::: pf-step
$\Aut((\ZZ/p\ZZ)^n)\cong\GL_n(\FF_p)$.

::: pf-proof
$(\ZZ/p\ZZ)^n$ is the additive group of $\FF_p^n$, and every additive map commutes with multiplication by the integers, which give all scalars of $\FF_p$.
So the group automorphisms are exactly the invertible $\FF_p$-linear maps.
:::

:::

:::

:::
