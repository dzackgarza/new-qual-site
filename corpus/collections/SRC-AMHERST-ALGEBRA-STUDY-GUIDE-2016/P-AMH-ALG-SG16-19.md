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
(January 2010) Let $R$ be a commutative ring and $S\subseteq R$ a subset of $R$.
Define the annihilator of $S$ in $R$ to be
\[
\operatorname{Ann}(S)=\{r\in R\mid rs=0\text{ for every }s\in S\}.
\]
Prove that $\operatorname{Ann}(S)$ is an ideal of $R$.
:::

::: {.solution}
<1>1. The set $\operatorname{Ann}(S)$ is nonempty.

::: {.proof}
For every $s\in S$,
$$
0\cdot s=0.
$$
Hence $0\in\operatorname{Ann}(S)$.
:::

<1>2. The set $\operatorname{Ann}(S)$ is closed under subtraction.

::: {.proof}
Let $a,b\in\operatorname{Ann}(S)$.  For every $s\in S$,
$$
(a-b)s=as-bs=0-0=0.
$$
Therefore $a-b\in\operatorname{Ann}(S)$.
:::

<1>3. The set $\operatorname{Ann}(S)$ absorbs multiplication by arbitrary
elements of $R$.

::: {.proof}
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

<1>4. Therefore $\operatorname{Ann}(S)$ is an ideal of $R$.

::: {.proof}
Steps <1>1 and <1>2 show, by the subtraction criterion, that
$\operatorname{Ann}(S)$ is an additive subgroup of $R$.  Step <1>3 gives the
ideal absorption property.  Hence $\operatorname{Ann}(S)$ is an ideal.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
