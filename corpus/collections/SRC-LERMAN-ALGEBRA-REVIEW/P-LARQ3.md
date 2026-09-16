---
schema: qual/card@1
id: P-LARQ3
kind: problem
title: A unit multiple of an irreducible element is irreducible
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the commutative-ring, irreducible-element and unit hypotheses with Lerman practice problem 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nonzeroness, nonunit status and the factorization criterion directly from the definition of irreducibility."
---

::: {.problem}
Let $R$ be a commutative ring with identity.
Suppose $p\in R$ is irreducible and $u\in R$ is a unit.
Prove that $up$ is irreducible.
:::

::: {.solution}
<1>1. The element $up$ is nonzero and is not a unit.
::: {.proof}
Since $p$ is irreducible, $p\ne0$ and $p$ is not a unit. Multiplication by the unit $u$ is bijective, so $up\ne0$. If $up$ were a unit, then
$$
p=u^{-1}(up)
$$
would be a product of units and hence a unit, a contradiction.
:::

<1>2. Every factorization of $up$ has a unit factor.
::: {.proof}
Suppose
$$
up=ab.
$$
Multiplying by $u^{-1}$ gives
$$
p=(u^{-1}a)b.
$$
Because $p$ is irreducible, either $u^{-1}a$ is a unit or $b$ is a unit. In the first case, $a=u(u^{-1}a)$ is a product of units and hence is a unit. Therefore every factorization of $up$ has a unit factor. Together with <1>1, this is exactly the definition that $up$ is irreducible.
:::
:::
