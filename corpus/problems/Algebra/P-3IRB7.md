---
schema: qual/card@1
id: P-3IRB7
kind: problem
title: Whether $k[x_1,\ldots,x_n]$ is a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Polynomials
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Removed the false zero-constant-term description of (x1,x2) for n>2 and kept the common-divisor proof.
---

::: {.problem}
For which $n$ is the polynomial ring $k[x_1,\ldots,x_n]$ over a field $k$ a PID?
:::

::: {.solution}

::: pf

::: {.pf-step #small}

For $n\le1$, $k[x_1,\ldots,x_n]$ is a PID.

::: pf-proof

For $n=0$ the ring is the field $k$, whose only ideals are $0=(0)$ and $k=(1)$. For $n=1$ the ring $k[x_1]$ is a Euclidean domain under the degree, hence a PID.

:::

:::

::: {.pf-step #proper}

For $n\ge2$, the ideal $I=(x_1,x_2)$ is proper.

::: pf-proof

The evaluation homomorphism $x_1,\ldots,x_n\mapsto0$ sends every element of $I$ to $0$ and sends $1$ to $1$, so $1\notin I$.

:::

:::

::: {.pf-step #not-principal}

For $n\ge2$, the ideal $I=(x_1,x_2)$ is not principal.

::: pf-proof

Suppose $I=(d)$. Then $d$ divides both $x_1$ and $x_2$. In the UFD $k[x_1,\ldots,x_n]$, the irreducibles $x_1$ and $x_2$ are nonassociate, so their only common divisors are units. Thus $d$ is a unit and $I=(1)$, contradicting step [](#proper){.pf-ref}.

:::

:::

::: pf-step

$k[x_1,\ldots,x_n]$ is a PID exactly for $\boxed{n\le1}$.

::: pf-proof

This follows from steps [](#small){.pf-ref} and [](#not-principal){.pf-ref}.

:::

:::

:::

:::
