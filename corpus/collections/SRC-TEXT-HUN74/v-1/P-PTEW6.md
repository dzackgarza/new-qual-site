---
schema: qual/card@1
id: P-PTEW6
kind: problem
title: Degrees and bases of $\QQ(\sqrt2,\sqrt3)$ and $\QQ(i,\sqrt3,\zeta_3)$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Bases
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
\envlist

1. If $F = \mathbb{Q}(\sqrt 2, \sqrt 3)$, compute $[F: \mathbb{Q}]$ and find a basis of $F/\mathbb{Q}$.

2. Do the same for $\mathbb{Q}(i, \sqrt 3, \zeta_3)$ where $\zeta_3$ is a complex third root of 1.
:::

::: {.solution}
We use the tower law in the following form: if $[L:K]=m$ with basis $\{x_i\}$ and $[M:L]=n$ with basis $\{y_j\}$, then $[M:K]=mn$ with basis $\{x_iy_j\}$.

::: pf

::: pf-step

(1) $[\QQ(\sqrt 2, \sqrt 3) : \QQ] = \boxed{4}$, with basis $\boxed{\{1, \sqrt 2, \sqrt 3, \sqrt 6\}}$.

::: pf-proof

::: {.pf-step #s1-1}

$[\QQ(\sqrt 2) : \QQ] = 2$ with basis $\{1,\sqrt2\}$.

::: pf-proof

$\sqrt2$ is irrational, so $X^2-2$ has no rational root and is the minimal polynomial of $\sqrt2$.

:::

:::

::: {.pf-step #s1-2}

$\sqrt 3 \notin \QQ(\sqrt 2)$, so $[\QQ(\sqrt 2, \sqrt 3) : \QQ(\sqrt 2)] = 2$ with basis $\{1,\sqrt3\}$.

::: pf-proof

Suppose $\sqrt 3 = a + b\sqrt 2$ with $a, b \in \QQ$. Squaring gives $3=a^2+2b^2+2ab\sqrt2$, so $ab=0$ because $\sqrt2$ is irrational. If $b=0$, then $\sqrt3=a\in\QQ$; if $a=0$, then $\sqrt6=2b\in\QQ$. Both contradict irrationality of $\sqrt3$ and $\sqrt6$. Hence $X^2-3$ has no root in $\QQ(\sqrt2)$ and is the minimal polynomial of $\sqrt3$ over it.

:::

:::

::: pf-qed

By the tower law and steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, the degree is $2\cdot2=4$ and the products $1,\sqrt2,\sqrt3,\sqrt2\sqrt3=\sqrt6$ form a basis.

:::

:::

:::

::: pf-step

(2) $[\QQ(i, \sqrt 3, \zeta_3) : \QQ] = \boxed{4}$, with basis $\boxed{\{1, i, \sqrt 3, i\sqrt 3\}}$.

::: pf-proof

::: {.pf-step #s2-1}

$\QQ(i, \sqrt 3, \zeta_3) = \QQ(i, \sqrt 3)$.

::: pf-proof

The complex third roots of $1$ other than $1$ are $\frac{-1 \pm i\sqrt 3}{2}\in\QQ(i,\sqrt3)$, and $\zeta_3=1$ also lies in $\QQ$.

:::

:::

::: {.pf-step #s2-2}

$[\QQ(i) : \QQ] = 2$ with basis $\{1,i\}$, and $[\QQ(i, \sqrt 3) : \QQ(i)] = 2$ with basis $\{1,\sqrt3\}$.

::: pf-proof

The polynomial $X^2 + 1$ has no rational root, so it is the minimal polynomial of $i$. Every element $a+bi$ of $\QQ(i)$ with $a,b\in\QQ$ is real only when $b=0$, so $\QQ(i)\cap\RR=\QQ$. Since $\sqrt3$ is real and irrational, $\sqrt 3 \notin \QQ(i)$, and $X^2-3$ is the minimal polynomial of $\sqrt3$ over $\QQ(i)$.

:::

:::

::: pf-qed

By step [](#s2-1){.pf-ref} and the tower law applied to step [](#s2-2){.pf-ref}, the degree is $2\cdot2=4$ and the products $1,i,\sqrt3,i\sqrt3$ form a basis.

:::

:::

:::

:::

:::
