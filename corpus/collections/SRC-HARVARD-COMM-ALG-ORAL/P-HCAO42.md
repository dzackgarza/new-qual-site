---
schema: qual/card@1
id: P-HCAO42
kind: problem
title: Product equals intersection for pairwise comaximal ideals
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Chinese Remainder Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $\mathfrak a_1,\ldots,\mathfrak a_r$ be ideals of a commutative ring $A$ such that $\mathfrak a_i+\mathfrak a_j=(1)$ whenever $i\ne j$.
Show that
\[
\prod_{i=1}^r \mathfrak a_i=\bigcap_{i=1}^r \mathfrak a_i.
\]
:::

::: {.solution}
<1>1. $\prod_i \mathfrak a_i \subseteq \bigcap_i \mathfrak a_i$.
::: {.proof}
the product $\mathfrak a_1 \cdots \mathfrak a_r$ is contained in each $\mathfrak a_i$ (since each factor is an ideal), hence in their intersection.
:::

<1>2. $\bigcap_i \mathfrak a_i \subseteq \prod_i \mathfrak a_i$.
<2>1. Base case $r = 2$: if $\mathfrak a_1 + \mathfrak a_2 = (1)$, then $\mathfrak a_1 \cap \mathfrak a_2 = \mathfrak a_1 \mathfrak a_2$.
::: {.proof}
choose $u \in \mathfrak a_1$, $v \in \mathfrak a_2$ with $u + v = 1$; for $x \in \mathfrak a_1 \cap \mathfrak a_2$, $x = x(u+v) = xu + xv \in \mathfrak a_1 \mathfrak a_2 + \mathfrak a_1 \mathfrak a_2 = \mathfrak a_1 \mathfrak a_2$ (since $x \in \mathfrak a_2$ and $u \in \mathfrak a_1$ give $xu \in \mathfrak a_1 \mathfrak a_2$, and $x \in \mathfrak a_1$ and $v \in \mathfrak a_2$ give $xv \in \mathfrak a_1 \mathfrak a_2$). <2>2. Inductive step: assume $\bigcap_{i=1}^{r-1} \mathfrak a_i = \prod_{i=1}^{r-1} \mathfrak a_i$.
:::
::: {.proof}
induction hypothesis.
:::
<2>3. $\prod_{i=1}^{r-1} \mathfrak a_i + \mathfrak a_r = (1)$.
::: {.proof}
$\mathfrak a_i + \mathfrak a_r = (1)$ for all $i < r$ implies $\prod_{i<r} \mathfrak a_i + \mathfrak a_r = (1)$ (standard: if $\mathfrak a + \mathfrak b = (1)$ and $\mathfrak a + \mathfrak c = (1)$, then $\mathfrak a + \mathfrak b \mathfrak c = (1)$). <2>4. Hence $\bigcap_{i=1}^r \mathfrak a_i = \left(\bigcap_{i=1}^{r-1} \mathfrak a_i\right) \cap \mathfrak a_r = \left(\prod_{i=1}^{r-1} \mathfrak a_i\right) \cap \mathfrak a_r = \left(\prod_{i=1}^{r-1} \mathfrak a_i\right) \mathfrak a_r = \prod_{i=1}^r \mathfrak a_i$.
:::
::: {.proof}
<2>2, <2>3, and the base case <2>1 applied to the two comaximal ideals $\prod_{i<r} \mathfrak a_i$ and $\mathfrak a_r$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
