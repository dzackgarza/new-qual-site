---
schema: qual/card@1
id: P-HCAO19
kind: problem
title: Example of a ring which is not Cohen--Macaulay
classification:
  areas:
  - algebra
  topics:
  - Cohen–Macaulay Rings
  - Noetherian Rings
  - Krull Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Give an example of a ring which is not Cohen--Macaulay.
:::

::: {.solution}
Let
\[
A=\left(k[x,y]/(x^2,xy)\right)_{(x,y)}.
\]
Then $A$ is a one-dimensional Noetherian local ring of depth $0$, hence is not
Cohen--Macaulay.

::: pf

::: {.pf-step #a-has-dimension-one}
The ring $A$ has Krull dimension $1$.

::: pf-proof
In $k[x,y]$,
\[
\sqrt{(x^2,xy)}=(x),
\]
because $(x^2,xy)=x(x,y)$ has radical $(x)$. Therefore
\[
\dim k[x,y]/(x^2,xy)
=\dim k[x,y]/(x)
=\dim k[y]
=1.
\]
Localizing at the maximal ideal $(x,y)$ preserves the chain
\[
(x)/(x^2,xy)\subsetneq(x,y)/(x^2,xy),
\]
so the local ring still has dimension $1$.
:::

:::

::: {.pf-step #x-annihilated-by-m}
The image of $x$ in $A$ is nonzero and is annihilated by the maximal
ideal $\mathfrak m=(x,y)A$.

::: pf-proof
The element $x$ is not in the ideal $(x^2,xy)$, so its image is nonzero before
localization and remains nonzero after localization at $(x,y)$. Moreover,
\[
x\cdot x=x^2=0,
\qquad
y\cdot x=xy=0
\]
in $A$. Hence every element of $\mathfrak m$ annihilates $x$.
:::

:::

::: {.pf-step #depth-is-zero}
Every element of $\mathfrak m$ is a zerodivisor, so
\[
\operatorname{depth}A=0.
\]

::: pf-proof
By step [](#x-annihilated-by-m){.pf-ref} every element of $\mathfrak m$ kills the same nonzero element $x$.
Thus no element of $\mathfrak m$ is $A$-regular. A nonzero local ring has depth
$0$ exactly when its maximal ideal contains no nonzerodivisor.
:::

:::

::: pf-step
Therefore $A$ is not Cohen--Macaulay.

::: pf-proof
A Noetherian local ring is Cohen--Macaulay precisely when its depth equals its
Krull dimension. Here step [](#a-has-dimension-one){.pf-ref} gives dimension $1$ and step [](#depth-is-zero){.pf-ref} gives depth $0$.
:::

:::

:::
:::
