---
schema: qual/card@1
id: FT-RVIGS
kind: theorem
title: Fermat's little theorem
prompts:
- State Fermat's little theorem.
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Finite Fields
relations: []
review: draft
---

::: {.theorem}
Let $p$ be a prime and let $a\in\ZZ$.
Then
$$
a^p\equiv a\pmod p,
$$
and if $p\nmid a$, then $a^{p-1}\equiv1\pmod p$.
:::

::: {.proof}
If $p\nmid a$, the class of $a$ lies in the group $\FF_p^\times$ of order $p-1$, so $a^{p-1}\equiv1\pmod p$ by Lagrange's theorem, and multiplying by $a$ gives $a^p\equiv a\pmod p$.
If $p\divides a$, both sides of $a^p\equiv a$ are $0$ modulo $p$.
:::
