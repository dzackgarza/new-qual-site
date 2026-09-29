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

::: {.problem}
Let $\mathfrak a_1,\ldots,\mathfrak a_r$ be ideals of a commutative ring $A$ such that $\mathfrak a_i+\mathfrak a_j=(1)$ whenever $i\ne j$.
Show that
\[
\prod_{i=1}^r \mathfrak a_i=\bigcap_{i=1}^r \mathfrak a_i.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #product-subset-intersection}
$\prod_i \mathfrak a_i \subseteq \bigcap_i \mathfrak a_i$.

::: pf-proof
The product $\mathfrak a_1 \cdots \mathfrak a_r$ is contained in each
$\mathfrak a_i$, since each factor is an ideal, hence in their intersection.
:::

:::

::: {.pf-step #two-comaximal-intersection-equals-product}
If $\mathfrak b+\mathfrak c=(1)$, then $\mathfrak b\cap\mathfrak c=\mathfrak b\mathfrak c$.

::: pf-proof
Choose $u\in\mathfrak b$ and $v\in\mathfrak c$ with $u+v=1$. For
$x\in\mathfrak b\cap\mathfrak c$,
$$
x=xu+xv,
$$
where $xu\in\mathfrak c\mathfrak b$ because $x\in\mathfrak c$, and
$xv\in\mathfrak b\mathfrak c$ because $x\in\mathfrak b$. Hence
$x\in\mathfrak b\mathfrak c$. The reverse inclusion is step [](#product-subset-intersection){.pf-ref} for two
ideals.
:::

:::

::: {.pf-step #comaximal-with-product}
If $\mathfrak a+\mathfrak b=(1)$ and $\mathfrak a+\mathfrak c=(1)$, then
$\mathfrak a+\mathfrak b\mathfrak c=(1)$.

::: pf-proof
Write $1=a+b$ and $1=a'+c$ with $a,a'\in\mathfrak a$, $b\in\mathfrak b$,
$c\in\mathfrak c$. Then
$$
1=(a+b)(a'+c)=(aa'+ac+ba')+bc\in\mathfrak a+\mathfrak b\mathfrak c.
$$
:::

:::

::: {.pf-step #intersection-subset-product}
$\bigcap_{i=1}^r\mathfrak a_i\subseteq\prod_{i=1}^r\mathfrak a_i$.

::: pf-proof
Induct on $r$; the case $r=1$ is trivial and the case $r=2$ is step [](#two-comaximal-intersection-equals-product){.pf-ref}.
For $r\ge3$, assume $\bigcap_{i<r}\mathfrak a_i=\prod_{i<r}\mathfrak a_i$.
Applying step [](#comaximal-with-product){.pf-ref} repeatedly to $\mathfrak a_r+\mathfrak a_i=(1)$ for $i<r$
gives $\prod_{i<r}\mathfrak a_i+\mathfrak a_r=(1)$. Step [](#two-comaximal-intersection-equals-product){.pf-ref} then gives
$$
\bigcap_{i=1}^r\mathfrak a_i
=\Bigl(\prod_{i<r}\mathfrak a_i\Bigr)\cap\mathfrak a_r
=\Bigl(\prod_{i<r}\mathfrak a_i\Bigr)\mathfrak a_r
=\prod_{i=1}^r\mathfrak a_i.
$$
:::

:::

::: pf-qed
Steps [](#product-subset-intersection){.pf-ref} and [](#intersection-subset-product){.pf-ref}.
:::

:::
:::
