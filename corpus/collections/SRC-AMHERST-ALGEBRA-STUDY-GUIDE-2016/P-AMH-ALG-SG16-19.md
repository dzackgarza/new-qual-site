---
schema: qual/card@1
id: P-AMH-ALG-SG16-19
kind: problem
title: Annihilators are ideals
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
Let $R$ be a commutative ring and $S\subseteq R$ a subset of $R$.
Define the annihilator of $S$ in $R$ to be
$$
\operatorname{Ann}(S)=\{r\in R\mid rs=0\text{ for every }s\in S\}.
$$
Prove that $\operatorname{Ann}(S)$ is an ideal of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The set $\operatorname{Ann}(S)$ is nonempty.

::: pf-proof
For every $s\in S$,
$$
0\cdot s=0.
$$
Hence $0\in\operatorname{Ann}(S)$.
:::

:::

::: {.pf-step #s1-2}
The set $\operatorname{Ann}(S)$ is closed under subtraction.

::: pf-proof
Let $a,b\in\operatorname{Ann}(S)$.  For every $s\in S$,
$$
(a-b)s=as-bs=0-0=0.
$$
Therefore $a-b\in\operatorname{Ann}(S)$.
:::

:::

::: {.pf-step #s1-3}
The set $\operatorname{Ann}(S)$ absorbs multiplication by arbitrary
elements of $R$.

::: pf-proof
Let $r\in R$ and $x\in\operatorname{Ann}(S)$.  For every $s\in S$,
$$
(rx)s=r(xs)=r\cdot0=0.
$$
Thus $rx\in\operatorname{Ann}(S)$.  Since $R$ is commutative,
$$
xr=rx\in\operatorname{Ann}(S)
$$
as well.
:::

:::

::: pf-step
Therefore $\operatorname{Ann}(S)$ is an ideal of $R$.

::: pf-proof
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show, by the subtraction criterion, that
$\operatorname{Ann}(S)$ is an additive subgroup of $R$.  Step [](#s1-3){.pf-ref} gives the
ideal absorption property.  Hence $\operatorname{Ann}(S)$ is an ideal.
:::

:::

:::

:::
