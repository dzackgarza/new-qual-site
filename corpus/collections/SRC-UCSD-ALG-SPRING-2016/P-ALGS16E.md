---
schema: qual/card@1
id: P-ALGS16E
kind: problem
title: Whether $\mathbb{F}_9$ embeds in $\mathbb{F}_{27}$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
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
Let $K$ and $L$ be fields of orders $9$ and $27$, respectively.
Is $K$ isomorphic to a subfield of $L$?
:::


::: {.solution}
<1>1. The fields are, up to isomorphism, $K\cong\mathbf F_{3^2}$ and $L\cong\mathbf F_{3^3}$.
::: {.proof}
A finite field is determined up to isomorphism by its cardinality, and both cardinalities are powers of $3$.
:::

<1>2. A finite field $\mathbf F_{3^d}$ is a subfield of $\mathbf F_{3^n}$ if and only if $d\mid n$.
::: {.proof}
The subfields of $\mathbf F_{3^n}$ are exactly the fixed fields of subgroups of the cyclic Galois group $\operatorname{Gal}(\mathbf F_{3^n}/\mathbf F_3)\cong C_n$. Equivalently, their degrees over $\mathbf F_3$ are exactly the divisors of $n$.
:::

<1>3. Since $2\nmid3$, $\mathbf F_{3^2}$ is not isomorphic to a subfield of $\mathbf F_{3^3}$.
::: {.proof}
Apply Step <1>2 with $d=2$ and $n=3$.
:::

<1>4. Therefore $K$ is not isomorphic to a subfield of $L$.
::: {.proof}
Combine Steps <1>1 and <1>3.
:::
:::
