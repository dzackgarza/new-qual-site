---
schema: qual/card@1
id: P-XWYKO
kind: problem
title: A single Jordan block of size $6$ for $T$ with $p_T(x)=\chi_T(x)=x^6$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Let $V$ be $6$-dimensional and let $T\in\Endo(V)$ satisfy
$$
T^6=0,
\qquad
T^5\ne0.
$$
Show that $T$ has a single Jordan block of size $6$.
:::

::: {.solution}
Write $m_T$ for the minimal polynomial and $\chi_T$ for the characteristic polynomial of $T$.

::: pf

::: {.pf-step #minpoly}
$m_T(x)=x^6$.

::: pf-proof
$T^6=0$ gives $m_T\mid x^6$, so $m_T=x^r$ with $r\le6$, and $T^5\ne0$ forces $r>5$.
:::

:::

::: pf-step
The Jordan form of $T$ is the single block $J_6(0)$.

::: pf-proof
All roots of $m_T$ are $0$, so $\chi_T(x)=x^6$ splits and $T$ has a Jordan form, with all blocks for the eigenvalue $0$.
The largest block has size equal to the exponent of $x$ in $m_T$, which is $6$ by step [](#minpoly){.pf-ref}, and the block sizes sum to $\dim V=6$, so there is exactly one block.
:::

:::

:::

:::
