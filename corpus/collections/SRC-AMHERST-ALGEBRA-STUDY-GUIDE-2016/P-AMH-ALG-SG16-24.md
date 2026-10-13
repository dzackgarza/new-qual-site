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
(March 2005) Let $F$ be a field and let $J\subseteq F$ be an ideal of $F$.
Prove that either $J=\{0\}$ or $J=F$.
:::

::: {.solution}
<1>1. If $J=\{0\}$, then the required conclusion holds.

::: {.proof}
This is one of the two alternatives in the statement.
:::

<1>2. Suppose $J\neq\{0\}$.  Then $1\in J$.

::: {.proof}
Since $J$ is nonzero, choose $a\in J$ with $a\neq0$.  Because $F$ is a
field, $a$ has a multiplicative inverse $a^{-1}\in F$.  Since $J$ is an ideal,
multiplication by the ring element $a^{-1}$ preserves membership in $J$, so
$$
1=a^{-1}a\in J.
$$
:::

<1>3. If $1\in J$, then $J=F$.

::: {.proof}
Let $x\in F$.  Since $1\in J$ and $J$ is an ideal,
$$
x=x\cdot1\in J.
$$
Thus $F\subseteq J$.  The reverse inclusion is part of the hypothesis
$J\subseteq F$, so $J=F$.
:::

<1>4. Therefore
$$
\boxed{J=\{0\}\quad\text{or}\quad J=F}.
$$

::: {.proof}
If $J=\{0\}$, step <1>1 applies.  Otherwise step <1>2 gives $1\in J$, and
step <1>3 then gives $J=F$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required dichotomy.
:::
:::
