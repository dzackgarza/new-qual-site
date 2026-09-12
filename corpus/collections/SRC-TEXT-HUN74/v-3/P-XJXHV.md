---
schema: qual/card@1
id: P-XJXHV
kind: problem
title: Separability descends through intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Cornell Math 201C notes reproducing Hungerford V.3.12 and its two parts.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $E$ be an intermediate field extension in $K \leq E \leq F$.

1. Show that if $u\in F$ is separable over $K$, then $u$ is separable over $E$.

2. Show that if $F$ is separable over $K$, then $F$ is separable over $E$ and $E$ is separable over $K$.
:::

::: solution
<1>1. If $u\in F$ is separable over $K$, then $u$ is separable over $E$.
::: proof
Let
\[
m_K(x)\in K[x]
\]
be the minimal polynomial of $u$ over $K$, and let
\[
m_E(x)\in E[x]
\]
be the minimal polynomial of $u$ over $E$. Since $K[x]\subseteq E[x]$ and
$m_K(u)=0$, minimality of $m_E$ implies
\[
m_E\mid m_K\qquad\text{in }E[x].
\]

Because $u$ is separable over $K$, the polynomial $m_K$ has no repeated root in
a splitting field. Every divisor of a polynomial with distinct roots likewise
has distinct roots. Hence $m_E$ is separable, so $u$ is separable over $E$.
:::

<1>2. If $F/K$ is separable, then $F/E$ is separable.
::: proof
Let $u\in F$. Since $F/K$ is separable, $u$ is separable over $K$. By <1>1,
$u$ is separable over $E$. Since this holds for every $u\in F$, the extension
$F/E$ is separable.
:::

<1>3. If $F/K$ is separable, then $E/K$ is separable.
::: proof
Every element of $E$ is also an element of $F$. Since every element of $F$ is
separable over $K$, every element of $E$ is separable over $K$. Thus $E/K$ is
separable.
:::
:::
