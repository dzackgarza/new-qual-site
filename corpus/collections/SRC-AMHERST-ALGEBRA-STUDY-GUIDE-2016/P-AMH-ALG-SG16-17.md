---
schema: qual/card@1
id: P-AMH-ALG-SG16-17
kind: problem
title: Ideals of $\ZZ$ containing relatively prime integers
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
(February 1982) Prove that if an ideal $I$ of the ring $\ZZ$ contains two relatively prime integers, then $I=\ZZ$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
There exist integers $a,b\in I$ and $m,n\in\ZZ$ such that
$$
ma+nb=1.
$$

::: pf-proof
By hypothesis, $I$ contains two relatively prime integers $a$ and $b$, so
$\gcd(a,b)=1$.  Bézout's identity therefore gives integers $m,n\in\ZZ$ with
$$
ma+nb=\gcd(a,b)=1.
$$
:::

:::

::: {.pf-step #s1-2}
One has $1\in I$.

::: pf-proof
Because $I$ is an ideal and $a,b\in I$, multiplication by arbitrary integers
gives
$$
ma\in I
\qquad\text{and}\qquad
nb\in I.
$$
Ideals are closed under addition, so step [](#s1-1){.pf-ref} gives
$$
1=ma+nb\in I.
$$
:::

:::

::: {.pf-step #s1-3}
Every integer belongs to $I$.

::: pf-proof
Let $x\in\ZZ$.  By step [](#s1-2){.pf-ref}, $1\in I$, and the ideal absorption property
gives
$$
x=x\cdot1\in I.
$$
Thus $\ZZ\subseteq I$.
:::

:::

::: pf-step
Therefore
$$
\boxed{I=\ZZ}.
$$

::: pf-proof
By definition $I\subseteq\ZZ$, while step [](#s1-3){.pf-ref} gives the reverse inclusion.
:::

:::

:::

:::
