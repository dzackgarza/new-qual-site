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
Prove that $m,n\in\mathbb Z$ are relatively prime if and only if $m\mathbb Z+n\mathbb Z=\mathbb Z$.
:::

::: {.solution}
<1>1. If $m$ and $n$ are relatively prime, then they generate $\mathbb Z$.
::: {.proof}
Relative primality means $\gcd(m,n)=1$. By Bezout's identity there exist integers $a,b$ such that
$$
am+bn=1.
$$
Hence $1\in m\mathbb Z+n\mathbb Z$. Since $m\mathbb Z+n\mathbb Z$ is an ideal of $\mathbb Z$ containing $1$, it equals all of $\mathbb Z$.
:::

<1>2. If $m\mathbb Z+n\mathbb Z=\mathbb Z$, then $m$ and $n$ are relatively prime.
::: {.proof}
The equality implies $1\in m\mathbb Z+n\mathbb Z$, so there exist integers $a,b$ with
$$
am+bn=1.
$$
Any common divisor $d$ of $m$ and $n$ divides every integer linear combination of them, hence divides $1$. Therefore every common divisor is a unit in $\mathbb Z$, so $\gcd(m,n)=1$. Thus $m$ and $n$ are relatively prime.
:::
:::
