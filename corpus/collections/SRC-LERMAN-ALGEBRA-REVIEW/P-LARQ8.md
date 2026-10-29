---
schema: qual/card@1
id: P-LARQ8
kind: problem
title: Coprime integers generate the unit ideal
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the equivalence between relative primality and generation of the unit ideal with Lerman practice problem 8."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved both implications directly using Bezout's identity and divisibility of integer linear combinations."
---

::: {.problem}
Prove that $m,n\in\ZZ$ are relatively prime if and only if $m\ZZ+n\ZZ=\ZZ$.
:::

::: {.solution}

::: pf

::: pf-step

If $m$ and $n$ are relatively prime, then they generate $\ZZ$.

::: pf-proof

Relative primality means $\gcd(m,n)=1$. By Bezout's identity there exist integers $a,b$ such that
$$
am+bn=1.
$$
Hence $1\in m\ZZ+n\ZZ$. Since $m\ZZ+n\ZZ$ is an ideal of $\ZZ$ containing $1$, it equals all of $\ZZ$.

:::

:::

::: pf-step

If $m\ZZ+n\ZZ=\ZZ$, then $m$ and $n$ are relatively prime.

::: pf-proof

The equality implies $1\in m\ZZ+n\ZZ$, so there exist integers $a,b$ with
$$
am+bn=1.
$$
Any common divisor $d$ of $m$ and $n$ divides every integer linear combination of them, hence divides $1$. Therefore every common divisor is a unit in $\ZZ$, so $\gcd(m,n)=1$. Thus $m$ and $n$ are relatively prime.

:::

:::

:::

:::
