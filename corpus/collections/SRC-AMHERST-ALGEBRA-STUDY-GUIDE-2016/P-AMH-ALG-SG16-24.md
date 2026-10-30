---
schema: qual/card@1
id: P-AMH-ALG-SG16-24
kind: problem
title: Ideals of a field are trivial
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $F$ be a field and let $J\subseteq F$ be an ideal of $F$.
Prove that either $J=\{0\}$ or $J=F$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
If $J=\{0\}$, then the required conclusion holds.

::: pf-proof
This is one of the two alternatives in the statement.
:::

:::

::: {.pf-step #s1-2}
Suppose $J\neq\{0\}$.  Then $1\in J$.

::: pf-proof
Since $J$ is nonzero, choose $a\in J$ with $a\neq0$.  Because $F$ is a
field, $a$ has a multiplicative inverse $a^{-1}\in F$.  Since $J$ is an ideal,
multiplication by the ring element $a^{-1}$ preserves membership in $J$, so
$$
1=a^{-1}a\in J.
$$
:::

:::

::: {.pf-step #s1-3}
If $1\in J$, then $J=F$.

::: pf-proof
Let $x\in F$.  Since $1\in J$ and $J$ is an ideal,
$$
x=x\cdot1\in J.
$$
Thus $F\subseteq J$.  The reverse inclusion is part of the hypothesis
$J\subseteq F$, so $J=F$.
:::

:::

::: pf-step
Therefore
$$
\boxed{J=\{0\}\quad\text{or}\quad J=F}.
$$

::: pf-proof
If $J=\{0\}$, step [](#s1-1){.pf-ref} applies.  Otherwise step [](#s1-2){.pf-ref} gives $1\in J$, and
step [](#s1-3){.pf-ref} then gives $J=F$.
:::

:::

:::

:::
